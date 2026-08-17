# ScreensDesign MCP Tools

Hosted Streamable HTTP MCP server:

```text
https://api.screensdesign.com/v1/mcp
```

All research tools are read-only. Revenue and download filters are estimated monthly USD and installs. `offset` is zero-based. Live input schemas are authoritative and include allowed enum values.

## Account, Capability, And Skill

### `get_screensdesign_skill(installed_version=None, include_content=False)`

Check whether the loaded `screensdesign-data` skill is current. Pass the release declared near the top of `SKILL.md` once per conversation. The response reports `current`, `update_available`, `incompatible`, `ahead`, or `unreported`, plus the latest release, compatibility, update command, hashes, and MCP resources. `include_content=true` also returns the current release's text files; normally use the ZIP resource instead.

### `describe_screensdesign_mcp()`

Return the connected scopes and authentication method, available tools, and high-level capabilities. Use only when access or the live surface is unclear; do not call before ordinary research.

### `get_me()`

Return the connected user's email and optional display name together with the credential-bound organization's public identifier, name, membership role, and ScreensDesign plan. Use when the user asks which ScreensDesign account or organization is connected.

## Apps

### `search_apps(...)`

Default 20, maximum 100. Paginate with `limit` and `offset`.

Important parameters:

- `app_name`: full or partial brand name.
- `smart_search`: semantic description of a concrete capability, audience, product mechanic, problem, or recorded UI behavior. It fuses app-description and recorded-screen relevance, controls result ordering, and takes precedence over `sort`.
- `category`, `app_ids`, `exclude_app_ids`.
- `detected_patterns`, `excluded_patterns` using the enum in the live schema.
- `min/max_onboarding_steps`, `min/max_paywalls`, `min/max_quiz_questions`.
- `min/max_revenue`, `min/max_downloads`, `min/max_rating`.
- `sort`: `revenue`, `downloads`, `updated`, `released`, `rating`, or `name` when semantic search is inactive.

Do not put list intent such as “top subscription apps” into `smart_search`. Use `min_paywalls=1`, `sort="revenue"`, and other explicit filters instead.

Smart-search results can include `match_sources` and up to two compact `matched_screen_evidence` records with exact replay links.

### `similar_apps(app_id=None, app_ids=None, limit=20, offset=0)`

Find comparable apps for one source or as many as 10 sources. Maximum 50 results per source. In batch mode the server merges duplicates and records which source apps each result resembles.

### `app_detail(app_id=None, app_ids=None, include_store_screens=True, include_videos=True)`

Return detailed evidence for one app or a batch of up to 10. App identifiers may be ScreensDesign or App Store URLs, slugs, store IDs, bundles, or internal IDs. The response includes product/performance metadata, compact detected patterns, monthly revenue history, latest replay summary, chronological `flows`, optional replay summaries, and App Store screenshot IDs.

Use `flows[].id` in an exact `search_flows(flow_id=...)` follow-up. `flows[].type` distinguishes broad `main_flows` from granular `onboarding_sequence` steps.

## Broader Market Apps And Reviews

### `search_market_apps(smart_search, ...)`

Search apps across the broader App Store market. `smart_search` is required and should describe an app purpose, audience, problem, or product concept. Semantic relevance always determines ordering; other parameters narrow the candidate set.

Default 20, maximum 100. Important optional parameters:

- `app_name`, `category`, and `revenue_month` in `YYYY-MM` format.
- `min/max_revenue`, `min/max_downloads`, and `min/max_rating`.
- Inclusive `released_from` and `released_until` boundaries in `YYYY-MM-DD` format.
- `library_status`: `all`, `in_library`, or `outside_library`.
- `screenshots_per_app`: 1–5 App Store listing screenshots per result.
- `limit` and `offset` for pagination.

Results include a short and medium description, icon, release date, metrics, public App Store URL, listing screenshots, and `is_in_screensdesign_library`. Use library tools for recorded UI evidence only when that field is true and a ScreensDesign app reference is supplied.

### `similar_market_apps(app, focus="", ...)`

Find semantic broader-market neighbors for an App Store URL, numeric App Store identifier, or app name. Add `focus` only when one comparison angle should influence similarity. It accepts the same category, month, metric, rating, release-date, library-status, pagination, and screenshot controls as `search_market_apps`.

Results remain ordered by semantic similarity. The response includes the resolved source app, matching results, and their library availability.

### `market_app_detail(app, country="us", force_refresh=false)`

Return one broader-market app with its short and medium descriptions, full public App Store description, icon, category, metrics, release date, public links, library availability, and App Store listing screenshots. Set `force_refresh=true` only when the user explicitly needs a new listing-screenshot check.

### `app_store_reviews(app, countries="us", reviews_per_country=500, ratings=None, locale="en-US", force_refresh=false)`

Return the latest public App Store reviews for an App Store URL, numeric App Store identifier, or app name, including apps outside the ScreensDesign library.

- `countries` accepts one or up to 10 two-letter country codes and defaults to `us`.
- `reviews_per_country` accepts 1–500.
- `ratings` accepts one rating, a list, or a range such as `1-3`.
- `force_refresh=true` is only for an explicit request for newly posted or freshly checked reviews.

The tool does not accept a review date range. Each returned review contains only its publication date, 1–5 rating, and text. Fewer reviews than requested is a valid result and may mean that the app, country, or rating selection has fewer available reviews.

## Recorded Screens And Flows

### `app_screens(app_id=None, app_ids=None, query="", limit=50, offset=0)`

Browse a latest recorded experience for one app or up to 10. Maximum 50 screens per app per call, with independent pagination per app.

- Leave `query` empty to browse chronologically.
- Provide a concrete visible-UI `query` to rank matching screens independently inside each app's latest replay. The returned `position` and `timestamp` remain the true replay values even though matches are relevance-ranked.
- Set `limit` to the number of matching screens needed per app. For example, `app_screens(app_ids=["340","512"], query="free trial toggle paywall", limit=1)` returns one focused candidate from each app.
- Continue with each `next_offset` only when broader coverage is actually needed.

### `search_screens(query, ..., max_per_app=2, limit=20, offset=0)`

Search isolated screens from each app's latest replay by a natural-language visible UI or experience concept. Maximum 50. Scope with app inclusion/exclusion, category, paywall type, revenue, downloads, and rating filters. `max_per_app` accepts 1–10 and prevents one app from dominating broad results.

Results are nearest semantic candidates, not calibrated relevance guarantees. Check every returned `description`; when it does not actually support the requested UI concept, do not use it as evidence and report no strong match when appropriate. Search results do not contain neighboring screens.

### `search_flows(query="", flow_id=None, ..., limit=20, offset=0)`

Provide exactly one of:

- `flow_id` to retrieve a known flow returned by `app_detail` or `search_flows`.
- A concise `query` describing a journey or stored flow name.

Maximum 50. Apply app, category, paywall, revenue, download, and rating filters early. For before/after questions, use screen discovery followed by `app_screens` instead.

### `screen_detail(screen_id=None, screen_ids=None, neighbor_count=1, include_image=True)`

Return focused evidence for one screen or up to 10 screens. Includes app identity, compact structured description, image URL, exact replay-moment URL, related flow references, and immediately adjacent screens from the same replay. `neighbor_count` accepts 0–3 screens on each side. `include_image` controls native image content blocks for the focused screens, not structured metadata.

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
