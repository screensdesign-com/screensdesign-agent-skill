# App Intelligence Workflow

Use this workflow for target audience, niche status, buildability, habit potential, opportunity class, risk, score, onboarding-step, paywall, quiz-length, or detected-pattern filters.

## Construct Valid Filters

- Use `search_apps` for structured intelligence filtering.
- Call `describe_app_intelligence_schema` when enum values or pattern flags are uncertain.
- Send only named `search_apps` parameters. Do not send arbitrary schema fields through `app_context_filters`.
- Use `app_context_match_any=true` only when requested array filters may match any value; the default requires all requested array values.
- Use the named novelty, commodity, and incumbent score ranges for 0-100 score filtering.
- Use `detected_patterns` and `excluded_patterns` with live pattern flags.
- Use the named onboarding-step, paywall, and quiz-question ranges for flow shape.
- Use `aio_text` for heuristic concepts without a dedicated filter, including gamification, personalization, social proof, streaks, or commitment. Do not send `has_gamification`.

Put broad product/classification text in `query` and replay-analysis concepts in `aio_text`.

Example, "solo-buildable fitness apps with a long quiz and at least two paywalls":

```json
{
  "category": "Health & Fitness",
  "indie_buildability": "solo_buildable",
  "detected_patterns": ["HasQuiz"],
  "min_quiz_questions": 10,
  "min_paywalls": 2,
  "sort": "revenue",
  "limit": 20
}
```

Verify enum and pattern values against the live schema before sending.

## Verify Intelligence With Replay Evidence

1. Use `list_research_apps(app_ids=[...])` for richer descriptions and public links.
2. Use `app_screens` on the strongest matches to inspect the latest replay in order.
3. Use `search_screens(app_ids=[...])` for semantic discovery of the screens behind a detected concept.
4. Use `screen_detail` on important screen ids for complete text evidence.

## Output

Lead with the result count and structured filters used. Pair metrics with the classification or flow evidence that matched. Treat AI fields as signals, not ground truth, and verify consequential claims against replay screens.
