# Backup retention replacement — checklist saves, 10Web’s new Updraft copies, damaged-site rotation

**Prepared:** 12 October 2026  
**Owner:** Daniel Reid. **Migrate-window vendor inside WordPress:** 10Web only.  
**Not a legal opinion.**

This file replaces the earlier “someone deleted backups / actor unknown” shorthand. It records how the healthy pre-migration backups left the **server**, without claiming a 10Web employee clicked Delete on each file by hand.

---

## 1. Why older CPU copies are hard to find, and why that does not weaken 7/25

Daniel and Cursor/Claude spent about **six days** hunting remnants of the July Cursor conversation and any saved backups. He then found the full pre/during/post migration Cursor Cloud conversation (BDM testimony / PR #6 / the PDF he sent this run).

Going further back on disk (30 June, 12 July) **waters down** the picture. Those nights are real Updraft archives. They do not show the continued building that ran from those dates **through 25 July**. Counsel should treat:

- **23 July 19:30** and **24 July 16:59** as the migrate-ready window  
- Earlier Drive/PC copies as proof the Updraft naming and off-server copies exist, not as the best snapshot of the site 10Web was hired to copy

That is why this chat asked for the 23 July `-db.gz` first, not the oldest zip in the folder.

---

## 2. Three layers (keep them separate or 10Web will mix them)

### Layer 1 — Daniel deleted **older-than-checklist** automated backups (not 10Web)

The same Cursor agent that ran the migrate checklist instructed Daniel to free disk so the migration would have storage. The plugin (Updraft) only keeps a limited number of backups.

What Daniel says he did:

1. Take **new** Hostinger/Updraft backups as the checklist required, days before 25 July.  
2. **Open those new backups and confirm they were intact and correct.**  
3. **Then delete older automated plugin backups** so the new ones had room.

That deletion is **owner + Cursor checklist**, not a 10Web act. Disclose it. Those older automated copies were also **not** the 7/25-ready site.

### Layer 2 — 10Web’s admitted new Updraft saves, while they were inside WordPress

Nazeli, 30 September 2026: 10Web used Updraft **to create a new backup for migration**. They deny they “deleted backups.”

Updraft (and similar Hostinger backup slots) holds only **X** archives. When a new backup is saved and the slot is full, the **oldest** remaining archive is dropped. Daniel: every save 10Web made while inside WordPress, by their own admission of using Updraft, **deleted the oldest backup he had just kept**.

That is not a contradiction of their letter. It is how the plugin they admit using works. “We only created a new backup” **is** a deletion of the oldest kept backup when the cap is full.

The healthy backups Layer 1 had just preserved (the checklist copies, verified intact) sat in that finite slot. 10Web’s new migrate-window saves were the next writes into that slot.

### Layer 3 — After about 3 August, automated backups of the **damaged** site

After 10Web’s work in WordPress, the plugin kept running on schedule. Backups from **3 August onward** are copies of the **already damaged** site. Each of those also rotated out whatever older slot remained.

By the 10 October 2026 Updraft “known backups” dump:

- **16** timestamps  
- **Oldest on the server history: 15 September 2026**  
- **No June, July, or August 2026 filenames**  
- Drive SHA256 hashes for 12 July and 23 July **not** in that dump  

That dump is what Layer 3 looks like when it has run for weeks: only damaged-site dailies remain.

The **28 July `db.gz` missing from disk in August** (handoff: File not found when a restore was needed) is the contemporaneous gap. It is not explained by October rotation alone.

---

## 3. End state (truthful sentence)

Daniel, on Cursor’s checklist, cleared older automated backups after verifying new pre-migration backups. 10Web then entered WordPress, admitted using Updraft to create new backups, and the plugin cap dropped the oldest remaining (the healthy checklist copies). After about 3 August the same plugin kept saving the destroyed site until the server history showed only mid-September onward. Off-server copies from 12 July, 23 July, 24 July, and 30 June still exist on Daniel’s PC and Google Drive. Restores from what the server still offered did not return the migrate-source site.

10Web did not need a separate “delete all backups” click. Their admitted Updraft use plus the retention cap, then damaged-site automation, replaced every healthy server copy the checklist had required.

---

## 4. How this answers the 30 September denial

| 10Web sentence | Accurate counter |
| --- | --- |
| We did not delete backups | Creating a new Updraft archive when only X slots exist **drops the oldest**. That is deletion by replacement. They admit the new save. |
| We only created a backup for migration | That new save is Layer 2. Combined with Layer 3 (post-3 Aug damaged dailies), the healthy checklist copies are gone from the server. |
| Source remained live / DNS unchanged | Irrelevant to Updraft slot rotation on `tcstaging`. |

Do **not** say Daniel never deleted any backup. He deleted older-than-checklist copies for storage after verifying the new ones. Do **not** say 10Web formatted the disk. Say retention replacement while they were the only vendor in WordPress.

---

## 5. What to send next (specific)

1. Screenshot of Updraft **“retain this many backups”** (the number X). The 10 Oct dump showing 16 known backups is a clue, not a setting.  
2. Print-PDF page from the July Cursor conversation where the agent said to delete older plugin backups for migrate storage.  
3. Confirm whether **24 July 16:59** (or 23 July 19:30) is the set he opened and verified intact before deleting older ones.  
4. Still: upload `backup_2026-07-23-1930_…-db.gz` for offline SQL read. That night is closer to 7/25 than 30 June. Do not restore it onto staging.
