<a href="https://screensdesign.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/screensdesign-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/screensdesign-logo.svg">
    <img alt="ScreensDesign" src="assets/screensdesign-logo.svg" width="216" height="29">
  </picture>
</a>

# ScreensDesign Agent Skill

**Give your AI agent real app screens, complete flows, and market context to work from.**

Research competitors, compare onboarding and paywalls, explore App Store reviews, and find visual references with the [ScreensDesign MCP](https://screensdesign.com/mcp/). Bring the evidence into Claude Code, Codex, Cursor, and other agents that support skills and MCP.

[Website](https://screensdesign.com) · [Connect the MCP](https://screensdesign.com/mcp/) · [Browse on skills.sh](https://skills.sh/screensdesign-com/screensdesign-agent-skill) · [Releases](https://github.com/screensdesign-com/screensdesign-agent-skill/releases)

[![skills.sh installs](https://skills.sh/b/screensdesign-com/screensdesign-agent-skill)](https://skills.sh/screensdesign-com/screensdesign-agent-skill)

## Install

Run this from your project root:

```bash
npx skills@latest add screensdesign-com/screensdesign-agent-skill --skill screensdesign-data
```

Then [connect the ScreensDesign MCP](#connect-the-screensdesign-mcp). The skill provides research instructions; the MCP provides access to the data through your ScreensDesign account.

<details>
<summary>Agent-specific, global, and versioned installation</summary>

Install for specific agents without prompts:

```bash
npx skills@latest add screensdesign-com/screensdesign-agent-skill --skill screensdesign-data -a claude-code -a codex -a cursor -y
```

Install across your projects:

```bash
npx skills@latest add screensdesign-com/screensdesign-agent-skill --skill screensdesign-data -g
```

Install the exact **v1.0.9** release:

```bash
npx skills@latest add https://github.com/screensdesign-com/screensdesign-agent-skill/tree/v1.0.9/screensdesign-data
```

Update an installed copy:

```bash
npx skills@latest update screensdesign-data
```

</details>

## What the skill does

[`screensdesign-data`](screensdesign-data/SKILL.md) teaches your agent how to choose the right research tools, inspect the evidence, and return useful findings with source links.

| Research task | What you get |
| --- | --- |
| Discover apps and competitors | Apps matched by product, category, positioning, or recorded UI, with revenue and download estimates where available. |
| Study onboarding and paywalls | Recorded screens, chronological replays, and stored flows that show how a journey unfolds. |
| Find UI references | Relevant screens across apps, focused searches within an app, and visual matches to a reference image. |
| Explore the broader app market | Competitor discovery, public app listings, and App Store reviews for researching recurring complaints and positioning. |
| Research App Store creatives | Marketing screenshots searched separately from recorded in-app screens. |
| Continue saved research | Your saved app collections and developer portfolios brought into the conversation. |

The skill checks replay context before making claims about screen order and links findings to the supplied app, screen, or flow sources. It distinguishes observed UI from inference and treats revenue and downloads as performance signals, not proof of conversion.

## Try it

With the skill installed and the MCP connected, ask your agent:

> Compare onboarding in three high-revenue habit trackers. Show the recorded screens in order and where each paywall appears.

> Find apps similar to my sleep app idea. Compare their positioning and summarize recurring complaints in their public App Store reviews.

> Find paywalls that show an annual subscription as a price per day. Link to the actual screens.

> Find app screens visually similar to this screenshot. Explain which layout and navigation patterns are shared.

> Compare the App Store screenshot messaging of three meditation apps. Which benefits does each lead with?

> Open my saved app collection and compare the onboarding patterns across its apps.

## Connect the ScreensDesign MCP

Add this hosted endpoint to your MCP client and sign in with your ScreensDesign account:

```text
https://api.screensdesign.com/v1/mcp
```

MCP access is included with [ScreensDesign Pro](https://screensdesign.com/mcp/). See the [setup page](https://screensdesign.com/mcp/) for supported clients and access details.

<details>
<summary>Claude Code</summary>

```bash
claude mcp add --transport http screensdesign "https://api.screensdesign.com/v1/mcp" --scope user
claude mcp login screensdesign
```

You can also open `/mcp` inside Claude Code to check the connection and authenticate.

</details>

<details>
<summary>Codex</summary>

```bash
codex mcp add screensdesign --url 'https://api.screensdesign.com/v1/mcp'
codex mcp login screensdesign
```

</details>

<details>
<summary>Cursor</summary>

Add this server to your Cursor MCP configuration:

```json
{
  "mcpServers": {
    "screensdesign": {
      "url": "https://api.screensdesign.com/v1/mcp"
    }
  }
}
```

Complete the browser sign-in when prompted.

</details>

Authentication uses browser OAuth. If the tools do not appear after setup, refresh the MCP connection or start a new conversation. See [connection troubleshooting](screensdesign-data/references/connection.md) for more detail.

## How it works

The skill stays compact and loads focused guides for [app research](screensdesign-data/workflows/app-research.md), [market and review research](screensdesign-data/workflows/market-research.md), [screen and flow research](screensdesign-data/workflows/screen-research.md), [app intelligence](screensdesign-data/workflows/app-intelligence.md), and [saved collections](screensdesign-data/workflows/saved-research.md) as needed.

The [tool reference](screensdesign-data/references/tools.md) and [response field guide](screensdesign-data/references/response-fields.md) document the research interface. Live MCP schemas take precedence when a tool changes.

The current data-skill release is **1.0.9**. When connected, the agent checks its installed version once per conversation through `get_screensdesign_skill` to learn whether it is current or needs an update.

<details>
<summary>For maintainers: release process</summary>

Each release uses a semantic Git tag matching the version declared in `screensdesign-data/SKILL.md`. For the current release:

```bash
python3 scripts/build_release.py --write-manifest
python3 scripts/build_release.py --check --tag v1.0.9
```

The release manifest records immutable content and ZIP hashes. Pushing the matching tag validates the package and creates a GitHub Release with the ZIP and manifest. The hosted MCP vendors that exact package for authenticated clients to read or download through MCP resources.

</details>

## License

[MIT](LICENSE) © 2026 ScreensDesign. The ScreensDesign name and logo are brand assets; this license does not grant trademark rights.

---

Built by [ScreensDesign](https://screensdesign.com) — real app screens, recorded flows, and market intelligence for your next product decision.
