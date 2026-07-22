# ScreensDesign Agent Skill

Public agent instructions for using the read-only ScreensDesign MCP server for iOS app and UI research.

## What It Supports

- Discover apps by name, category, developer, revenue, downloads, rating, and replay/store-screen availability.
- Filter apps with structured intelligence such as target audience, niche status, buildability, scores, onboarding steps, paywall counts, quiz length, and detected patterns.
- Resolve pasted ScreensDesign or App Store links and common app identifiers.
- Inspect an app's latest replay as an ordered, paginated sequence with inline thumbnails and timestamped public page links.
- Search replay-screen concepts semantically and inspect complete text-only OCR/UI analysis for selected screens.
- Find visual-neighbor screens from a known replay screen.
- Discover App Store screenshot metadata such as count, order, and dimensions.
- Read app collections, saved groups, saved replay points, and saved store-screen records.

The visual boundary is intentional: only `app_screens` returns thumbnail images. Other hosted screen tools return text or metadata, and no tool returns replay videos, original/full-size images, PDFs, or downloadable flow documents.

## Repository Structure

```text
screensdesign-agent-skill/
|-- README.md
`-- screensdesign-data/
    |-- SKILL.md
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

`screensdesign-data/SKILL.md` is the installable entrypoint. Supporting files contain stable workflow and payload guidance; exact parameters and enums come from the live MCP schemas.

## Hosted MCP

Use the stateless Streamable HTTP endpoint:

```text
https://api.screensdesign.com/v1/mcp
```

OAuth browser login is preferred. Clients without MCP OAuth support can use a developer API key created at `https://screensdesign.com/mcp/keys`. Keys belong in client configuration or environment variables, never in chat.

The MCP scope is read-only (`mcp:read`). The user must remain an active organization member, and production access may require an active ScreensDesign Pro subscription.

### Claude Code

```bash
claude mcp add --transport http screensdesign "https://api.screensdesign.com/v1/mcp" --scope user
claude mcp login screensdesign
```

### Codex

```bash
codex mcp add screensdesign --url 'https://api.screensdesign.com/v1/mcp'
codex mcp login screensdesign
```

### Cursor

```json
{
  "mcpServers": {
    "screensdesign": {
      "url": "https://api.screensdesign.com/v1/mcp"
    }
  }
}
```

See `screensdesign-data/references/connection.md` for API-key fallback examples and troubleshooting.

## Install The Skill

```bash
npx -y skills add hashtagfox/screensdesign-agent-skill
```

Skill source:

```text
https://github.com/hashtagfox/screensdesign-agent-skill/tree/main/screensdesign-data
```

After installation, configure the MCP endpoint separately if the client does not install declared MCP dependencies automatically. Open a new agent session or refresh the MCP client when newly added tools are not visible.

## Contract Maintenance

The live MCP tool schemas are authoritative for parameters, defaults, limits, category values, and paywall enums. The skill deliberately avoids copying complete schemas so backend changes do not leave agents with stale call signatures.

Use `describe_screensdesign_mcp` for the current tool surface and privacy contract, and `describe_app_intelligence_schema` for intelligence fields, enums, scores, booleans, and pattern flags.
