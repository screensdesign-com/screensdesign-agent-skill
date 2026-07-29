#!/usr/bin/env python3
"""Build and validate a deterministic ScreensDesign skill release."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import UTC, datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

REPOSITORY_URL = "https://github.com/screensdesign-com/screensdesign-agent-skill"
SKILL_NAME = "screensdesign-data"
MCP_CONTRACT_VERSION = "1"
ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / SKILL_NAME
MANIFEST_PATH = ROOT / "release.json"


def skill_version() -> str:
    markdown = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"^Release: `([0-9]+\.[0-9]+\.[0-9]+)`", markdown, re.MULTILINE)
    if match:
        return match.group(1)
    raise SystemExit("SKILL.md release declaration is missing.")


def release_files() -> list[Path]:
    return sorted(
        path
        for path in SKILL_ROOT.rglob("*")
        if path.is_file()
        and not any(part.startswith(".") for part in path.relative_to(SKILL_ROOT).parts)
        and "__pycache__" not in path.parts
    )


def content_sha256(files: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in files:
        relative = path.relative_to(SKILL_ROOT).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def build_zip(files: list[Path], output_path: Path) -> str:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_path, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = f"{SKILL_NAME}/{path.relative_to(SKILL_ROOT).as_posix()}"
            info = ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return hashlib.sha256(output_path.read_bytes()).hexdigest()


def expected_manifest(
    *, version: str, files: list[Path], archive_sha256: str, released_at: str
) -> dict[str, object]:
    tag = f"v{version}"
    return {
        "name": SKILL_NAME,
        "version": version,
        "minimum_supported_version": "1.0.0",
        "mcp_contract_version": MCP_CONTRACT_VERSION,
        "release_tag": tag,
        "released_at": released_at,
        "repository_url": REPOSITORY_URL,
        "source_url": f"{REPOSITORY_URL}/tree/{tag}/{SKILL_NAME}",
        "release_url": f"{REPOSITORY_URL}/releases/tag/{tag}",
        "install_command": (
            "npx -y skills add "
            f"{REPOSITORY_URL}/tree/{tag}/{SKILL_NAME}"
        ),
        "update_command": f"npx skills update {SKILL_NAME}",
        "content_sha256": content_sha256(files),
        "archive_sha256": archive_sha256,
        "files": [path.relative_to(SKILL_ROOT).as_posix() for path in files],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tag")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()

    version = skill_version()
    if args.tag and args.tag != f"v{version}":
        raise SystemExit(
            f"Release tag {args.tag!r} does not match the SKILL.md release v{version}."
        )

    files = release_files()
    archive_path = args.output_dir / f"{SKILL_NAME}-v{version}.zip"
    archive_hash = build_zip(files, archive_path)

    existing = json.loads(MANIFEST_PATH.read_text(encoding="utf-8")) if MANIFEST_PATH.exists() else {}
    released_at = str(
        existing.get("released_at") or datetime.now(tz=UTC).date().isoformat()
    )
    manifest = expected_manifest(
        version=version,
        files=files,
        archive_sha256=archive_hash,
        released_at=released_at,
    )

    if args.write_manifest:
        MANIFEST_PATH.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    if args.check:
        if not MANIFEST_PATH.exists():
            raise SystemExit("release.json is missing; run --write-manifest first.")
        actual = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        if actual != manifest:
            raise SystemExit(
                "release.json does not match the skill package; run --write-manifest."
            )

    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"Built {archive_path}")


if __name__ == "__main__":
    main()
