# Preserving Cursor chats from the 10Web / site-damage period

**Goal:** Find and save **before**, **during**, and **after** conversations with Cursor related to the failed 10Web migration and the live-site damage (~July–August 2026), for ticket **#375660**, insurance, and future recovery work.

**Important finding (2026-10-05):** For repo `truth-collective`, Cursor Cloud only retains **three** agent runs. The **oldest is 2026-08-19** (“Truth collective content rebuild”). There is **no cloud transcript** in this account for the July crash window. The damaging session was almost certainly a **Desktop (local) Cursor chat** tied to your WordPress workspace, not a Cloud Agent on GitHub.

---

## Timeline (from repo evidence — not a legal record)

Use this to label exports **Before / During / After** when you find chats.

| Phase | Approx. window | What happened (repo/docs) |
|-------|----------------|---------------------------|
| **Before** | Through early Jul 2026 | Live site in progress; **Computers** page fully built (Rank Math ~90, animations, images) per `STAGING-RECOVERY-HANDOFF.md`. |
| **During (damage)** | Jul 2026 (esp. around **Jul 24** restore) | Migration Brief: a prior AI **converted overlay HTML to CSS** without understanding existing code; ~six weeks lost. Handoff: Jul 24-era restore + stacked `tc-explore*` / STAGING PATCH CSS; `10web_tmp` cleanup; 10WEB Manager still active. |
| **10Web parallel track** | Jul–Aug 2026 | 10Web hosting/migration and ticket **#375660** (RCA/compensation). Vercel/10Web **samples** used as visual reference only (`vercel-and-10web-comparison.pdf`). **Do not confuse** sample PDFs with the Hostinger live HTML/CSS failure. |
| **After (recovery)** | From **2026-08-08** handoff onward | `STAGING-RECOVERY-HANDOFF.md`, REST hub rebuilds, cloud agents from **2026-08-19** on. |

---

## Part 1 — Cloud Agent chats (already in Cursor cloud)

These are **after** the July crash, but save them anyway for a complete record.

| Label | Date (UTC) | Name | URL |
|-------|------------|------|-----|
| After | 2026-08-19 | Truth collective content rebuild | https://cursor.com/agents/bc-badd5954-984d-412a-8c1c-80a985692480 |
| After | 2026-08-26 | Homepage robots meta injection | https://cursor.com/agents/bc-87234e27-1251-4700-9db0-c37e19a60626 |
| After | 2026-10-05 | 10web migration (this runbook work) | https://cursor.com/agents/bc-16f364f0-f650-4deb-a735-e07176aba537 |

**How to save safely**

1. Open each URL while logged in as Daniel.
2. Scroll the full thread (Cloud UI is the source of truth).
3. **Redacted JSON mirrors** (no raw secrets) live in `diagnostics/cursor-chat-archive/cloud/*.transcript.redacted.json` after you merge the preservation PR.
4. **Note:** Desktop **Export Transcript** does **not** work for Cloud Agent chats (Cursor shows a message to that effect). Use the web UI + JSON archive above, or ask Cursor support for a full export if you need tool-call detail.

---

## Part 2 — Desktop Cursor chats (where the July session likely lives)

### Step A — Search chat history in the app

1. On the **same machine** you used for WordPress work in July 2026, open **Cursor**.
2. Open **Chat / Agent history** (history picker for past chats).
3. Search keywords (one at a time):

   `10web`, `10Web`, `tenweb`, `migration`, `overlay`, `tc-explore`, `Additional CSS`, `Jul 24`, `restore`, `Hostinger`, `truth-collective`, `Computers`, `HTML to CSS`, `Customizer`

4. Open each matching chat. Check the **date** in the thread or file timestamps (Step B).

### Step B — Export each chat (safe local backup)

For **Desktop / local Agent chats** (not Cloud):

1. Open the chat tab.
2. **Right-click the chat tab** → **Export Transcript** (saves `.md`),  
   **or** use the **`⋯` menu** on the chat editor title bar → **Export Transcript**.

