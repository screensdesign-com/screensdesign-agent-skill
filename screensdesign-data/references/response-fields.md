# ScreensDesign Response Guidance

Use live tool output as the source of truth. The hosted server sanitizes private metadata and visual URLs from every tool response; only `app_screens.thumbnail_url` is explicitly allowed.

## App Search

`search_apps` returns `query`, `total`, `limit`, `offset`, echoed `filters`, and `results`.

Each result contains app identity, developer/category metadata, monthly revenue/download estimates, rating and dates, `appstore_url`, `web_url`, and an `intelligence` block:

- `intelligence.app_context`: public classification fields such as audiences, app types, opportunity/buildability fields, scores, risks, and booleans.
- `intelligence.all_in_one`: detected patterns, onboarding summary, radar axes, main flows, unique onboarding, and learning notes.

`list_research_apps` and `resolve_app_link` return richer app records with:

- `public_links.app` and `public_links.app_store` for users.
- `internal_refs` for follow-up calls.
- `enhanced_description`, `classification`, and `replay_summary`.

No hosted app response exposes `icon_url`.

## App Detail

`app_detail` returns app-level metadata plus:

- `latest_ai_patterns`: the public subset of the latest replay analysis.
- `revenue_list` and up to five `reviews_sample` items.
- `latest_replay`: replay id, duration, recording date, onboarding/paywall summary, screen count, ordering, and flow intelligence.
- `videos[]`: identifiers, dates, durations, onboarding-step counts, and paywall types; no video URLs.
- `store_screens[]`: ids, dimensions, order, and creation dates; no screenshot URLs.

It does not return replay `screens[]`. Use `app_screens` for those.

## App Screens

`app_screens` returns both structured content and MCP content blocks.

Structured content contains:

- `app`: compact app/developer/category metadata and public app links.
- `latest_replay`: replay metadata, screen count, ordering, and flow intelligence.
- `pagination`: `total`, `limit`, `offset`, `returned`, `has_more`, and `next_offset`.
- `screens[]`: `id`, `position`, `timestamp`, `app_video_id`, labels/tags, full OCR text and annotations, public screen description fields, optional onboarding/paywall analysis, `thumbnail_url`, and timestamped `frontend_url`.

MCP content begins with a page summary. Each screen then has a caption, an optional WebP thumbnail `ImageContent`, and a separately labeled HTML ResourceLink. The ResourceLink is not the thumbnail asset.

## Screen Search And Detail

`search_screens` returns `query`, `search_mode="semantic"`, pagination fields, top-level deduplicated `apps[]`, and `results[]`. Each result references its app with `app_id` and includes timestamp/replay metadata, OCR excerpt, description, labels/tags, screen/funnel classification, actions, visible text, components, layout/style, design patterns, and monetization signals.

It does not return image URLs, nested full app objects, match scores, or semantic-fallback errors.

`screen_detail` returns one screen's position, timestamp, full OCR and annotations, labels/tags, public description fields, optional onboarding/paywall analysis, a compact `app`, and replay metadata. It does not return raw `vsearch_data`, embedding fields, or visual assets.

`find_similar_screens` returns `source`, `mode`, top-level `apps`, and text-only `results`. Modes are `visual_similarity` and `same_app_neighbors`; no similarity score is exposed.

## Store Screens

`search_store_screens` returns `query`, list pagination fields, top-level deduplicated `apps[]`, and results containing `id`, `app_id`, dimensions, order, and creation date. It does not return `image_url` or `thumbnail_url`.

## Saved Research

`list_collections` returns `app_collections[]` and/or `saved_groups[]` with names and counts.

`search_saved_research` returns `groups[]`, `saved_points[]`, and `saved_store_screens[]`. Saved points expose descriptions, timestamps, `app_video_id`, app metadata, and creation dates. Saved store-screen items expose descriptions, `store_screen_id`, app metadata, and creation dates. Visual asset URLs are removed.

## Errors

- HTTP 401 indicates missing/invalid credentials, missing scope, inactive membership, or a Pro-access failure. Follow the OAuth discovery metadata in `WWW-Authenticate` or fix the configured API key.
- HTTP 429 includes `Retry-After`; wait before retrying.
- Invalid ids and apps without an enabled replay surface as tool errors. Verify identifiers from earlier results and continue with other candidates when appropriate.
