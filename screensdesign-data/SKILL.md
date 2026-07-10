---
name: screensdesign-data
version: 2026-07-10.agent-guide.1
description: Use ScreensDesign mobile app design research through the ScreensDesign MCP tools - a searchable iOS app database with revenue/downloads, full replay screen recordings, App Store screenshots, semantic screen search, app intelligence classification, and replay-screen PDF contact sheets. Trigger when a user asks for app design research, onboarding flow examples, paywall examples, UI/screen references, App Store screenshot research, competitor app teardowns, revenue-filtered app discovery, app intelligence filters (target audience, buildability, gamification, onboarding steps, paywall counts), replay PDFs, or saved ScreensDesign research.
---

# ScreensDesign Data

Use ScreensDesign for iOS app discovery, competitor teardowns, replay screen research (onboarding, paywalls, in-app UI), App Store screenshot research, structured app intelligence filtering, replay PDF contact sheets, and saved research.

## Load Only What You Need

This skill uses progressive disclosure. Read the focused file that matches the request:

| User intent | Read |
|-------------|------|
| Find apps, competitors, revenue-filtered markets, developers, categories, or resolve a pasted URL | `workflows/app-research.md` |
| Research replay screens, onboarding flows, paywalls, UI patterns, replay PDFs, or App Store screenshots | `workflows/screen-research.md` |
| Filter apps by target audience, buildability, gamification, onboarding steps, paywall counts, or detected patterns | `workflows/app-intelligence.md` |
| Read the user's collections, saved groups, saved replay points, or saved store screens | `workflows/saved-research.md` |
| Decide what to suggest after completing a research task | `workflows/completion-followups.md` |
| Need the full tool list with exact parameters | `references/tools.md` |
| Need returned field names or payload shapes | `references/response-fields.md` |
| Need connection/auth setup details | `references/connection.md` |

Prefer live schema tools when MCP is connected: `describe_screensdesign_mcp` for the current tool surface and authenticated account, `describe_app_intelligence_schema` for current app-context fields, enum values, and pattern flags. If the live tool output disagrees with local docs, follow the live tool output.

## Core Rules

1. Use MCP tools when available. The server is read-only (`mcp:read`); never promise saving or writing through it.
2. Never print OAuth tokens, API keys, authorization codes, callback URLs, or refresh tokens.
3. Use `resolve_app_link` first when the user pastes a ScreensDesign, App Store, or replay PDF URL, slug, store id, or bundle.
4. Use `list_research_apps` or `search_apps` for discovery; `list_research_apps` returns richer research payloads with `public_links` and `internal_refs`.
5. Use `search_app_intelligence` for structured app-context filters and onboarding/paywall counts; keep free text out of typed filters.
6. Use `search_screens` for replay UI research: `search_mode="text"` for OCR/exact wording, `search_mode="semantic"` for concepts. Use `search_store_screens` for App Store screenshots.
7. `app_screen_pdf` and `screen_pdf_detail` return a PDF ResourceLink plus a `screen_index` manifest. Open the PDF first for the visual flow, then call `screen_detail` on interesting `screen_id`s for OCR, metadata, and assets.
8. Present public links (`web_url`, `appstore_url`, `public_links.latest_replay_pdf`), timestamps, visible text, and OCR snippets to users. Keep `internal_refs` ids for follow-up calls; do not show raw ids unless asked.
9. Treat revenue and download figures as estimates, and AI classifications/patterns as signals, unless the response says otherwise.
10. Finish useful research by suggesting 2-3 adaptive next actions; read `workflows/completion-followups.md` for the decision pattern.

## Hosted MCP Setup

Use the hosted Streamable HTTP MCP server:

```text
https://api.screensdesign.com/v1/mcp
```

Install or update this skill:

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

Other MCP clients: configure a remote Streamable HTTP MCP server named `screensdesign` at the hosted MCP URL above, then use the client OAuth/browser-login flow if supported. OAuth 2.1 discovery and dynamic client registration are automatic. For clients without OAuth support, use a developer API key (`sd_key_...`) from `https://screensdesign.com/mcp/keys` as `Authorization: Bearer`; see `references/connection.md`.

If MCP tools do not reload in the current session after setup, ask the user to open a new session or restart/refresh the MCP client.
