# ScreensDesign MCP Connection

Hosted Streamable HTTP MCP server (production, stateless):

```text
https://api.screensdesign.com/v1/mcp
```

Server name convention: `screensdesign`. Scope: `mcp:read` (read-only; there are no write tools).

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

## API Key Fallback

For clients without remote MCP OAuth support, use a developer API key. The user creates one at:

```text
https://screensdesign.com/mcp/keys
```

Keys start with `sd_key_` and are sent as `Authorization: Bearer sd_key_...` (the header `X-ScreensDesign-Agent-Key: sd_key_...` also works). Never ask the user to paste a key into chat; keys belong in client config or environment variables.

Claude Code:

```bash
claude mcp add --transport http screensdesign "https://api.screensdesign.com/v1/mcp" --header "Authorization: Bearer <screensdesign-api-key>" --scope user
```

Codex (`config.toml`):

```toml
[mcp_servers.screensdesign]
url = "https://api.screensdesign.com/v1/mcp"
bearer_token_env_var = "SCREENSDESIGN_API_KEY"
```

Cursor (`mcp.json`):

```json
{
  "mcpServers": {
    "screensdesign": {
      "url": "https://api.screensdesign.com/v1/mcp",
      "headers": {
        "Authorization": "Bearer ${env:SCREENSDESIGN_API_KEY}"
      }
    }
  }
}
```

Generic MCP client:

```json
{
  "mcpServers": {
    "screensdesign": {
      "url": "https://api.screensdesign.com/v1/mcp",
      "headers": {
        "Authorization": "Bearer <screensdesign-api-key>"
      }
    }
  }
}
```

## Troubleshooting

- HTTP 401 with `{"detail": "..."}`: no or invalid credentials. Complete the OAuth browser login, or check that the `sd_key_` is active and unexpired. The 401 response's `WWW-Authenticate` header carries the OAuth resource-metadata URL for discovery.
- Tools not visible after adding the server: the client usually needs a new session or an MCP restart/refresh.
- The server is stateless; each request authenticates independently, so there is no session to resume after token expiry — the client re-runs OAuth automatically or keeps using the API key.
- Verify the connection by calling `describe_screensdesign_mcp`; it echoes the authenticated key prefix, user, organization, scopes, and auth method.
- Never print tokens, API keys, authorization codes, callback URLs, or refresh tokens in output.
