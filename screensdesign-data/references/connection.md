# ScreensDesign MCP Connection

Hosted Streamable HTTP MCP server (production, stateless):

```text
https://api.screensdesign.com/v1/mcp
```

Server name convention: `screensdesign`. Scope: `mcp:read` (read-only; there are no write tools).

Install the versioned companion skill release:

```bash
npx -y skills add https://github.com/screensdesign-com/screensdesign-agent-skill/tree/v1.0.8/screensdesign-data
```

Update an existing installation:

```bash
npx skills update screensdesign-data
```

When connected, call `get_screensdesign_skill` with the release declared near the top of the installed `SKILL.md` to verify whether an update is available. The server can compare a reported version but cannot inspect the client's local filesystem.

## OAuth (Preferred)

OAuth 2.1 browser login is the preferred connection method. Clients that support MCP OAuth only need the URL: protected-resource discovery, authorization-server metadata, and dynamic client registration are automatic. When the client prompts, the user approves ScreensDesign in the browser.

Claude Code:

```bash
claude mcp add --transport http screensdesign "https://api.screensdesign.com/v1/mcp" --scope user
claude mcp login screensdesign
```

Codex (`config.toml`):

```toml
[mcp_servers.screensdesign]
url = "https://api.screensdesign.com/v1/mcp"
```

Then `codex mcp login screensdesign`.

Cursor (`mcp.json`):

```json
{
  "mcpServers": {
    "screensdesign": {
      "url": "https://api.screensdesign.com/v1/mcp"
    }
  }
}
```

## Troubleshooting

- HTTP 401 with `{"detail": "..."}`: complete the OAuth browser login. The 401 response's `WWW-Authenticate` header carries the OAuth resource-metadata URL for discovery.
- Tools not visible after adding the server: the client usually needs a new session or an MCP restart/refresh.
- The server is stateless; each request authenticates independently, so there is no session to resume after token expiry — the client re-runs OAuth automatically.
- Verify which user and organization are connected by calling `get_me`. Use `describe_screensdesign_mcp` for authenticated scopes, auth method, access, and capabilities.
- HTTP 429 means the current request window is exhausted; wait for the retry period supplied by the server.
- Never print OAuth tokens, authorization codes, callback URLs, or refresh tokens in output.
