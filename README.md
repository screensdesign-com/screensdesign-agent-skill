# ScreensDesign Agent Skill

Public agent instructions for using ScreensDesign app, replay screen, App Store screenshot, app intelligence, and saved research data from Codex, Claude Code, Cursor, Windsurf, and other agent clients.

Recommended repository name:

```text
screensdesign-agent-skill
```

## What This Gives Agents

- How to search the ScreensDesign iOS app database by name, category, revenue, downloads, and rating.
- How to resolve pasted ScreensDesign, App Store, or replay PDF URLs to app records.
- How to research full replay screen recordings: onboarding flows, paywalls, and in-app UI.
- How to search replay screens by OCR text or semantic embeddings, and find visually similar screens.
- How to search current App Store screenshots.
- How to filter apps with structured app intelligence: target audience, buildability, gamification, onboarding steps, paywall counts, and detected onboarding patterns.
- How to use replay-screen PDF contact sheets: open the PDF for the visual flow, then drill into screen ids.
- How to read the user's saved collections, saved replay points, and saved App Store screens.
- How to present public links, timestamps, and OCR text to users while keeping internal ids for follow-up calls.

## Repository Structure

```text
screensdesign-agent-skill/
|-- README.md
`-- screensdesign-data/
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

`SKILL.md` is the entrypoint. The workflow and reference files are bundled resources that agents can read on demand.

## How Skill Loading Works

Skill-aware agents do not usually load every file in a skill folder into context up front.

1. The client indexes the skill metadata in `SKILL.md`, especially `name` and `description`.
2. When a user request matches the description, the agent reads `SKILL.md`.
3. `SKILL.md` routes the agent to supporting files such as `workflows/screen-research.md` or `references/tools.md`.
4. The agent can read files inside the installed skill folder by relative path, as long as the folder was installed/copied with those files.

This means splitting a skill into folders and Markdown files works well. The important rule is that the top-level `SKILL.md` must clearly mention the supporting files and when to read them.

If `screensdesign-data/` is installed as one skill, the files under `workflows/` are supporting docs, not separately discoverable skills. If you want separately discoverable skills, create separate folders and give each one its own `SKILL.md`.

## Hosted MCP

Use the hosted Streamable HTTP MCP server:

```text
https://api.screensdesign.com/v1/mcp
```

Install or update the skill:

```bash
npx -y skills add hashtagfox/screensdesign-agent-skill
```

Claude Code:

```bash
npx -y skills add hashtagfox/screensdesign-agent-skill
claude mcp add --transport http screensdesign "https://api.screensdesign.com/v1/mcp" --scope user
claude mcp login screensdesign
```

Codex:

```bash
npx -y skills add hashtagfox/screensdesign-agent-skill
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

Other MCP clients: configure a remote Streamable HTTP MCP server named `screensdesign` at the hosted MCP URL above, then use the client OAuth/browser-login flow if supported. There is no single JSON shape that works for every MCP client.

When the client asks for authorization, approve ScreensDesign in the browser. OAuth discovery and dynamic client registration are automatic; the client only needs the URL. Developer API keys (`sd_key_...`) remain available at `https://screensdesign.com/mcp/keys` for clients that do not support remote MCP OAuth; pass them as `Authorization: Bearer sd_key_...`. See `screensdesign-data/references/connection.md` for per-client API-key fallback snippets.

The server is read-only (`mcp:read` scope). There are no write tools.

## Agent Skill

Install the skill with:

```bash
npx -y skills add hashtagfox/screensdesign-agent-skill
```

Skill repo:

```text
https://github.com/hashtagfox/screensdesign-agent-skill
```

Skill source folder:

```text
https://github.com/hashtagfox/screensdesign-agent-skill/tree/main/screensdesign-data
```

For older agents without the skills CLI, ask the agent:

```text
Install screensdesign-data from https://github.com/hashtagfox/screensdesign-agent-skill/tree/main/screensdesign-data
```

Manual install:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R screensdesign-data "${CODEX_HOME:-$HOME/.codex}/skills/screensdesign-data"
```

## Agent Handoff

Paste this into an agent after the MCP connector is configured:

```text
Use ScreensDesign as an agent data source for iOS app design research: app database with revenue/downloads, full replay screen recordings, App Store screenshots, app intelligence classification, and replay-screen PDF contact sheets.

Hosted MCP URL: https://api.screensdesign.com/v1/mcp
API key fallback (sd_key_...): https://screensdesign.com/mcp/keys
Skill install: npx -y skills add hashtagfox/screensdesign-agent-skill
Skill repo: https://github.com/hashtagfox/screensdesign-agent-skill
Skill source folder: https://github.com/hashtagfox/screensdesign-agent-skill/tree/main/screensdesign-data

Before answering ScreensDesign questions:
1. If the ScreensDesign skill is missing or stale, install/update it with: npx -y skills add hashtagfox/screensdesign-agent-skill
2. If the MCP client asks for authorization, open the browser login and approve ScreensDesign.
3. If the current session cannot see the hosted MCP server after configuration, say that a new agent session or MCP client restart/refresh is needed.
4. Use resolve_app_link first when the user pastes a ScreensDesign, App Store, or replay PDF URL.
5. Use list_research_apps or search_apps for app/category/revenue discovery.
6. Use search_app_intelligence for structured filters such as target audience, buildability, gamification, onboarding step counts, and paywall counts; call describe_app_intelligence_schema when unsure about fields or enum values.
7. Use search_screens for replay UI research (search_mode="text" for OCR/exact wording, search_mode="semantic" for concepts) and search_store_screens for App Store screenshots.
8. app_screen_pdf and screen_pdf_detail return a PDF ResourceLink plus a screen_id manifest. Open the PDF first for the visual flow, then call screen_detail on interesting screen_ids.
9. Present public links (web_url, appstore_url, latest_replay_pdf), timestamps, visible text, and OCR snippets to users. Keep internal ids for follow-up calls; do not show raw ids unless asked.
10. Do not ask the user to paste a ScreensDesign API key into chat. If OAuth is unavailable, ask the user to configure an sd_key_ from https://screensdesign.com/mcp/keys outside chat.
11. Do not print OAuth tokens, API keys, authorization codes, callback URLs, or refresh tokens in status messages, command transcripts, or final notes.
```

## Notes

The server is stateless Streamable HTTP; each request is authenticated independently. The skill keeps the full tool and field references in `screensdesign-data/references/` so agents can load that detail only when they need it.
