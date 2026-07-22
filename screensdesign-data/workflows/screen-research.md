# Screen Research Workflow

Use this workflow for ordered replay flows, onboarding and paywall analysis, semantic UI discovery, screen details, visual neighbors, and App Store screenshot metadata.

## Choose The Screen Tool

- Use `app_screens` to browse one app's latest replay sequentially with thumbnails and timestamped public page links.
- Use `search_screens` to find concepts semantically across apps or within an `app_id`/`app_ids` scope.
- Use `screen_detail` for full OCR and public structured analysis of one screen.
- Use `find_similar_screens` to find visual neighbors from a known screen id.
- Use `search_store_screens` to discover App Store screenshot records. It returns metadata, not screenshot images.

## Browse A Replay Flow

1. Call `app_screens(app_id=...)`.
2. Read screens in `position` and timestamp order.
3. Continue with `pagination.next_offset` until `has_more=false` when completeness matters.
4. Interpret inline ImageContent as a thumbnail. Interpret the separately labeled ResourceLink as the public HTML page at that timestamp.
5. Use OCR, visible text, UI components, screen type, funnel stage, and flow intelligence to explain the sequence.
6. Call `screen_detail` for screens requiring exact copy or deeper analysis.

The tool uses the latest enabled replay and exposes at most 10 screens per page. It does not expose older recordings by `app_video_id`.

## Semantic Search

Use a concise conceptual query such as "streak celebration", "lifetime offer paywall", or "commitment screen". `search_screens` always searches semantically when a query is present; there is no exact OCR/text mode, `search_mode` parameter, `vector_scope`, match score, or text fallback.

Scope results with the live app/category/paywall/market filters when useful. App metadata is deduplicated in top-level `apps` and joined to results through `app_id`.

## Similar Screens

Use `find_similar_screens(screen_id)` after identifying a strong reference. Treat `mode="visual_similarity"` as cross-app visual-neighbor results and `mode="same_app_neighbors"` as the fallback for screens without an image vector. Results are text-only.

## Store-Screen Metadata

`search_store_screens.query` matches app, developer, and category metadata—not screenshot copy. Compare counts, order, and dimensions, and use the returned public app links for any separate visual inspection. Do not promise screenshot image URLs through MCP.

## Output

For replay flows, describe the sequence with positions and timestamps, cite OCR/visible text as evidence, and show available thumbnails and `frontend_url` links. For semantic results, explain the conceptual matches without inventing similarity scores. Keep screen ids for follow-up calls unless the user requests them.
