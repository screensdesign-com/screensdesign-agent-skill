# Completion Follow-Ups

Suggest 2-3 next actions only when they materially advance the user's goal. Tie each suggestion to evidence already gathered and capabilities the hosted MCP actually exposes.

## Capability Map

- App context: `resolve_app_link`, `list_research_apps`, `search_apps`, `app_detail`, `search_developers`.
- Ordered replay flow: `app_screens` with pagination.
- Semantic screen discovery: `search_screens`.
- Deeper text evidence: `screen_detail`.
- Visual neighbors: `find_similar_screens`.
- Store-screen metadata: `search_store_screens`.
- Structured narrowing: `describe_app_intelligence_schema`, `search_apps`.
- Saved research: `list_collections`, `search_saved_research`.

## Adaptive Patterns

### App List Found

- Inspect the latest replay flows for the top candidates with `app_screens`.
- Narrow by buildability, audience, scores, or verified pattern flags.
- Semantically search a relevant paywall or onboarding concept across the shortlist.

### One App Selected

- Paginate through its latest replay to reconstruct the onboarding-to-paywall sequence.
- Open `screen_detail` on important screens for exact OCR and UI components.
- Find visual neighbors for a strong screen reference.

### Replay Screens Reviewed

- Compare the same concept across other apps with `search_screens`.
- Verify a detected pattern against the actual ordered flow.
- Compare metrics and classifications for apps using similar patterns.

### Store-Screen Metadata Found

- Compare screenshot counts, order, and dimensions across the shortlist.
- Open public app links separately if visual store-page inspection is needed.

### Empty Or Weak Results

- Broaden the semantic query or remove market/category constraints.
- Check live intelligence enums and pattern flags before refiltering.
- Switch from cross-app search to one app's ordered latest replay when sequence matters.

Do not suggest unsupported exact-OCR search, downloadable flows, replay videos, full-size image assets, or saving through MCP.
