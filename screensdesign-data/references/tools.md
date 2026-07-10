# ScreensDesign MCP Tools

Hosted Streamable HTTP MCP server (stateless):

```text
https://api.screensdesign.com/v1/mcp
```

All tools are read-only. Defaults: `limit=20` (most list tools cap at 50, some at 100), `offset=0`. `category` parameters accept a name or list of names matched case-insensitively against primary and secondary categories (use `list_categories` for valid names). `app_ids`/`exclude_app_ids` accept internal app ids, slugs, store ids, or bundles. Revenue and download filters are monthly estimates in USD / installs.

## Discovery And Schema

### describe_screensdesign_mcp()

Describe the current tool surface, transport, PDF/intelligence usage notes, and the authenticated account (key prefix, user, organization, scopes, auth method).

### describe_app_intelligence_schema()

List filterable app-context fields (string/array/score/boolean fields with enum values) from `vsearch_app_context_v3` and all-in-one fields, pattern flags, and numeric summary filters from `latest_av_ai_aio`. Call before constructing nontrivial `search_app_intelligence` filters.

## Apps

### search_apps(query="", category=None, min_revenue=None, max_revenue=None, min_downloads=None, max_downloads=None, min_rating=None, max_rating=None, has_replays=None, has_store_screens=None, sort="revenue", limit=20, offset=0)

Lightweight app search. `query` matches name, shortname, description, developer, and category text. `sort`: `revenue`, `downloads`, `updated`, `released`, `rating`, `name`. Limit max 100.

### list_research_apps(query="", category=None, app_ids=None, exclude_app_ids=None, min_revenue=None, max_revenue=None, min_downloads=None, max_downloads=None, min_rating=None, max_rating=None, has_replays=None, has_store_screens=None, has_pdf=None, include_description=True, sort="revenue", limit=20, offset=0)

Research-grade app list. `query` additionally matches the app-context and all-in-one JSON text. Results include `public_links`, `internal_refs` (including `latest_app_video_id` and `latest_pdf_id`), `enhanced_description`, `classification`, and `replay_summary`. `has_pdf=true` requires a ready replay PDF. Limit max 50.

### resolve_app_link(app_link, include_description=True, limit=5)

Resolve a pasted ScreensDesign app URL, App Store URL, replay PDF URL, slug, store id, bundle, or internal app id to app research metadata and internal refs. Call first when the user pastes a URL. Limit max 10.

### app_detail(app_id, include_screens=True, include_store_screens=True, include_videos=True, screen_limit=12)

One app: full metadata and description, `latest_ai_patterns` (raw all-in-one analysis), monthly `revenue_list`, `reviews_sample` (5), up to 10 replay `videos` (with `onboarding_step_count`, `paywall_type`, preview URLs), latest replay `screens`, and current `store_screens`. `screen_limit` max 50. `app_id` accepts any app identifier.

## App Intelligence

### search_app_intelligence(query="", category=None, app_ids=None, exclude_app_ids=None, app_context_filters=None, app_context_match_any=False, ..., sort="revenue", limit=20, offset=0)

Structured app search. Beyond the standard metric filters (`min/max_revenue`, `min/max_downloads`, `min/max_rating`, `has_replays`, `has_store_screens`), it accepts:

- Typed app-context filters (string or list): `target_audiences`, `niche_status`, `app_types`, `category_refinements`, `tags`, `usage_frequency`, `habit_potential`, `time_to_value`, `opportunity_class`, `opportunity_lens`, `buildability`, `indie_buildability`, `network_effects`, `clone_risk`, `trust_burden`, `sensitive_domains`.
- Boolean app-context filters: `requires_real_world_infrastructure`, `is_known_brand`, `is_provider_portal`, `is_transactional_brand_app`, `is_content_catalog`, `is_original_product`.
- Score ranges (0-100): `min_novelty_score`/`max_novelty_score`, `min_commodity_score`/`max_commodity_score`, `min_incumbent_score`/`max_incumbent_score`.
- `app_context_filters` dict for any other field from `describe_app_intelligence_schema`. Array filters match all values by default; `app_context_match_any=true` matches any.
- All-in-one filters: `detected_patterns` / `excluded_patterns` (pattern flags below), `aio_text` (text search across the replay-analysis JSON), `has_gamification`, `min/max_onboarding_steps`, `min/max_paywalls`, `min/max_quiz_questions`.

