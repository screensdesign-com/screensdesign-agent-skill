---
name: screensdesign-data
description: "Research iOS app design with the ScreensDesign MCP tools: discover apps by market metrics and AI classifications, inspect latest replay flows through paginated thumbnails and timestamped links, semantically search replay screens, analyze OCR and UI metadata, discover App Store screenshot metadata, compare developers, and read saved research. Use for competitor teardowns, onboarding or paywall research, UI references, revenue-filtered app discovery, app intelligence filters, replay-flow analysis, or saved ScreensDesign research."
---

# ScreensDesign Data

Use ScreensDesign for read-only iOS app discovery, competitor research, replay-flow analysis, semantic UI search, App Store screenshot metadata, structured app intelligence, and saved research.

## Load Only What You Need

| User intent | Read |
|-------------|------|
| Find apps, competitors, revenue bands, developers, categories, or resolve a pasted URL | `workflows/app-research.md` |
| Inspect replay flows, onboarding, paywalls, UI patterns, similar screens, or store-screen metadata | `workflows/screen-research.md` |
| Filter by audience, buildability, scores, onboarding steps, paywalls, quiz length, or detected patterns | `workflows/app-intelligence.md` |
| Read collections, saved groups, saved replay points, or saved store screens | `workflows/saved-research.md` |
| Suggest useful follow-up research | `workflows/completion-followups.md` |
| Need stable tool-choice or payload guidance | `references/tools.md` and `references/response-fields.md` |
| Need connection or authentication help | `references/connection.md` |

Use the live MCP input schemas for exact parameters and enums. Call `describe_screensdesign_mcp` for the current capability contract and `describe_app_intelligence_schema` for supported intelligence fields, enum values, scores, booleans, and pattern flags. If local guidance conflicts with live output, follow the live output.

## Core Workflow

1. Use `resolve_app_link` first for a pasted ScreensDesign URL, App Store URL, slug, store id, bundle, or app id.
2. Use `list_research_apps` for rich candidate records and `search_apps` for unified metadata, metric, and structured-intelligence filtering.
3. Use `app_detail` for app-level context. It does not return replay screens or visual assets.
4. Use `app_screens` to inspect the selected app's latest replay in timestamp order. Follow `pagination.next_offset` until `has_more=false` when the full flow matters.
5. Use `search_screens` for semantic concept search. It has no text/OCR mode, `search_mode` argument, or `vector_scope` argument.
6. Use `screen_detail` for complete text-only OCR and analysis of a selected screen. Use `find_similar_screens` for visual-neighbor discovery.
7. Use `search_store_screens` only for App Store screenshot metadata; it does not return screenshot images.
8. Use `list_collections` and `search_saved_research` for saved research. The server has no write tools.

## Visual And Privacy Boundary

- Only `app_screens` returns visual content: optional inline thumbnail `ImageContent` plus `thumbnail_url` in structured content.
- Treat each `app_screens` ResourceLink as an HTML detail page at the screen timestamp, not as the thumbnail image.
- No hosted tool returns replay videos, original images, full processed screens, PDFs, or downloadable flow documents.
- Other screen tools are text or metadata only. Do not promise image URLs from `screen_detail`, `search_screens`, `find_similar_screens`, `search_store_screens`, `app_detail`, or saved research.
- Never print OAuth tokens, API keys, authorization codes, callback URLs, or refresh tokens.

## Output

Present public app links, timestamped `frontend_url` links, available thumbnails, timestamps, visible text, and OCR excerpts. Keep internal ids for follow-up calls and omit them from prose unless requested. Treat revenue/download estimates and AI classifications or pattern flags as signals, then verify important claims against replay evidence.

Finish useful research with 2-3 adaptive next actions from `workflows/completion-followups.md`.

## Connection

If the MCP dependency is unavailable or authentication fails, read `references/connection.md`. A client may need a new session or MCP refresh after configuration.
