# ScreensDesign MCP Tools

Hosted Streamable HTTP MCP server:

```text
https://api.screensdesign.com/v1/mcp
```

All research tools are read-only. Revenue and download filters are estimated monthly USD and installs. `offset` is zero-based. Live input schemas are authoritative and include allowed enum values.

## Capability And Skill

### `get_screensdesign_skill(installed_version=None, include_content=False)`

Check whether the loaded `screensdesign-data` skill is current. Pass the release declared near the top of `SKILL.md` once per conversation. The response reports `current`, `update_available`, `incompatible`, `ahead`, or `unreported`, plus the latest release, compatibility, update command, hashes, and MCP resources. `include_content=true` also returns the current release's text files; normally use the ZIP resource instead.

### `describe_screensdesign_mcp()`

Return the connected scopes and authentication method, available tools, and high-level capabilities. Use only when access or the live surface is unclear; do not call before ordinary research.

## Apps

### `search_apps(...)`

Default 20, maximum 100. Paginate with `limit` and `offset`.

Important parameters:

- `app_name`: full or partial brand name.
- `smart_search`: semantic description of a concrete capability, audience, or problem. It controls relevance ordering and takes precedence over `sort`.
- `category`, `app_ids`, `exclude_app_ids`.
- `detected_patterns`, `excluded_patterns` using the enum in the live schema.
- `min/max_onboarding_steps`, `min/max_paywalls`, `min/max_quiz_questions`.
- `min/max_revenue`, `min/max_downloads`, `min/max_rating`.
- `sort`: `revenue`, `downloads`, `updated`, `released`, `rating`, or `name` when semantic search is inactive.

Do not put list intent such as “top subscription apps” into `smart_search`. Use `min_paywalls=1`, `sort="revenue"`, and other explicit filters instead.

### `similar_apps(app_id=None, app_ids=None, limit=20, offset=0)`

Find comparable apps for one source or as many as 10 sources. Maximum 50 results per source. In batch mode the server merges duplicates and records which source apps each result resembles.

### `app_detail(app_id=None, app_ids=None, include_store_screens=True, include_videos=True)`

Return detailed evidence for one app or a batch of up to 10. App identifiers may be ScreensDesign or App Store URLs, slugs, store IDs, bundles, or internal IDs. The response includes product/performance metadata, compact detected patterns, monthly revenue history, latest replay summary, chronological `flows`, optional replay summaries, and App Store screenshot IDs.

Use `flows[].id` in an exact `search_flows(flow_id=...)` follow-up. `flows[].type` distinguishes broad `main_flows` from granular `onboarding_sequence` steps.

## Recorded Screens And Flows

### `app_screens(app_id=None, app_ids=None, limit=50, offset=0)`

Browse a latest recorded experience in replay order for one app or up to 10. Maximum 50 screens per app per call. Batch results include independent pagination per app; continue with each `next_offset` when present. Use positions and timestamps to verify sequence.

### `search_screens(query, ..., limit=20, offset=0)`

Search isolated recorded screens by a natural-language UI or experience concept. Maximum 50. Scope with app inclusion/exclusion, category, paywall type, revenue, downloads, and rating filters. Search results do not contain neighboring screens and cannot prove sequence.

### `search_flows(query="", flow_id=None, ..., limit=20, offset=0)`

Provide exactly one of:

- `flow_id` to retrieve a known flow returned by `app_detail` or `search_flows`.
- A concise `query` describing a journey or stored flow name.

Maximum 50. Apply app, category, paywall, revenue, download, and rating filters early. For before/after questions, use screen discovery followed by `app_screens` instead.

### `screen_detail(screen_id=None, screen_ids=None, include_image=True)`

Return focused evidence for one screen or up to 10 screens. Includes app identity, compact structured description, image URL, exact replay-moment URL, and related flow references. `include_image` controls native image content blocks, not structured metadata.

### `find_similar_screens(screen_id=None, image=None, limit=20)`

Find visually similar recorded screens from exactly one source: a known `screen_id` or a base64 image object with `data` and `content_type`. Maximum 50. Screens belonging to the source app are excluded.

## App Store Creatives

### `search_store_screens(query="", app_smart_search="", screen_smart_search="", ..., limit=20, offset=0)`

Search promotional App Store product-page screenshots. Maximum 50.

- `query` matches app, developer, or category metadata.
- `app_smart_search` ranks by what an app does, who it serves, or the problem it solves. Follow the same ranking cautions as `search_apps.smart_search`.
- `screen_smart_search` ranks what one listing screenshot visibly shows or communicates: copy, UI, imagery, composition, style, or marketing message.
- Scope with app IDs, excluded app IDs, category, and revenue bounds.

Use `search_screens` for actual recorded in-app UI. Do not use either semantic field for rankings, and do not put non-visible app capabilities or sequence questions into `screen_smart_search`. When both semantic fields are supplied, app relevance is considered first and screenshot-content relevance second.

## Developers And Saved Collections

### `search_developers(query="", category=None, min_revenue=None, min_downloads=None, limit=20, offset=0)`

Search publishers and portfolios. Maximum 100. Each developer result includes authoritative internal app IDs for follow-up calls.

### `list_collections(include_app_collections=True, include_saved_groups=True)`

List the connected user's app collections and shared saved groups, including counts. This tool does not return their contents.

### `get_collection(collection_id, limit=20, offset=0)`

Browse latest-replay screens across the apps in one app collection. Maximum 50. Use a collection ID returned by `list_collections` and continue with `next_offset` when present.

## Error Recovery

- Read the tool error's corrective message and valid parameter example, fix the call once, and continue.
- Do not repeat the same invalid or already-successful call unchanged.
- When a record is unavailable, try one materially relevant alternative route and then report the limitation.
- HTTP 401 means authentication must be completed or refreshed. HTTP 429 means wait for the supplied retry period before trying again.