Pattern flags (verify the live list with `describe_app_intelligence_schema`):

`HasQuiz`, `HasTimer`, `HasVideo`, `HasAppleBadges`, `ShowsStarRating`, `HasDiscountOffer`, `HasLifetimeOffer`, `HasPressMentions`, `HasTrialTimeline`, `HasATTWarmupScreen`, `HasFeatureCarousel`, `HasMascotCharacter`, `RequestsHealthData`, `HasUserTestimonials`, `SpecialOfferPaywall`, `HasBeforeAfterScreen`, `HasFeatureHighlights`, `HasFreeTrialSwitcher`, `ShowsPricePerWeekDay`, `HasRatingWarmupScreen`, `HasSignToCommitScreen`, `AmountOfPlansDisplayed`, `HasReviewsTestimonials`, `HasReinforcementScreens`, `HasBuildingYourPlanScreen`, `HasFeatureComparisonTable`, `HasPrivacyDedicatedScreen`, `HasSignUpDuringOnboarding`, `HasNotificationWarmupScreen`, `HasHowDidYouHearAboutUsScreen`, `HasPostSubscriptionWelcomeScreen`.

## Replay Screens

### search_screens(query="", search_mode="text", app_id=None, app_ids=None, exclude_app_ids=None, category=None, paywall_type=None, min_revenue=None, max_revenue=None, min_downloads=None, max_downloads=None, min_rating=None, max_rating=None, vector_scope="description", limit=20, offset=0)

Search replay screens. `search_mode="text"` matches OCR text plus app/developer/paywall metadata. `search_mode="semantic"` embeds the query and ranks by pgvector similarity, returning `match_score` and `match_text`; on embedding failure it falls back to text mode and sets `semantic_error`. Limit max 50.

### screen_detail(screen_id)

One replay screen: full `ocr_text` and `ocr_annotations`, `vsearch_data`, `screen_description`, `screen_type`, `funnel_stage`, `visible_text`, `ui_components`, `domain_signals`, optional `ai_onboarding`/`ai_paywall`, app context, and image URLs.

### find_similar_screens(screen_id, limit=20, pool_size=None)

Visually similar replay screens from an AppVideoScreen id. `mode="pgvector_image"` when an image vector exists; otherwise `mode="same_app_fallback"` returns same-app screens in timestamp order. Limit max 50.

## Replay PDF Contact Sheets

PDF tools return a PDF ResourceLink plus a JSON manifest as tool content. Open the PDF for the visual flow; each tile is labeled with its `screen_id`.

### app_screen_pdf(app_id, app_video_id=None, screens_per_page=12, max_screens=240, refresh=False)

Generate or fetch the PDF for an app's replay (latest video by default). `refresh=true` regenerates.

### list_app_screen_pdfs(app_id=None, app_ids=None, exclude_app_ids=None, status="ready", include_screen_index=False, limit=20, offset=0)

List persisted replay PDFs. Limit max 50.

### screen_pdf_detail(pdf_id, include_screen_index=True)

Fetch one persisted PDF record by id with its `screen_index` manifest.

### Resource: screensdesign://app-screen-pdfs/{pdf_id}

JSON manifest resource for one replay PDF (PDF URL, app/app_video ids, page count, screen_id index).

## App Store Screenshots

### search_store_screens(query="", app_id=None, app_ids=None, exclude_app_ids=None, category=None, min_revenue=None, max_revenue=None, limit=20, offset=0)

Search current App Store screenshots. `query` matches app/developer/category metadata, not screenshot content. Limit max 50.

## Developers, Categories, Saved Research

### search_developers(query="", category=None, min_revenue=None, min_downloads=None, limit=20, offset=0)

Search developers/publishers with portfolio and revenue metadata, sorted by revenue. Limit max 100.

### list_categories(query="", limit=100, offset=0)

List app categories with app counts. Use for valid `category` filter names.

### list_collections(include_app_collections=True, include_saved_groups=True)

The authenticated user's app collections and the organization's saved groups with counts.

### search_saved_research(query="", limit=20, offset=0)

Search the organization's saved groups, saved replay points, and saved App Store screens by name/description/app name. Returns `groups`, `saved_points`, and `saved_store_screens`.
