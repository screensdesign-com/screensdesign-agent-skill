# Saved Research Workflow

Use this workflow when the user refers to their existing ScreensDesign collections, saved groups, saved replay points, or saved App Store screens.

## Read-Only

The MCP server is read-only (`mcp:read`). You can read saved research but cannot create, update, or delete it. If the user asks to save something, say saving happens in the ScreensDesign web app and offer to prepare the findings (links, screen ids, timestamps) they can save there.

## Tool Choice

- Use `list_collections` for an overview: the user's app collections (with app counts) and the organization's saved groups (with saved replay point and saved store screen counts).
- Use `search_saved_research` with a `query` to find specific saved items. It searches saved group names, saved replay point descriptions, saved store screen descriptions, and the associated app names, and returns three lists: `groups`, `saved_points`, and `saved_store_screens`.
- Saved replay points include a `screen_url`, `timestamp`, `app_video_id`, and app summary; saved store screens include the `store_screen_id` and app summary.

## Reconnecting Saved Items To Live Data

- Use the app summary in a saved item with `app_detail`, `list_research_apps(app_ids=[...])`, or `app_screen_pdf` to refresh context around a saved finding.
- Use `search_screens(app_ids=[...])` around a saved point's timestamp to find the surrounding flow.
- Use `search_store_screens(app_ids=[...])` to see how a saved store screen fits the app's current screenshot ladder.

## Output

Summarize what is saved and where (collection or group names with counts). Show saved item descriptions, app names, and screen/image URLs. Keep internal ids for follow-up calls. If a search returns nothing, say so and offer a broader query or a live search of the same topic.
