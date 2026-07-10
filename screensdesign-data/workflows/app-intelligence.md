# App Intelligence Workflow

Use this workflow when the user filters apps by structured classification: target audience, niche status, buildability, habit potential, opportunity class, gamification, onboarding step counts, paywall counts, quiz length, or detected onboarding patterns.

## Tool Choice

- Use `search_app_intelligence` for all structured filtering. It combines app-context classification filters with all-in-one (AIO) replay analysis filters and the standard metric filters.
- Use `describe_app_intelligence_schema` first when unsure about field names, enum values, score fields, boolean fields, or pattern flags. Do not guess enum values.
- Results return the app summary plus an `intelligence` block: `app_context` classification and `all_in_one` with `detected_patterns`, `onboarding_sequence_summary`, `onboarding_radar_axes`, `main_flows`, `unique_onboarding`, and `what_to_learn_onboarding`.

## Filter Placement

- Put free text only in `query` (matches names, descriptions, and classification JSON text) or `aio_text` (matches replay-analysis JSON text, e.g. "personalization", "social proof", "streaks").
- Use typed arguments for known fields: `target_audiences`, `niche_status`, `app_types`, `category_refinements`, `tags`, `usage_frequency`, `habit_potential`, `time_to_value`, `opportunity_class`, `opportunity_lens`, `buildability`, `indie_buildability`, `network_effects`, `clone_risk`, `trust_burden`, `sensitive_domains`, plus booleans such as `is_original_product`, `is_known_brand`, `is_provider_portal`, `is_content_catalog`, `requires_real_world_infrastructure`.
- Use `app_context_filters={...}` for any other field listed by `describe_app_intelligence_schema`. Array filters must match all requested values by default; set `app_context_match_any=true` to match any value.
- Use score ranges for 0-100 style scores: `min_novelty_score`/`max_novelty_score`, `min_commodity_score`/`max_commodity_score`, `min_incumbent_score`/`max_incumbent_score`.

## Onboarding And Paywall Filters

- Use `detected_patterns` / `excluded_patterns` with AIO pattern flags such as `HasQuiz`, `SpecialOfferPaywall`, `HasSignToCommitScreen`, `HasFreeTrialSwitcher`, `HasRatingWarmupScreen`, or `HasBeforeAfterScreen`. The full list is in `references/tools.md`; the live list comes from `describe_app_intelligence_schema`.
- Use numeric ranges for flow shape: `min_onboarding_steps`/`max_onboarding_steps`, `min_paywalls`/`max_paywalls`, `min_quiz_questions`/`max_quiz_questions`.
- Use `has_gamification=true` for gamified onboarding; it is a text-based signal, not a strict flag.
- Use `aio_text` for concepts without a dedicated flag.

Example, "solo-buildable fitness apps with a long quiz onboarding and 2+ paywalls":

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

Verify enum values like `solo_buildable` against `describe_app_intelligence_schema` before sending.

## Intelligence-To-Screen Drilldown

After structured filtering finds apps:

1. Use `list_research_apps` with `app_ids` for public links, internal refs, and richer descriptions of the matched set.
2. Use `app_screen_pdf` on the strongest matches to see the actual onboarding/paywall flow the patterns describe.
3. Use `search_screens` with `app_ids` to pull the specific screens behind a detected pattern (e.g. the sign-to-commit screen).

## Output

Lead with the count and the structured filters used. For each app, pair the metric summary with the classification evidence that matched (detected patterns, onboarding step count, paywall count). Treat classifications and pattern flags as AI-derived signals, not ground truth; verify against replay screens or PDFs before strong claims.

Useful next actions often include:

- open replay PDFs for the top matches to verify the detected patterns
- pull the exact pattern screens with `search_screens`
- relax or tighten pattern/score filters when results are too thin or too broad
