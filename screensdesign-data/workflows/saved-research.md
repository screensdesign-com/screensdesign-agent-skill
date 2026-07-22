# Saved Research Workflow

Use this workflow for existing ScreensDesign app collections, saved groups, saved replay points, or saved store-screen records.

## Read Only

The MCP server can read saved research but cannot create, update, or delete it. If the user asks to save something, direct them to the ScreensDesign web app and offer a concise finding they can save there.

## Tool Choice

- Use `list_collections` for app collections and organization saved-group counts.
- Use `search_saved_research(query=...)` to find matching groups, replay points, saved store-screen records, and associated apps.

Saved replay points expose their description, timestamp, `app_video_id`, and app context. Saved store-screen items expose their description, `store_screen_id`, and app context. Hosted sanitization removes their visual URLs.

## Reconnect To Current Data

- Use `app_detail` or `list_research_apps(app_ids=[...])` to refresh app context.
- Use `app_screens` only when the saved point's `app_video_id` matches the app's current latest replay; paginate to the saved timestamp.
- If the saved point belongs to an older replay, explain that the hosted MCP cannot browse that recording directly.
- Use `search_store_screens(app_ids=[...])` for current store-screen metadata, not images.

## Output

Summarize what is saved and where, with collection/group names, counts, descriptions, timestamps, app names, and public app links. Do not promise saved screen or store-image URLs.
