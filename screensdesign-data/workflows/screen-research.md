# Screen Research Workflow

Use this workflow for replay screen research (onboarding flows, paywalls, quizzes, in-app UI), replay PDF contact sheets, similar-screen lookups, and App Store screenshot research.

## Replay Screens Vs Store Screens

- Replay screens (`search_screens`, `screen_detail`, `find_similar_screens`, PDFs) come from full screen recordings of real app sessions: onboarding, paywalls, and main-app UI, with OCR text and AI screen descriptions.
- Store screens (`search_store_screens`) are the app's current App Store marketing screenshots.

Pick by intent: "how does the paywall actually look/flow" is replay; "how do they market on the App Store" is store.

## Replay Screen Search

- Use `search_screens` with `search_mode="text"` (default) for OCR text, exact wording, app/developer names, or paywall type wording.
- Use `search_mode="semantic"` for concepts such as "streak celebration screen" or "paywall with lifetime offer"; it ranks by pgvector embeddings and returns `match_score`/`match_text`. Keep `vector_scope="description"` unless you have a reason to change it.
- Scope with `app_id`/`app_ids`/`exclude_app_ids`, `category`, `paywall_type`, and revenue/downloads/rating bounds.
- If `semantic_error` is set in the response, the server fell back to text mode; say so if it changes result quality.
- Use `screen_detail(screen_id)` for one screen: full OCR text and annotations, `screen_type`, `funnel_stage`, `visible_text`, `ui_components`, and asset URLs.
- Use `find_similar_screens(screen_id)` for visually similar screens across apps; `mode="pgvector_image"` is a true visual match, `mode="same_app_fallback"` means no image vector existed and results are same-app screens in timestamp order.

## Replay PDF Contact Sheets

PDFs show watermarked replay screens in timestamp order, each tile labeled with its `screen_id`.

1. Use `app_screen_pdf(app_id)` to generate or fetch the PDF for an app's latest replay (or pass `app_video_id` for a specific recording). Use `list_app_screen_pdfs` / `screen_pdf_detail(pdf_id)` for already-persisted PDFs; `list_research_apps` results expose `internal_refs.latest_pdf_id`.
2. The tool returns a PDF ResourceLink plus a JSON manifest. Open the PDF first to read the visual flow end to end.
3. Use the `screen_id` labels (also in `screen_index` with page, position, and timestamp) and call `screen_detail(screen_id)` on interesting tiles for OCR, metadata, and raw assets.
4. Check `pdf.truncated`; if true, the recording had more screens than `max_screens`. Regenerate with a higher `max_screens` or `refresh=true` if completeness matters.

Give the user the PDF URL (`agent_document.url` or `pdf.url`) as the shareable artifact.

## App Store Screenshots

- Use `search_store_screens` with `query` (matches app/developer/category metadata, not screenshot content), `app_ids`, `category`, and revenue bounds.
- Results return `image_url`/`thumbnail_url` plus `order`, so you can compare full screenshot ladders across apps.

## Output

Lead with the count and scope. For flow research, describe the sequence with timestamps and screen types, and cite OCR/visible text as evidence. Show screen image URLs and PDF links; keep `screen_id`s available for follow-up but out of user-facing prose unless asked.

Useful next actions often include:

- open `screen_detail` on the strongest screens for exact copy and UI components
- find visually similar screens across other apps
- pull the replay PDF for a competitor to compare full flows
- compare replay paywalls against the same apps' store screenshots
