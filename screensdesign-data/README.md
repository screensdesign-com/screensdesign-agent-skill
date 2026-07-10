# ScreensDesign Data Skill

This folder is the installable `screensdesign-data` skill. Agent clients discover the skill from `SKILL.md`; the other files are supporting resources that the agent can read when `SKILL.md` routes it to them.

## File Structure

```text
screensdesign-data/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
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

## How Agents Load It

- Skill discovery uses the frontmatter in `SKILL.md`, especially `name` and `description`.
- When the skill triggers, the agent reads `SKILL.md`.
- Supporting files inside this folder are available by relative path, but they are not all loaded automatically.
- `SKILL.md` should route the agent to the right workflow or reference file so context stays small.
- If this folder is installed as one skill, the `workflows/` files are supporting docs, not separate skills.
- If you want separately discoverable skills, each separate skill folder needs its own `SKILL.md`.

Codex, Claude Code, Cursor, Windsurf, and similar skill-aware agents follow this same general pattern: a skill folder has one primary `SKILL.md`, and bundled resources can be read when needed. Exact installation commands differ by client.
