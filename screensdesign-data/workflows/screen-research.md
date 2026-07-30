# Screen And Flow Research Workflow

Use this workflow for recorded screens, onboarding/paywall sequence, stored flows, visual similarity, attached references, and App Store creatives.

## Pick The Evidence Surface

- Recorded in-app UI concept across unknown apps: `search_screens`.
- Specific UI concept inside known apps: `app_screens(query=...)`.
- Complete latest replay in chronological order: `app_screens` without `query`.
- Stored journey or exact known flow: `search_flows`.
- One or up to 10 known screen records: `screen_detail`.
- Visual alternatives to a known or attached screen: `find_similar_screens`.
- App Store product-page marketing screenshots: `search_store_screens`.

## Verify Sequence

`search_screens` searches only latest replays and diversifies results across apps. It still returns nearest semantic candidates, so first reject results whose descriptions do not support the requested visible UI. For “before”, “after”, “immediately following”, or similar claims:

1. Search for the most distinctive target screen.
2. Validate its returned description before collecting app IDs.
3. Use `screen_detail(neighbor_count=1)` when immediate adjacency can answer the question.
4. Otherwise retrieve each needed event inside those apps with focused `app_screens` queries. Use an unfiltered replay page only when focused results are insufficient.
5. Locate both target events in the same replay and compare returned position and timestamp evidence.
6. Make the sequence claim only when both events and their order are present.

For example, to find apps that request notifications before a paywall, search for the permission/warmup screen first and reject off-topic descriptions. If the paywall is an immediate neighbor, `screen_detail` supplies that local evidence. Otherwise use focused `app_screens` queries to retrieve both events inside each candidate app and compare true positions or timestamps.

## Flow Search

- Use a concise journey concept such as `onboarding`, `subscription`, `checkout`, or `notification permission`.
- Use `flow_id` to retrieve an exact flow returned by `app_detail` or a prior search.
- Do not use flow search as a temporal query engine. Verify before/after relationships with `app_screens`.

## Visual Similarity

- For a ScreensDesign source, pass `screen_id`.
- For an external image through public MCP, pass the supported base64 `image` object.
- If the current host exposes an attachment index or handle, use only the live host-specific parameter instead of copying base64 into model text.
- Supply exactly one source. Results exclude the source app.

## App Store Creatives

- Use `query` to narrow by app, publisher, or category metadata.
- Use `app_smart_search` for the app's capability, audience, or problem, such as `AI math tutor`.
- Use `screen_smart_search` for visible screenshot content: headline copy, displayed UI, device composition, illustration/photography, visual style, or marketing message.
- When both semantic fields are supplied, app relevance is considered first and screenshot-content relevance second.
- Do not use either semantic field for rankings. Do not infer recorded product behavior from marketing screenshots alone.

## Output

Separate observation from interpretation. Cite visible text and compact descriptions, link each app/screen/flow to the exact URL supplied with that object, and use replay-moment links for timing claims. Do not print raw positions, IDs, or guessed links.

Never infer visible details from `visual_details_locked`. Use only the timestamp and replay URL supplied for the same screen; omit timing when exact evidence is unavailable.
