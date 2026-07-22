# ScreensDesign MCP Usage

Use the hosted read-only Streamable HTTP server at `https://api.screensdesign.com/v1/mcp`.

## Live Contract First

Use the MCP tool schemas for exact arguments, defaults, limits, category values, and paywall enums. Do not reconstruct parameters from this file.

- Call `describe_screensdesign_mcp` for the current tool list, schema version, visual/privacy boundary, and authentication method.
- Call `describe_app_intelligence_schema` before nontrivial app-intelligence filtering. Only named `search_apps` parameters are filterable; schema fields are documentation, not arbitrary filters.

## Tool Choice

| Need | Tool | Key behavior |
|------|------|--------------|
| Rich app candidates | `list_research_apps` | Returns descriptions, classification, replay summary, public links, and internal follow-up refs |
| Unified app search | `search_apps` | Filters metadata, metrics, app context, scores, and onboarding/paywall intelligence |
| Resolve a pasted link or identifier | `resolve_app_link` | Accepts ScreensDesign/App Store links and common app identifiers |
| App-level context | `app_detail` | Returns metadata, revenue history, reviews, latest-replay summary, video metadata, and store-screen metadata; no visuals or replay screens |
| Browse a latest replay | `app_screens` | Returns an ordered, paginated flow with optional inline thumbnails and timestamped page links |
| Search replay UI concepts | `search_screens` | Semantic AI search over screen descriptions and curated UI intelligence |
| Inspect one screen | `screen_detail` | Complete text-only OCR and public analysis metadata |
| Find visual neighbors | `find_similar_screens` | Uses visual similarity when possible, otherwise returns same-app neighbors |
| Discover store-screen records | `search_store_screens` | Metadata only; no screenshot image assets |
| Research publishers | `search_developers` | Portfolio and market metadata |
| Read saved research | `list_collections`, `search_saved_research` | Authenticated user's collections and organization saved groups/items |

## App Intelligence

Use `search_apps` named parameters for supported array fields, enums, booleans, score ranges, detected/excluded patterns, and onboarding/paywall counts.

- Array filters match all requested values by default; set `app_context_match_any=true` to match any requested array value.
- Use `detected_patterns` and `excluded_patterns` only with flags returned by `describe_app_intelligence_schema`.
- Use `aio_text` for heuristic concepts without a dedicated parameter, such as gamification, personalization, social proof, streaks, or commitment.
- Do not send `app_context_filters` or `has_gamification`; neither is part of the hosted schema.

## Latest Replay Browsing

Use `app_screens` after selecting an app:

1. Start with the default page or request up to 10 screens.
2. Read `screens` in `position` and timestamp order.
3. Use `pagination.next_offset` while `pagination.has_more` is true.
4. Treat inline `ImageContent` as the thumbnail and the following ResourceLink as the separate HTML screen page.
5. Use `frontend_url` to open the public app page at that exact replay timestamp.
6. Pass interesting screen ids to `screen_detail` or `find_similar_screens`.

`app_screens` always uses the latest enabled replay. It does not accept an `app_video_id` for an older recording.

## Screen Search

A non-empty `search_screens.query` always performs semantic search. Scope it with app, category, paywall type, and market bounds when useful. Omitting the query returns recent screen records rather than an OCR text search.

Results contain text and UI intelligence, with app records deduplicated in top-level `apps` and referenced by `app_id`. They do not contain image assets, match scores, or fallback error fields.

`find_similar_screens.mode` is `visual_similarity` when an image vector exists and `same_app_neighbors` otherwise.

## Store Screens And Saved Research

`search_store_screens` searches app/developer/category metadata, not text inside screenshots. Results expose ids, dimensions, order, timestamps, and top-level app references; image and thumbnail URLs are removed.

`search_saved_research` returns saved group and item metadata. Hosted sanitization removes visual asset URLs, including saved replay-point screen URLs.
