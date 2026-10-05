# Finding Cursor transcripts: 10Web relay prompts & post-migration damage

**Purpose (legal bundle):** Show that **Cursor (Desktop)** drafted **specific instructions** for Daniel to send to **10Web** (what to do / what **not** to do), including **pre-migration** and **during failed migration**, and that **after ~2 weeks** when a migration appeared complete, **staging/site damage** was documented in Cursor — supporting **disregard of agreed constraints** (preserve WP, no AI Builder, `tcstaging`, custom HTML/JS, etc.).

**This is not** the 10Web chatbot log (see `docs/10WEB-SUPPORT-TRANSCRIPT-TIMELINE.md`).  
**This is** Daniel ↔ **Cursor Desktop** threads (and any Cloud runs that quoted relay text).

---

## Timeline anchors (search by content, not folder name)

| Window | What Cursor threads likely contain |
|--------|-------------------------------------|
| **Pre-migration (~7/24–7/25)** | Checklists for Charlie/10Web; LiteSpeed off; **do not** update WP/plugins; site size; **preserve** custom code; DNS later not now. |
| **During failure (~7/25–8/3)** | Relay prompts to Marta/support; reconnect/disconnect; **“start over”**; anger at 8 days no help; **do not use AI Builder**. |
| **After “success” (~8/4–8/18+)** | **Destruction** discovery: overlays, crop, EXPLORE split, wrong site/fake site, compare to `tcstaging`; prompts telling 10Web **stop**, **restore**, **human migration**. |

Governance engine / ISI folders are **post-crash** — **July–August 10Web relay** threads are usually under an **older workspace hash** or **global history**.

---

## Part 1 — Cursor Desktop UI (try first)

1. Open **Cursor Desktop** (ISI OK as starting point).
2. **Ctrl + Shift + P** → **Chat: Show History** / **Previous Chats**.
3. Search **one phrase at a time** (history search, **not** bottom agent box):

### Relay / instruction prompts (high value for “disregard” claim)

- `paste this to 10web`
- `send to Charlie`
- `tell 10web`
- `tell Charlie`
- `message for support`
- `what to tell Marta`
- `do not use AI Builder`
- `do not publish`
- `fake site`
- `preserve`
- `wp-content`
- `Manager plugin`
- `disconnected`
- `start over`
- `375660`
- `Marta`
- `escalate`

### Damage / aftermath

- `destruction`
- `destroyed`
- `irreversible`
- `crop`
- `EXPLORE`
- `overlay`
- `tc-explore`
- `Additional CSS`
- `Jul 24`
- `restore`
- `rollback`
- `when migration finished`
- `two weeks`

### Staging vs live

- `tcstaging`
- `tcstaging.truth-collective.com`
- `truth-collective.com`
- `Hostinger`
- `LiteSpeed`

4. Open each hit → scroll **top to bottom** → **Export Transcript** →  
   `J:\Legal-Exhibits\…\cursor-exports\YYYY-MM-DD__CURSOR-RELAY-10web__short-title.md`

5. Label files for counsel:

   - `__PRE__` — pre-migration checklist / prompts to 10Web  
   - `__DURING__` — migration failure / support relay  
   - `__AFTER-DAMAGE__` — post-migration discovery + corrective prompts  

---

## Part 2 — Forensic search on `User` copy (when UI shows only Sept+)

**Prerequisite:** Full copy of  
`C:\Users\dreid\AppData\Roaming\Cursor\User`  
→ e.g. `J:\DLegal_Exhibits2026_10_05_cursor_user_FORENSIC_COPY`  
(Cursor **fully exited** before copy.)

### A. List workspaces (July–August `state.vscdb` dates)

See PowerShell in `docs/CURSOR-CHAT-PRESERVATION-10WEB-CRASH.md` (Windows section).

### B. String search on **copy only** (finds text Notepad may miss)

PowerShell:

```powershell
$copy = "J:\DLegal_Exhibits2026_10_05_cursor_user_FORENSIC_COPY"
$terms = @(
  "10web","Charlie","Marta","375660","AI Builder","fake site",
  "tcstaging","disconnected","tell 10web","paste","preserve",
  "destruction","EXPLORE","do not publish","Manager plugin"
)
Get-ChildItem $copy -Recurse -Filter "state.vscdb" -ErrorAction SilentlyContinue | ForEach-Object {
  foreach ($t in $terms) {
    $hits = Select-String -Path $_.FullName -Pattern $t -SimpleMatch -Encoding byte -ErrorAction SilentlyContinue 2>$null
    if ($LASTEXITCODE -eq 0 -or $hits) {
      Write-Output "$($_.DirectoryName)  MATCH: $t  Modified: $($_.LastWriteTime)"
    }
  }
}
```

If `Select-String -Encoding byte` fails on your PS version, use **findstr** on each `state.vscdb`:

```cmd
findstr /i /m "10web tcstaging AI Builder fake site Marta 375660" "J:\...\workspaceStorage\*\state.vscdb"
```

When a **hash folder** hits, open the **same workspace** in Desktop (path from `workspace.json`) and use **History** again, or give that `.vscdb` file to a forensic vendor (SQLite export).

### C. Optional: `globalStorage\state.vscdb`

Same searches — some chats index globally.

---

## Part 3 — Local Cloud Agent cache (supplement only)

```
C:\Users\dreid\.cursor\agents\
```

Folders named by branch (e.g. `10web-migration-a537`) are **Oct 2026** runbooks — **not** July relay. Still scan **other** agent folders for **Aug 2026** dates; export any JSON/transcript to `J:\…\cursor-exports\`.

---

## Part 4 — Pair with 10Web exhibits (“disregard” narrative)

For each **Cursor Export** that contains a **prompt block** you sent to 10Web:

1. Save Cursor `.md` as **Exhibit C-__**  
2. Save matching **10Web** reply (from your full chat export) as **Exhibit T-__** with **same date**  
3. One-line **comparison** in `EXHIBIT-INDEX.txt`:  
   `Cursor instructed X / 10Web did Y`

Examples from your 10Web log that Cursor likely warned about **before** Aug 3:

- **Do not** use **AI Builder** / fake site → user had to say explicitly **Aug 3**.  
- **Preserve** HTML/JS / structure → bot promised, builder path contradicted.  
- **Migrate `tcstaging` WP only** → disconnect / reconnect / start over.  
- **DNS / primary domain** only after preview test.

Cursor transcripts prove **you were instructed**; 10Web transcripts prove **what they said/did**.

---

## Part 5 — If nothing from July–August appears

1. **`J:\Laptop Backup`** — search `AppData\Roaming\Cursor\User` from **July–Aug 2026**.  
2. **Previous Versions** on `%APPDATA%\Cursor`.  
3. **Cursor support** — request Desktop export **2026-07-01 through 2026-08-31**, keywords: 10Web, tcstaging, migration relay.  
4. **Your sent messages** — if you **pasted Cursor text into 10Web chat**, those blocks may exist **only** in 10Web log (you already have many) — Cursor side still helps if you **edited** prompts before sending (version in Desktop).

---

## Part 6 — Do not harm ISI

Read-only: History, Export Transcript, copy `User` folder.  
Do **not** continue old agent runs or save edited `state.vscdb`.

---

*Not legal advice. Pair with attorney on exhibit numbering and privilege.*
