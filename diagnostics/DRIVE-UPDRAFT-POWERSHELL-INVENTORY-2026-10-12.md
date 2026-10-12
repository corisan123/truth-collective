# Drive Updraft listing — 12 October 2026 PowerShell (suffixes now named)

**Source:** owner-pasted `Get-ChildItem` of `C:\Users\dreid\My Drive\UpdraftPlus\`  
**Drives present:** C, D, F, G, H, I, J. **Only hits:** Drive `UpdraftPlus`. Each file printed twice (C:\ recurse + `My Drive` path). Deduped below.  
**Do not restore Hostinger.**

Size-based guesses in earlier notes are **withdrawn**. Real suffixes:

## Deduped inventory

| Stamp | File (nonce) | KB | Role |
| --- | --- | --- | --- |
| 2026-06-30-1930 | `…11b0badf493f-mu-plugins.zip` | 11 | mu-plugins |
| 2026-06-30-1930 | `…11b0badf493f-others.zip` | 174 | others (already opened) |
| 2026-06-30-1930 | `…11b0badf493f-plugins.zip` | 47,132 | plugins (**not** db) |
| 2026-06-30-1930 | `…11b0badf493f-themes.zip` | 10,773 | themes |
| 2026-06-30-1930 | `…-uploads.zip` … `uploads6.zip` | 406,397 / 391,223 / 391,589 / 391,358 / 391,455 / 330,565 | six media splits |
| 2026-07-12-1930 | `…a2f57e449b46-db.gz` | 17,390 | **database only** |
| 2026-07-23-1930 | `…c9570a105596-db.gz` | 19,827 | **database only** (hashed) |
| 2026-07-24-1659 | `…93bbf2b8c244-plugins.zip` | 50,110 | plugins (**not** db) |
| 2026-07-24-1659 | `…93bbf2b8c244-themes.zip` | 10,773 | themes (the boxed ~10,774 KB file) |
| 2026-07-24-1659 | `…93bbf2b8c244-uploads.zip` | 392,691 | media |
| 2026-07-24-1659 | `…93bbf2b8c244-uploads2.zip` | 392,197 | media |

## What is missing on Drive

| Night | Has | Missing |
| --- | --- | --- |
| 30 Jun 19:30 | plugins, themes, others, mu-plugins, six uploads | **`-db`** |
| 12 Jul 19:30 | `-db.gz` | uploads, plugins, themes |
| 23 Jul 19:30 | `-db.gz` | uploads, plugins, themes |
| 24 Jul 16:59 | plugins, themes, two uploads | **`-db`**, others |

**No complete same-stamp night (db + uploads) is on Drive.** That is why a Hostinger uploads-only restore crushed Computers: 24 July local copies are files without a matching database.

USB letters D, F, G, H, I, J returned **no** extra `backup_2026-07-*The_Truth_Collective*` paths in this run. Either empty of those names, or the recurse skipped them. Search those letters **only** for `-db` next.

## Which file to open

1. **Peek first:** `C:\Users\dreid\My Drive\UpdraftPlus\backup_2026-07-23-1930_The_Truth_Collective_c9570a105596-db.gz` (SQL only).  
2. **Do not** pair that db with 24 July photos (`93bbf2b8c244-uploads*`). Different stamp, different nonce.  
3. **Do not** treat 50,110 KB as a database. It is `-plugins.zip`.  
4. Hunt USB for `backup_2026-07-24-1659_*db*` and any other `*-db.gz` / `*-db.zip`.
