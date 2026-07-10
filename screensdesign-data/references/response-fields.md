# ScreensDesign Response Fields

The MCP tools return compact agent-facing objects, not raw database rows. Use `describe_screensdesign_mcp` and `describe_app_intelligence_schema` for the live contract.

Most list responses share a common envelope: `query`, `total`, `limit`, `offset`, `results`. Missing values can be `null`, empty arrays, or absent.

## App Summary

Returned by `search_apps` results and nested `app` objects on screens and saved items:

- `id`, `slug`, `store_id`, `bundle`, `name`, `shortname`
- `developer.id`, `developer.name`, `developer.slug`, `developer.store_id`
- `category_primary`, `categories`
- `revenue`, `downloads`: monthly estimates.
- `rating_value`, `released`, `updated`, `rev_install_rate`, `featured`
- `latest_app_video_id`: latest replay recording id.
- `icon_url`, `appstore_url`, `web_url`: `web_url` is the public ScreensDesign app page.
- With descriptions enabled: `description`, `showcase_article`, `review_count`.

## App Research Summary

Returned by `list_research_apps` and `resolve_app_link` results. Everything in the app summary plus:

- `public_links.app`, `public_links.app_store`, `public_links.latest_replay_pdf`: show these to users.
- `internal_refs.app_id`, `internal_refs.app_slug`, `internal_refs.store_id`, `internal_refs.bundle`, `internal_refs.latest_app_video_id`, `internal_refs.latest_pdf_id`: use internally for follow-up calls; do not show raw ids unless asked.
- `enhanced_description`: `short_description`, `one_liner`, `primary_use_case`, `primary_use_cases`, `job_to_be_done`, `why_interesting`, `why_unique`, `app_metadata_description`, `app_metadata_labels`.
- `classification`: `target_audiences`, `audience_specificity`, `niche_status`, `app_types`, `category_refinements`, `category_refinement_main`, `tags`, `usage_frequency`, `habit_potential`, `time_to_value`, `opportunity_class`, `opportunity_lens`, `buildability`, `indie_buildability`, `is_original_product`, `is_provider_portal`.
- `replay_summary.latest_video`: `id`, `recording_date`, `duration_seconds`, `onboarding_step_count`, `paywall_type`.
- `replay_summary.onboarding_sequence_summary`, `replay_summary.detected_patterns`.

`list_research_apps` responses also include `search_url` (public search page) and a `usage` block with follow-up tool hints. `resolve_app_link` responses include `input`, `resolved`, `candidate_identifiers`, and `usage`.

## App Detail

`app_detail` returns the app summary with description plus:

- `latest_ai_patterns`: raw latest all-in-one replay analysis JSON (can be large).
- `revenue_list`: recent monthly revenue rows.
- `reviews_sample`: up to 5 App Store reviews.
- `videos[]`: `id`, `duration_seconds`, `recording_date`, `onboarding_step_count`, `paywall_type`, `preview_url`, `bunny_preview_mp4_url`.
- `screens[]`: replay screen summaries (below).
- `store_screens[]`: store screen summaries (below).

## App Intelligence Results

`search_app_intelligence` results are app summaries plus `intelligence`:

- `intelligence.app_context`: classification fields such as `one_liner`, `target_audiences`, `niche_status`, `job_to_be_done`, `opportunity_lens`, `buildability`, `indie_buildability`, `novelty_score`, `commodity_score`, `incumbent_score`, `clone_risk`, `trust_burden`, and related fields from the app-context schema.
- `intelligence.all_in_one.detected_patterns`: onboarding/paywall pattern flags detected in the latest replay.
- `intelligence.all_in_one.onboarding_sequence_summary`: includes `total_steps`, `paywalls`, `quiz_questions`.
- `intelligence.all_in_one.onboarding_radar_axes[]`: `name`, `score`, `rationale`.
- `intelligence.all_in_one.main_flows`, `unique_onboarding`, `what_to_learn_onboarding`.

