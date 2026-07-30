# App Research Workflow

Use this workflow for app and competitor discovery, rankings, selected-app details, pasted app links, and publisher portfolios.

## Choose The First Call

- Known app, ScreensDesign URL, App Store URL, slug, store ID, or bundle: call `app_detail` directly.
- Named brand search: use `search_apps(app_name=...)`.
- Concrete capability, audience, job, product mechanic, or recorded UI behavior: use `search_apps(smart_search=...)`.
- Ranked or filtered market list: leave `smart_search` empty and use explicit filters plus `sort`.
- Alternatives to known apps: use `similar_apps`, batching up to 10 source IDs.
- Publisher portfolio: use `search_developers`, then reuse returned `app_ids`.

## Search Discipline

- Apply category, revenue, download, rating, detected-pattern, onboarding, quiz, and paywall filters in the tool call when relevant.
- Revenue and downloads are monthly estimates. For “around $20K”, a reasonable starting range is `min_revenue=15000`, `max_revenue=30000`; state the assumption.
- `smart_search` fuses app-description and recorded-screen relevance. Check app names, short descriptions, and `matched_screen_evidence` before treating results as relevant.
- If semantic results are clearly off-topic, make at most one materially different retry—for example, use an exact app name or remove an overly restrictive filter. Do not retry synonyms indefinitely.
- Paginate only when the user needs broader coverage or the first page is insufficient.

## Drill Down

After discovering candidates:

1. Call `app_detail` for only the selected apps; batch up to 10.
2. Use `app_screens(query=...)` for a particular recorded UI concept inside the selected apps.
3. Use `app_screens` without `query` when complete chronological replay coverage matters; use `search_screens` for a UI concept across apps that are not yet known.
4. Use `search_store_screens` for how the same apps market themselves on the App Store.
5. Use `search_flows(flow_id=...)` when `app_detail` exposes a specific flow worth opening.

## Output

Lead with the answer and scope. For comparisons, keep criteria consistent: positioning, estimated revenue/downloads, rating, release/update timing, observed patterns, and relevant flow evidence. Link app names to supplied ScreensDesign app URLs and label estimates and AI-derived intelligence appropriately.
