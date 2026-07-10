# Completion Follow-Ups

Use this workflow before ending a useful ScreensDesign research answer. Follow-ups must be adaptive, not a fixed checklist.

## Rule

Suggest 2-3 next actions only when they fit the user's goal, the evidence already gathered, and ScreensDesign's available tools. Each suggestion should feel like the obvious next research move from the current result, not a generic menu.

Do not always suggest the same things. Do not suggest PDFs, similar screens, or intelligence filters just because those tools exist. Choose based on what would materially improve the user's next decision.

When the user says yes, act immediately with the relevant MCP tools.

## Decide From Context

Before suggesting next actions, infer:

- **User goal:** app discovery, competitor teardown, onboarding/paywall inspiration, UI reference hunting, market sizing, or revisiting saved research.
- **Current artifact:** app list, selected app, replay screens, a replay PDF, store screenshots, intelligence-filtered set, saved items, or empty/weak results.
- **Missing evidence:** actual flow visuals, exact screen copy, cross-app pattern confirmation, marketing (store) counterpart, revenue context, or structured classification.
- **Available identifiers:** `internal_refs.app_id`, `latest_app_video_id`, `latest_pdf_id`, `screen_id`s, `pdf_id`s.

Then suggest the smallest high-leverage next step.

## Capability Map

Use these capabilities as ingredients, not as a static list:

- **App context:** `resolve_app_link`, `list_research_apps`, `search_apps`, `app_detail`, `search_developers`, `list_categories`.
- **Flow visuals:** `app_screen_pdf`, `list_app_screen_pdfs`, `screen_pdf_detail` -> open PDF -> `screen_detail` on labeled screen ids.
- **Screen evidence:** `search_screens` (text/semantic), `screen_detail`, `find_similar_screens`.
- **Marketing counterpart:** `search_store_screens`.
- **Structured narrowing:** `describe_app_intelligence_schema`, `search_app_intelligence` (patterns, scores, onboarding/paywall counts).
- **Saved research:** `list_collections`, `search_saved_research` (read-only).

## Adaptive Patterns

Use patterns like these, rewritten for the actual result:

### App List Found

- "Should I open the replay PDF for the top 2-3 apps so we can compare their full onboarding flows?"
- "Should I pull their paywall screens side by side to compare pricing presentation?"
- "Should I narrow this list with intelligence filters like buildability or detected quiz onboarding?"

### One App Selected

- "Should I open this app's replay PDF and walk the onboarding-to-paywall flow screen by screen?"
- "Should I find similar apps in the same revenue band to see whether this flow is common or differentiated?"
- "Should I compare its replay paywall against its App Store screenshots to see what they promise vs deliver?"

### Replay Screens Or PDF Reviewed

- "Should I pull `screen_detail` on the strongest screens for exact copy and UI components?"
- "Should I find visually similar screens across other apps to confirm the pattern?"
- "Should I check which other apps share this detected pattern with `search_app_intelligence`?"

### Store Screenshots Found

- "Should I compare these against the same apps' actual replay onboarding to spot the gap between marketing and product?"
- "Should I widen to the category's top-revenue apps for a fuller screenshot ladder comparison?"

### Intelligence Filter Results

- "Should I verify the detected patterns by opening replay PDFs for the top matches?"
- "Should I loosen the pattern filters or scores if this set is too thin?"

### Empty Or Weak Results

- "Should I broaden by removing revenue/category constraints?"
- "Should I switch `search_screens` to semantic mode for the concept instead of exact wording?"
- "Should I check `describe_app_intelligence_schema` for the correct enum values before refiltering?"

Do not suggest deeper drilldowns when there is not enough evidence yet, and do not suggest saving through MCP; saving is web-app only.

## Response Pattern

Use one concise line or short paragraph. Tie each action to why it matters:

```text
Smart next moves: 1. open the replay PDF for the top app to walk its full onboarding, 2. pull its paywall screens for exact pricing copy, 3. find similar apps with the same quiz pattern to confirm the trend.
```

For final answers, use natural language. Avoid repeating the same suggestions across different tasks.
