# ScreensDesign Agent Skill

Versioned companion instructions for using the hosted ScreensDesign MCP from Codex, Claude Code, Cursor, and other skill-aware agents.

The skill teaches agents how to:

- Discover and compare mobile apps using product, category, performance, and detected-pattern filters.
- Inspect detailed app evidence, recorded screens, chronological replays, and stored user flows.
- Verify before/after sequence claims instead of treating isolated screen matches as a full replay.
- Search App Store marketing creatives separately from recorded in-app UI.
- Find screens visually similar to a ScreensDesign screen or external reference image.
- Research developer portfolios and saved app collections.
- Cite public ScreensDesign links without exposing internal handles or withheld premium content.

## Install Version 1.0.2

```bash
npx -y skills add https://github.com/screensdesign-com/screensdesign-agent-skill/tree/v1.0.2/screensdesign-data
```

Update an installed copy:

```bash
npx skills update screensdesign-data
```

The skill declares its release near the top of `SKILL.md`. When the hosted MCP is connected, the agent calls `get_screensdesign_skill` once with that version to learn whether the installation is current, compatible, or needs an update.

## Connect The Hosted MCP

Endpoint:

```text
https://api.screensdesign.com/v1/mcp
```

Claude Code:

```bash
claude mcp add --transport http screensdesign "https://api.screensdesign.com/v1/mcp" --scope user
claude mcp login screensdesign
```

Codex:

```bash
codex mcp add screensdesign --url 'https://api.screensdesign.com/v1/mcp'
codex mcp login screensdesign
```

Cursor:

```json
{
  "mcpServers": {
    "screensdesign": {
      "url": "https://api.screensdesign.com/v1/mcp"
    }
  }
}
```

The server uses browser OAuth, is stateless, and exposes read-only research tools. A client may need a new conversation or MCP refresh after configuration.

## Repository Structure

```text
screensdesign-data/
|-- SKILL.md
|-- agents/openai.yaml
|-- workflows/
|   |-- app-research.md
|   |-- screen-research.md
|   |-- app-intelligence.md
|   |-- saved-research.md
|   `-- completion-followups.md
`-- references/
    |-- tools.md
    |-- response-fields.md
    `-- connection.md
```

`SKILL.md` stays compact and routes the agent to focused supporting files only when needed.

## Release Process

Every published release uses a semantic Git tag such as `v1.0.2`. The tag must match the release declared in `screensdesign-data/SKILL.md`.

Run the release builder before tagging:

```bash
python scripts/build_release.py --write-manifest
python scripts/build_release.py --check --tag v1.0.2
```

The release manifest records the immutable content and ZIP hashes. Pushing the matching tag validates the package and creates a GitHub Release containing the ZIP and manifest. The hosted MCP vendors that exact package so authenticated clients can read the current `SKILL.md` or download the release through MCP resources.
