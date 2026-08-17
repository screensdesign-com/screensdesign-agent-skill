# Completion Follow-Ups

Use this workflow before ending a useful ScreensDesign research answer. Suggest no more than two or three next actions, and only when they materially advance the user's goal.

## Decide From The Evidence

Infer:

- The goal: discovery, comparison, teardown, onboarding/paywall inspiration, visual references, portfolio research, or saved collections.
- The current evidence: app list, app detail, isolated screens, ordered replay, exact flow, store creatives, or weak/empty results.
- What remains missing: chronology, exact screen evidence, cross-app confirmation, marketing comparison, or performance context.
- Which identifiers and public links are already available.

Then suggest the smallest useful next step.

## Useful Transitions

- App list → inspect selected apps with `app_detail`, then open ordered replays with `app_screens`.
- One app → find alternatives with `similar_apps`, or compare its recorded UI with its App Store creatives.
- Broader-market list → inspect selected listings with `market_app_detail`, analyze feedback with `app_store_reviews`, or verify recorded UI for results marked as available in the ScreensDesign library.
- Review themes → compare the same theme across selected competitors or open recorded ScreensDesign evidence when the relevant apps are available in the library.
- Isolated screens → inspect immediate replay neighbors with `screen_detail`, verify broader sequence with `app_screens`, or expand visually with `find_similar_screens`.
- Flow result → retrieve the exact flow by ID or compare the same journey across shortlisted apps.
- Detected pattern → verify it against recorded screens before turning it into a recommendation.
- App Store creatives → compare their promise with recorded product behavior.
- Empty results → remove one meaningful constraint or switch between exact name, capability search, screen search, and app search as appropriate.

Do not suggest a capability merely because it exists. Do not repeatedly recommend the same transition, and do not offer write actions through the read-only MCP.

## Style

Use one natural sentence tied to the result, for example:

> Next, I can compare the top two apps' ordered onboarding replays or pull their paywall screens side by side for exact copy and layout evidence.

If the user already asked for a complete analysis and the available evidence supports it, finish the work instead of asking what to do next.