**Limits (Cursor, 2026):** Export Transcript is mainly **visible text**. It may **omit** collapsed tool calls, terminal I/O, and full reasoning blocks. For legal/RCA you may still want **Time Machine / disk backup** of Cursor’s data directory (Step C).

3. Save exports with a fixed naming scheme:

   ```
   YYYY-MM-DD__phase-BEFORE|DURING|AFTER__short-title.md
   ```

4. Store copies in **two places**: e.g. `truth-collective/diagnostics/cursor-chat-archive/desktop/` (private repo or local only) and **Google Drive** (same folder you use for WP backups per Migration Brief).

**Do not commit** exports that contain Application Passwords, Hostinger credentials, or API keys. Redact before git push.

### Step C — Backup Cursor’s local database (best “full” recovery)

Chat history is stored in SQLite (`state.vscdb`) under workspace storage.

| OS | Typical Cursor user data |
|----|---------------------------|
| **macOS** | `~/Library/Application Support/Cursor/User/workspaceStorage/` (each subfolder has `state.vscdb`) |
| **Windows** | `%APPDATA%\\Cursor\\User\\workspaceStorage\\` |
| **Linux** | `~/.config/Cursor/User/workspaceStorage/` |

**Safe procedure**

1. **Quit Cursor completely.**
2. Copy the entire `Cursor/User/` folder (or at least `workspaceStorage/` + `globalStorage/`) to an external drive or zip dated `2026-10-05-cursor-user-backup.zip`.
3. Do **not** overwrite your only copy of the live folder; **copy**, do not move.
4. Optional: use a local tool to search all `state.vscdb` files for `10web`, `tc-explore`, `migration` (community tools: **cursor-history**, **cursor-chat-export** — verify compatibility with your Cursor version; forum reports some tools break on 3.x).

### Step D — Time Machine / prior backups

If Time Machine (or similar) ran on the Mac used for Cursor in **July–August 2026**, restore **only** the Cursor `User` folder from a date **before** any Cursor upgrade that might have migrated DB format. Compare exports from Step B with DB backup from Step C.

---

## Part 3 — Non-Cursor evidence (same incident folder)

Bundle these with chat exports for 10Web ticket **#375660**:

| Source | Location |
|--------|----------|
| Recovery handoff | `STAGING-RECOVERY-HANDOFF.md` |
| CSS inventory | `diagnostics/css-inventory-2026-08-08.md` |
| Computers page notes | `diagnostics/computers-page-2026-08-08.md` |
| Page HTML before REST edits | `diagnostics/backups/page-*-2026-08-*.html` |
| 10Web ticket | Hostinger/10Web portal **#375660** emails and attachments |
| Hostinger backups | hPanel backup logs around **Jul 24–28, 2026** |

---

## Part 4 — Suggested folder layout (Daniel local + optional private git)

```
cursor-chat-archive/
  README.txt                 # index of what each file is
  desktop/
    2026-07-??__DURING__10web-migration.md
    2026-07-24__AFTER__jul24-restore-discussion.md
  cloud/
    (redacted JSON from repo diagnostics)
  email/
    10web-ticket-375660.pdf
  backups/
    2026-10-05-cursor-user-backup.zip   # never push to public GitHub
```

---

## Part 5 — If chats are missing

1. Check **another computer** or **older Cursor profile** if you switched machines during cancer treatment / travel.
2. Check **GitHub** only for **after** chats: PR/agent links in PR bodies (e.g. PR #2 agent `bc-b360733d-fbaa-412a-8c1c-80a985692480`) — different bcId from current repo list; open https://cursor.com/agents/bc-b360733d-fbaa-412a-8c1c-80a985692480 if still on your account.
3. Contact **Cursor support** with bcIds and dates; ask whether Desktop chats from Jul 2026 are recoverable from their side (Privacy Mode / retention may apply).
4. Contact **10Web** for **their** migration logs for the same dates (complements Cursor exports).

---

## What Cursor Cloud Agent already archived in this repo

See `diagnostics/cursor-chat-archive/cloud/README.md` and redacted JSON files. Update this section when you add Desktop `.md` exports to `diagnostics/cursor-chat-archive/desktop/` (recommended: **private** repo or local only).
