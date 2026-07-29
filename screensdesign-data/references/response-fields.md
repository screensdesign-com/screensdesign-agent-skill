# ScreensDesign Response Fields

The MCP returns compact public research objects, not raw database rows. Optional fields may be `null`, empty, or absent. Live output schemas override this reference.

## Shared App Objects

### App summary

Used by `search_apps`, `similar_apps`, and `app_detail`:

- `id`, `slug`, `store_id`, `name`.
- `short_description`: generated concise copy, or the first 100 words of the App Store description.
- `developer`: compact `id` and `name`.
- `category_primary`.
- `revenue`, `downloads`: estimated monthly values.
- `rating_value`, `released`, `updated`.
- `latest_app_video_id`.
- `appstore_url`, `screensdesign_app_url`.
- `intelligence` on search/similarity results:
  - `app_context.niche_segments` when available.
  - `all_in_one.onboarding_sequence_summary`, `onboarding_radar_axes`, and `unique_onboarding` when available.

### App reference

Screen, flow, and store-screen tools return app identity separately or under `app`/`apps`:

- `id`, `name`, `short_description`.
- `developer`, `category_primary`, `release_date`.
- `rating_value`, `revenue`, `installs`, optional `paywall_type`.
- `screensdesign_app_url`, `appstore_url`.

MCP App UI metadata may carry app icons separately from the model-facing structured JSON.

## App Search And Detail

`search_apps` returns `app_name`, `smart_search`, `total`, `limit`, `offset`, applied `filters`, and `results`.

Single-source `similar_apps` returns `source`, `total`, `limit`, `offset`, and `results`. Batch mode returns `sources`, `requested_app_ids`, merged `results`, `limit_per_source`, and per-source pagination; merged results include `similar_to_app_ids`.

`app_detail` extends an app summary with:

- `latest_ai_patterns.patterns`: detected public replay patterns only.
- `revenue_list`: monthly revenue history.
- `latest_replay`: onboarding step count, paywall type, screen count, and screen ordering.
- `flows`: chronological flow entries with `id`, `type`, `title`, `description`, `time_from`, and `time_to`.
- Optional `videos`: `id`, onboarding step count, and paywall type.
- Optional `store_screens`: current App Store screenshot IDs.

A batched app-detail response contains `requested_app_ids`, `count`, and `results`.

## Recorded Screens

A compact recorded screen can contain:

- `id`: handle for `screen_detail` or visual similarity.
- `app_id` where the surrounding result does not already carry app identity.
- `position` and `timestamp` where replay ordering matters.
- `description`: compact structured content such as `exhaustive_description`, `screen_type`, `funnel_stage`, `visible_text`, and—on focused detail—`primary_user_goal`.
- `image_url`.
- `screen_appearance_timestamp_url`: exact replay moment.
- `screensdesign_screen_deep_link_url`: specific-screen page.
- `flows`: related flow references when available.

`app_screens` returns a single `app`, `latest_replay`, `pagination`, and `screens`, or batch `apps`, `results_by_app`, and `pagination_by_app`.

`search_screens`, `find_similar_screens`, and `get_collection` normally return a top-level `apps` list plus compact `results`, so identity is not duplicated on every screen.

`screen_detail` returns one detailed screen or batched `requested_screen_ids`, `count`, and `results`.

## Flows

`search_flows` returns top-level `apps` and `results`. Each result can contain:

- `id`, `app_video_id`, `name`, `description`.
- `time_from`, `time_to` in replay seconds.
- `screensdesign_flow_deep_link_url`.
- Chronological `screens` with public image and deep-link evidence.

Use `app_detail.flows[].id` or an earlier flow-search result for exact retrieval.

## App Store Screens

`search_store_screens` returns `total`, pagination, top-level app references, and screenshot results. A result can contain:

- `id`.
- `screensdesign_store_screen_deep_link_url`.
- `width`, `height`, `order`, `created_at`.

The MCP's model-facing JSON may omit visual asset URLs while a compatible host receives them through UI metadata.

## Developers

`search_developers` returns `query`, `total`, pagination, and results. A developer result can contain:

- `id`, `name`, `slug`, `store_id`.
- `total_apps`, `revenue`, `downloads`, `rating_count`.
- `app_ids`: authoritative internal app identifiers owned by the developer.

## Collections

`list_collections` returns:

- `app_collections`: `id`, `name`, `app_count`, `screen_count`, `created_at`.
- `saved_groups`: group metadata and saved-item counts when requested.

`get_collection` returns `collection`, `total`, `limit`, `offset`, `next_offset`, top-level `apps`, and screen `results` in the same compact shape as screen search.

## Skill Release

`get_screensdesign_skill` returns:

- Installed and latest versions plus `status`.
- `minimum_supported_version` and `mcp_contract_version`.
- Immutable release tag, dates, repository/release URLs, and content/archive hashes.
- ZIP, manifest, and `SKILL.md` MCP resource URIs.
- Install and update commands.
- Optional `files` only when `include_content=true`.

## Errors And Access

- Authentication failures return HTTP 401 with OAuth discovery information.
- Rate limits return HTTP 429 and a retry hint.
- Invalid identifiers and arguments return corrective tool errors. Reuse identifiers from successful results.
- Results are already filtered for the current account. Do not infer withheld visual content or promise fields absent from the public contract.
