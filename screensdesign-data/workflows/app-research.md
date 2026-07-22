# App Research Workflow

Use this workflow for app discovery, competitor discovery, revenue bands, pasted URLs, app context, developers, and categories.

## Choose The App Tool

- Use `resolve_app_link` first for a pasted ScreensDesign URL, App Store URL, slug, store id, bundle, or app id.
- Use `list_research_apps` for rich candidates with descriptions, classifications, replay summaries, public links, and internal refs.
- Use `search_apps` for unified metadata, metric, and structured-intelligence filtering.
- Use `app_detail` after selecting an app for revenue history, reviews, latest-replay summary, video metadata, and store-screen metadata. It returns no replay screens or visuals.
- Use `search_developers` for publisher and portfolio research.
- Read category values from the live input schema; common aliases and legacy codes are normalized by the server.

## Market Filters

Treat revenue and downloads as monthly estimates. Translate fuzzy requests into explicit ranges and report the range used. Add `has_replays=true` when the user needs replay evidence and `has_store_screens=true` when store-screen records matter.

Use the live schema for exact filter and sort values. Do not inspect credentials or local application configuration to invent hidden options.

## Drill Into A Shortlist

1. Call `app_detail` for app-level context.
2. Call `app_screens` for the strongest apps and paginate through the latest replay when sequence matters.
3. Call `search_screens` with `app_ids` for semantic discovery of specific concepts across the shortlist.
4. Call `screen_detail` on important ids for complete OCR and UI analysis.
5. Call `search_store_screens` only for store-screen metadata such as order and dimensions.

## Output

Lead with the scope, result count, and filters used. Compare apps with revenue, downloads, rating, positioning, classifications, and public links. Keep internal ids out of prose unless requested.

Do not claim that `app_detail` includes sample screens, that store-screen search includes images, or that the MCP exposes replay videos.
