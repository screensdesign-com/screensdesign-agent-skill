# App Research Workflow

Use this workflow for app discovery, competitor discovery, revenue-banded markets, pasted URLs, app detail, developers, and categories.

## Tool Choice

- Use `resolve_app_link` first when the user pastes a ScreensDesign URL, App Store URL, replay PDF URL, slug, store id, or bundle. It returns app metadata plus `internal_refs` for follow-up calls.
- Use `list_research_apps` for research-grade discovery. It returns compact app candidates with App Store descriptions, AI-enhanced descriptions, classification, `public_links`, `internal_refs`, and a `replay_summary` with the latest video, onboarding step count, and paywall type.
- Use `search_apps` for a lighter app list when the research payload is unnecessary.
- Use `app_detail` after an app is selected. It returns full metadata, monthly `revenue_list`, a `reviews_sample`, replay videos, latest replay screens, and current store screenshots.
- Use `search_developers` for publisher/portfolio research and `list_categories` to discover valid category names with app counts.
- Use `describe_screensdesign_mcp` when unsure about the current tool surface.

## Revenue And Market Filters

For requests such as "apps doing 20k a month with replays":

- Use `min_revenue` and `max_revenue` (monthly USD estimates).
- For "around 20k", start with `min_revenue=15000` and `max_revenue=30000`.
- For "20k+", use `min_revenue=20000`.
- For smaller-app research, add an upper bound so results do not drift toward category leaders.
- `min_downloads`/`max_downloads` and `min_rating`/`max_rating` work the same way.
- Use `has_replays=true` when the user needs replay recordings, `has_store_screens=true` for App Store screenshots, and `has_pdf=true` (list_research_apps only) when a ready replay PDF matters.
- `sort` accepts `revenue` (default), `downloads`, `updated`, `released`, `rating`, and `name`.

Do not inspect local config files or credentials to discover hidden API options. Use `describe_screensdesign_mcp`, `describe_app_intelligence_schema`, and documented filters.

## App-To-Screen Drilldown

When app search identifies interesting apps:

1. Use `app_detail` on selected apps for context, revenue history, videos, and sample screens.
2. Use `app_screen_pdf` or `list_app_screen_pdfs` for the replay contact sheet; open the PDF for the full visual flow.
3. Use `search_screens` with `app_ids` to find specific replay screens (paywalls, quiz steps, settings) inside selected apps.
4. Use `search_store_screens` with `app_ids` to compare App Store marketing screenshots.
5. Use `search_app_intelligence` with `app_ids` when structured classification for the selected set matters.

Read `workflows/screen-research.md` before deep screen or PDF work.

## Output

Lead with the scope and result count. Include the filters used, especially category/revenue/replay constraints. Prefer compact tables for app comparisons with revenue, downloads, rating, and one-line positioning from `enhanced_description.one_liner`. Show `web_url` and `appstore_url` links; keep `internal_refs` ids out of user-facing text unless asked.

Useful next actions often include:

- open the replay PDF for the top apps
- search paywall or onboarding screens inside the selected apps
- compare App Store screenshots across the shortlist
- narrow with app intelligence filters such as buildability or niche status
