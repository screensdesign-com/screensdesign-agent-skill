# Broader Market And Review Research

Use this workflow for app ideas, broad competitor discovery, positioning, revenue research, release-date research, apps outside the ScreensDesign library, and public App Store review analysis.

## Choose The Evidence Surface

- Recorded interface, onboarding, paywall, or flow evidence: prefer `search_apps`, `app_detail`, `app_screens`, `search_screens`, and `search_flows`.
- Broader app-market discovery: use `search_market_apps`.
- Semantic neighbors of a known market app: use `similar_market_apps`.
- Full public listing copy and listing screenshots for one market app: use `market_app_detail`.
- Public customer feedback for one specific app: use `app_store_reviews`.

Broader-market apps can support app-idea, competitor, positioning, metric, release-date, review, and App Store listing research. They support recorded visual or product-flow claims only when `is_in_screensdesign_library` is true and a ScreensDesign app reference is returned.

## Broader-Market Discovery

1. Write a concrete `smart_search` describing the purpose, audience, problem, or product concept. It is required.
2. Add only relevant category, metric month, revenue, download, rating, release-date, and library-status filters.
3. Keep the returned semantic-relevance order. Do not request or imply revenue, download, rating, or alphabetical sorting.
4. Check names and medium descriptions before selecting candidates. Make at most one materially different retry when results are clearly off-topic.
5. Use `market_app_detail` for selected listings or `similar_market_apps` for semantic neighbors.
6. For results available in the ScreensDesign library, use their supplied ScreensDesign references with library tools when recorded UI evidence would improve the answer.

Treat returned App Store screenshots as listing creatives. Do not describe them as recorded app screens or infer in-app sequence and behavior from them.

## Public Review Research

1. Resolve one specific app by App Store URL, numeric App Store identifier, or app name.
2. Use the US by default. Request other countries only when geography matters.
3. Request only the number of reviews needed, up to 500 per country. Apply a rating selection only when it helps answer the question.
4. Set `force_refresh=true` only when the user explicitly asks for newly posted, freshly checked, or current reviews.
5. Do not request a date range; the tool returns the latest available review evidence.
6. Treat each review as one customer's report. Group genuinely repeated themes, distinguish recurring feedback from isolated comments, and preserve meaningful disagreement.
7. Do not infer prevalence, causation, or the experience of all users from a limited sample. Fewer reviews than requested is valid and must not be presented as a tool failure.

Use the returned date, rating, and text as evidence. Keep internal handles and tool mechanics out of the user-facing answer.

## Output

State whether findings come from recorded ScreensDesign evidence, App Store listing creatives, public reviews, or market metadata. Link supplied public app and App Store URLs. Label revenue and downloads as estimates, and make review-based recommendations proportional to the breadth and consistency of the returned feedback.
