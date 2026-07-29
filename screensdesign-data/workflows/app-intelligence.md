# App Pattern Filtering Workflow

Use this workflow for app discovery based on detected onboarding/paywall patterns or replay-shape counts.

## Available Filters

`search_apps` supports:

- `detected_patterns` and `excluded_patterns`; use only names from the live enum.
- `min/max_onboarding_steps`.
- `min/max_paywalls`.
- `min/max_quiz_questions`.
- Category, revenue, download, rating, app inclusion/exclusion, and sort filters.

Examples of live pattern names can include `HasQuiz`, `HasTrialTimeline`, `HasDiscountOffer`, `SpecialOfferPaywall`, `HasFreeTrialSwitcher`, `HasRatingWarmupScreen`, `HasSignToCommitScreen`, `HasBeforeAfterScreen`, `HasNotificationWarmupScreen`, and `HasPostSubscriptionWelcomeScreen`. Treat the tool schema as authoritative because this enum can evolve.

## Workflow

1. Translate only explicit or strongly implied constraints into filters.
2. Keep `smart_search` for a concrete app capability or audience, not the onboarding pattern itself when a structured pattern filter exists.
3. Sort explicitly when the user asks for top revenue, downloads, rating, newest, or recently updated apps.
4. Treat matching patterns as AI-derived signals.
5. Verify important claims against `app_screens`, `search_screens`, or an exact `search_flows` result before presenting them as observed behavior.

Example, “high-revenue fitness apps with quiz onboarding and at least one paywall”:

```json
{
  "category": "Health & Fitness",
  "detected_patterns": ["HasQuiz"],
  "min_paywalls": 1,
  "sort": "revenue",
  "limit": 20
}
```

## Output

State the applied filters and distinguish detected signals from visually verified evidence. Do not expose raw pattern payloads when a human explanation is clearer.