The response echoes applied `filters`.

## Replay Screen Summary

Returned by `search_screens`, `find_similar_screens`, and `app_detail.screens`:

- `id`: the `screen_id` used by `screen_detail` and PDF manifests.
- `timestamp`: seconds into the replay recording.
- `app_video_id`, `app` (app summary)
- `screen_url`, `preview_url`, `original_url`: image assets.
- `labels`, `tags`
- `ocr_excerpt`: first 500 characters of OCR text.
- `description`: AI screen description.
- `match_score`, `match_text`: present on semantic/similarity results.

`search_screens` responses also include `search_mode` and `semantic_error` (set when semantic search fell back to text). `find_similar_screens` responses include `source` (the query screen) and `mode` (`pgvector_image` or `same_app_fallback`).

## Replay Screen Detail

`screen_detail` adds:

- `ocr_text` (full), `ocr_annotations`
- `vsearch_data`: raw screen analysis JSON including `embedding_text`.
- `screen_description`, `screen_embedding_text`, `screen_description_json`
- `screen_type`, `funnel_stage`, `visible_text`, `ui_components`, `domain_signals`
- `ai_onboarding`, `ai_paywall`: present when the screen belongs to an onboarding or paywall flow.

## Replay PDF Payload

`app_screen_pdf`, `list_app_screen_pdfs` results, and `screen_pdf_detail` return:

- `id` (pdf_id), `status` (`ready` when usable), `created`, `error`
- `mcp_resource_uri`: `screensdesign://app-screen-pdfs/{pdf_id}`.
- `app`: `id`, `name`, `slug`, `store_id`, `bundle`.
- `app_video`: `id`, `recording_date`, `duration_seconds`, `paywall_type`.
- `pdf`: `url`, `filename`, `mime_type`, `size_bytes`, `page_count`, `screens_per_page`, `generated_screen_count`, `total_screen_count`, `truncated`, `screen_order` (`timestamp_ascending_then_id`).
- `agent_document`: the ResourceLink source; `agent_document.url` is the shareable PDF link.
- `screen_index[]` (when requested): `screen_id`, `page`, `position`, `timestamp`, `app_video_id`, `image_field`, `image_url`.

In MCP clients, `app_screen_pdf` and `screen_pdf_detail` return two content items: a `resource_link` to the PDF and a text JSON manifest.

## Store Screen Summary

Returned by `search_store_screens` and `app_detail.store_screens`:

- `id`, `app` (app summary)
- `image_url`, `thumbnail_url`, `width`, `height`
- `order`: position in the App Store screenshot ladder.
- `created_at`

## Developers And Categories

Developer results: `id`, `slug`, `store_id`, `name`, `total_apps`, `published_apps`, `revenue`, `downloads`, `rating_count`, `hq_country`, `url`, `category`, `top_apps`.

Category results: `id`, `name`, `app_count`.

## Saved Research

`list_collections`:

- `app_collections[]`: `id`, `name`, `app_count`, `created_at`.
- `saved_groups[]`: `id`, `name`, `saved_point_count`, `saved_store_screen_count`, `created_at`.

`search_saved_research`:

- `groups[]`: `id`, `name`, `created_at`, `updated_at`.
- `saved_points[]`: `id`, `description`, `timestamp`, `screen_url`, `app_video_id`, `app`, `created_at`.
- `saved_store_screens[]`: `id`, `description`, `store_screen_id`, `app`, `created_at`.

## Errors

Authentication failures return HTTP 401 with `{"detail": "..."}` and a `WWW-Authenticate` header pointing at the OAuth resource metadata; tell the user to complete the browser login or configure an `sd_key_` fallback. Not-found lookups (bad `app_id`, `screen_id`, `pdf_id`) raise tool errors; verify identifiers from earlier results before retrying.

Do not promise unsupported raw database fields. If the user needs data not listed here, say the current agent surface does not return it and point to the public `web_url` pages for inspection.
