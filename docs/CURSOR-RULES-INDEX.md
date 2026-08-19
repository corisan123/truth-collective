# Cursor project rules index (written “page rules”)

These files in `.cursor/rules/` **always apply** to Cloud and IDE agents in this repo. They are the durable rules Daniel asked for — not chat memory.

| Rule file | Locks in |
|-----------|----------|
| `truth-collective.mdc` | Staging, locked classes, voice, CSS ownership, image sizes |
| `lead-worker-no-drift.mdc` | Lead vs worker; secrets/new-agent investment; no lane theft |
| `command-os.mdc` | Obey and update `docs/COMMAND-OS.md` Current assignment |
| `rest-and-secrets.mdc` | Auth email user, backup-before-write, no secrets in git |
| `parallel-by-default.mdc` | Many hands; parallel across blocks; never same family |
| `staging-not-live-not-cdn.mdc` | Staging only; not live; not LiteSpeed/Cloudflare cache rituals |

**Skills (`.cursor/skills/`):** `cursor-lead` · `cursor-block-a-worker` · `claude-specialist`

**Board:** `docs/COMMAND-OS.md`  
**Paste dashboard:** `docs/SWARM-LAUNCH-PACK.md`  
**Charter:** `docs/COMMAND-CHARTER-2026-08-19.md`  
**Prompts:** `docs/AI-PLATFORM-RULES-AND-PROMPTS.md`

To change behavior: edit a rule file + COMMAND OS in the same PR. Do not “decide in chat” against rules.
