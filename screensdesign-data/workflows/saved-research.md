# Saved Collection Workflow

Use this workflow when the user refers to their ScreensDesign app collections or shared saved groups.

## Read-Only Workflow

1. Call `list_collections` to see the connected user's app collections and shared group counts.
2. For an app collection, pass its returned ID to `get_collection`.
3. Continue with `next_offset` only when more collection screens are needed.
4. Reuse app and screen identifiers from collection results for `app_detail`, `app_screens`, `screen_detail`, or similarity research.

`get_collection` currently browses screens from app collections. A listed shared group does not imply that a public tool exists to inspect every saved item inside it.

The MCP is read-only. If the user asks to save, rename, pin, or delete research, explain that those actions happen in the ScreensDesign website.

## Output

Use collection/group names and counts. Link returned apps and screens through their supplied public URLs. Keep collection, app, and screen IDs as internal follow-up handles unless debugging was requested.
