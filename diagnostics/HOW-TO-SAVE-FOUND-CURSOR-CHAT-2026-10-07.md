# How to save the found 10Web Cursor conversation without corrupting it

**For:** Daniel Reid, after locating the July–August 10Web Cursor thread.  
**Date:** 7 October 2026.  
**Goal:** copies for counsel / ticket `#375660`. Do **not** change the original chat.

This is a technical checklist, not legal advice.

---

## Golden rules (these are what actually corrupt chats)

Do **not**:

- Send a new message in that thread
- Click **Continue**, **Run**, **Agent**, or **Apply**
- Delete the chat, “clear history,” or rename workspace folders
- Open `state.vscdb` in a DB editor on the **live** Cursor folder
- Move (cut) the Cursor `User` folder; only **copy**
- Push the raw transcript to public GitHub (it can contain passwords, app passwords, Hostinger notes)

Safe: open, scroll, export, screenshot, copy the URL, copy folders **after Cursor is fully quit**.

**If you already asked that old thread for a summary** (pre-state / during / 10Web directives / post destruction): that turn is useful. **Export now** so the summary is in the file. Then **stop**. Do not ask it to fix WordPress. Paste **only the summary** into this Sep 19 Cloud Agent. Details: `diagnostics/JULY-CURSOR-SUMMARY-INGEST-2026-10-07.md`.

---

## Step 0 — Decide which kind you found

Look at the window.

| You see | Kind | Export method |
| --- | --- | --- |
| Address bar `cursor.com/agents/bc-…` or a message “export is not available for Cloud Agent” | **Cloud Agent** | Use **Path B** |
| Chat tab inside the Cursor desktop app; right-click tab offers **Export Transcript** | **Desktop chat** | Use **Path A** |
| Both (you opened a Cloud run from Desktop) | Save **both** | Path A if Export works; Path B for the `bc-` URL anyway |

If unsure: copy the URL from the browser or from **Open in Web**. If it contains `/agents/bc-`, it is Cloud.

**Owner 7 Oct 2026 ~18:56 UTC:** confirmed a **cloud icon at the top of the page**. The recovered 10Web thread is a **Cloud Agent**. Use **Path B** only. Desktop **Export Transcript will fail** (Cursor says export is not available for Cloud Agent chats).

---

## Path A — Desktop chat (Export Transcript works)

Do this **in order**.

### A1 — Forensic copy first (best protection)

1. Note the chat **title** and approximate **date**. Do not type in the chat.
2. **File → Exit** Cursor. Task Manager → no `Cursor` process.
3. Copy (do not move) this folder:

   `C:\Users\<YourName>\AppData\Roaming\Cursor\User`

   to something like:

   `J:\Legal-Exhibits\2026-10-07-cursor-user-FORENSIC-COPY\`

4. Zip that copy. In PowerShell:

   ```powershell
   certutil -hashfile "J:\Legal-Exhibits\2026-10-07-cursor-user-FORENSIC.zip" SHA256
   ```

   Paste the SHA256 line into `hash-manifest.txt` with today’s date and your name. Treat the zip as **read-only**. Never unzip it back over live Cursor.

ISI Consulting is a **different** subfolder under `workspaceStorage`. Copying `User` does not rewrite ISI if you copy, not move.

### A2 — In-app markdown export (readable exhibit)

1. Re-open Cursor normally.
2. Open the found thread. **Do not send a message.**
3. **Right-click the chat tab** → **Export Transcript**  
   or the **`⋯`** menu on the editor title bar → **Export Transcript**.  
   Saves a `.md` file.
4. Name it:

   `2026-10-07__10WEB-CURSOR__BEFORE-DURING-AFTER__short-title.md`

5. Save to **two places**: external drive / `J:\Legal-Exhibits\cursor-exports\` **and** Google Drive.

**Limit:** Export Transcript is **visible text only**. Cursor does **not** include collapsed tool calls, terminal output, or file edits. For a lawsuit, keep the **A1 zip** as the fuller original.

### A3 — Extra human-readable copy

With the thread open, **Print → Save as PDF** (or Windows + G / Snipping Tool for long screenshots of key pages: 10Web checklist, Charlie/Marta prompts, kind-louse, WP access). PDFs are easy for counsel even if `.md` is incomplete.

---

## Path B — Cloud Agent (`cursor.com/agents/bc-…`)

Desktop **Export Transcript does not work** on Cloud runs. Cursor says export is unavailable.

1. **Do not archive, kill, or delete** the agent.
2. Copy the full URL (`https://cursor.com/agents/bc-……`) into `EXHIBIT-INDEX.txt`.
3. While logged in as `contact@truth-collective.com`, scroll **top to bottom** once so the UI has loaded the thread.
4. Browser: **Print → Save as PDF** (enable “background graphics” if offered). That is your readable copy.
5. Email **Cursor support**: ask for an official transcript export of that `bcId`, dates July–August 2026, Truth Collective / 10Web. Keep their ticket number in the exhibit index.
6. Do **not** click Continue on that Cloud run to “resume repair.” New work stays in **this** Sep 19 staging Cloud Agent.

---

## After you have files — store, do not “improve”

| Keep | Where |
| --- | --- |
| Forensic `User` zip + SHA256 | External drive / `J:\Legal-Exhibits\` (attorney copy) |
| `.md` export and/or Print PDF | Same folder **plus** Google Drive |
| Cloud `bc-` URL | `EXHIBIT-INDEX.txt` |
| 10Web chat export | Pair as Exhibit T (vendor) vs Exhibit C (Cursor) |

Do **not** paste the full transcript into GitHub. If a redacted excerpt is needed later, strip Application Passwords, Hostinger logins, and 10Web payment details first.

**BDM testimony GitHub copy is already on PR #6.** Three-place save (PC + Drive + that zip): `diagnostics/TC-10WEB-LAWSUIT-THREE-PLACE-SAVE-2026-10-07.md`. Put the Cloud Agent Print-PDF in `Documents\TC-10WEB-LAWSUIT\05-cursor-cloud-thread\`.

Optional index line:

```
C-01  2026-10-07  Cursor 10Web thread  [Desktop export / Cloud bc-________]  SHA256=…
```

---

## Done when

- [ ] Cursor was not asked to keep working in that old thread  
- [ ] Forensic zip exists (Path A) **or** `bc-` URL + Print PDF exist (Path B)  
- [ ] Readable `.md` or PDF is in two places  
- [ ] Hash recorded for the zip  
- [ ] Nothing was uploaded to the public `truth-collective` repo  

When those boxes are checked, tell this Cloud Agent the **title**, **kind** (Desktop vs Cloud), and the **`bc-` URL if Cloud**. Do not paste the full chat here.
