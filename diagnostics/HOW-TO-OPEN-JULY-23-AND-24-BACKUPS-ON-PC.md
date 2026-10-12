# How to open the 23 July and 24 July backup folders on the PC

**Safest rule:** do not restore these onto Hostinger (live or staging) yet. Copy one complete night into a new folder. Peek. Only then, if you want to *see* the site, restore that copy into Local WP on the PC.

Updraft does not save extra websites when a date has more than two files. It saves **one night as several slices**: `-db`, `-uploads` (sometimes two), `-plugins`, `-themes`, `-others`. The 12 Oct Explorer shot of 24 July is four files with the **same** stamp `backup_2026-07-24-1659_`: two ~392 MB uploads, one 10,774 KB plugins zip, one 50,111 KB database zip. 23 July in that shot is one 19,827 KB archive; matching slices may still sit in Drive as `.gz`. Mix 23 July database with 24 July photos and you get the same class of damage as the August uploads-only restore.

**Group by the full timestamp in the filename** (`2026-07-23-1930` vs `2026-07-24-1659`), not by the calendar day Explorer shows.

---

## 0. Do not use

- Hostinger **Website Backup Restore** (hits live)
- Updraft **Continue** on staging
- Cursor Desktop (that window is ISI only)
- Mixing files from 7/23 with files from 7/24

---

## 1. See the real names, grouped by night (Explorer truncates them)

Open PowerShell. Paste this. It prints every file in the Drive Updraft folder, then groups them by the `YYYY-MM-DD-HHMM` stamp so four 24 July files stay one night.

```
$updraft = "C:\Users\dreid\My Drive\UpdraftPlus"

Get-ChildItem $updraft |
  Select-Object Name, Length, LastWriteTime |
  Sort-Object Name |
  Format-Table -AutoSize

Get-ChildItem $updraft |
  Where-Object { $_.Name -match '^backup_(\d{4}-\d{2}-\d{2}-\d{4})_' } |
  Group-Object { if ($_.Name -match '^backup_(\d{4}-\d{2}-\d{2}-\d{4})_') { $Matches[1] } } |
  ForEach-Object {
    "==== $($_.Name)  ($($_.Count) files) ===="
    $_.Group | ForEach-Object { "  {0,12:N0} KB  {1}" -f ($_.Length / 1KB), $_.Name }
  }
```

If the zips also live in another folder (the Explorer window from 12 Oct), change `$updraft` to that path and run it again. Do not merge the two folders into one restore.

You want groups whose stamp is:

- `2026-07-23-1930`
- `2026-07-24-1659`

The **end** of the name is the slice:

| Suffix | What it is | Typical size in your listing |
| --- | --- | --- |
| `-db.gz` or `-db.zip` | WordPress database (pages, CSS in options, catalogs) | 7/23 ~19,827 KB; 7/24 ~50,111 KB |
| `-uploads.zip` / `-uploads2.zip` | Media | ~392 MB each on 7/24 |
| `-plugins.zip` | Plugins | ~10,774 KB on 7/24 (the boxed file) |
| `-themes.zip` | Themes | often tens of MB |
| `-others.zip` | Leftovers (fonts, object-cache). Not the site. | ~174 KB on 6/30 |

A complete night is **all of those suffixes with the same date-time prefix**. Treat a group as incomplete until `-db` plus at least one `-uploads` are present. If 7/23 only has a `-db` (the 19,827 KB row in the 12 Oct shot, and the hashed Drive `.gz`), do not pair it with 7/24 uploads. Look in Drive and in the screenshot folder for other `2026-07-23-1930` slices first. If none exist, peek the 7/23 database alone (step 3) and keep 7/24 as its own night.

Expected groups from the 12 Oct Explorer shot (names were truncated; suffixes come from size):

```
==== 2026-07-24-1659  (4 files) ====
     392,197 KB  backup_2026-07-24-1659_…-uploads.zip   (or uploads2)
     392,691 KB  backup_2026-07-24-1659_…-uploads2.zip  (or uploads)
      10,774 KB  backup_2026-07-24-1659_…-plugins.zip   (the boxed file)
      50,111 KB  backup_2026-07-24-1659_…-db.zip

==== 2026-07-23-1930  (1 file in that shot) ====
      19,827 KB  backup_2026-07-23-1930_…-db.gz
```

Those four 24 July files are one website backup, not four sites. The 23 July row is database-only in that window until other `1930` slices are found.

---

## 2. Copy one night aside (do not work in Drive)

```
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\TC-backup-review\2026-07-23-1930"
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\TC-backup-review\2026-07-24-1659"

Copy-Item "C:\Users\dreid\My Drive\UpdraftPlus\backup_2026-07-23-1930_The_Truth_Collective_*" "$env:USERPROFILE\TC-backup-review\2026-07-23-1930\"
Copy-Item "C:\Users\dreid\My Drive\UpdraftPlus\backup_2026-07-24-1659_The_Truth_Collective_*" "$env:USERPROFILE\TC-backup-review\2026-07-24-1659\"
```

If those files are not in Drive, change the source path to the folder in the screenshot. Originals stay put. You only work in `TC-backup-review`.

Hash the copies so they match the Drive hashes you already made:

```
Get-ChildItem "$env:USERPROFILE\TC-backup-review" -Recurse -File |
  Get-FileHash -Algorithm SHA256 |
  Format-List
```

---

## 3. Cleanest first look (no WordPress install)

Install **7-Zip** if it is not already there.

**Database (this tells you if catalogs exist):**

1. In 7-Zip, open the `-db.gz` or `-db.zip` for **one** night.  
2. Extract only that one file into the same review folder. You should get a `.sql` (sometimes still gzipped once more).  
3. Do **not** need to read the whole file. In Notepad++ or VS Code, search:

- `tc-overlay-card`
- `amzn.to`
- `computers-digital-devices`
- `Emerging`
- `Wearables`
- `office-workspace`

If those strings are dense, that night’s **content** is present. If the SQL is tiny or those strings are missing, skip that night.

**Uploads (this tells you if photos exist):**

In 7-Zip, **open** the ~392 MB zip (do not extract all 392 MB yet). Browse to `uploads/2026/07/`. If product JPGs are listed, media for that month is in the archive. Then close 7-Zip.

Peek **23 July** first (already hashed `-db.gz`), then **24 July** the same way. Do not merge them.

---

## 4. Cleanest way to *see* the website (PC only)

Only after step 3 looks like a real catalog.

1. Install **Local** (Local WP) from localwp.com. Create a **new empty** site, PHP 8.x, name it `tc-review-0723` (or `0724`).  
2. Copy **every** file from that one review folder into the Local site’s `app/public/wp-content/updraft/` (create `updraft` if missing).  
3. In that Local site’s WP admin, install **UpdraftPlus**, open Existing backups, restore **Database + Plugins + Themes + Uploads + Others** from that one timestamp.  
4. After restore, Settings → Permalinks → Save.  
5. Browse `http://tc-review-0723.local` (or whatever Local assigned).  

That is a private copy on your machine. It does not touch Hostinger. If Computers, Office children, and overlays look like the pre-migrate site, that night is the candidate to talk about for a later **staging-only** restore.

If Local asks for a site URL, keep the Local URL. Do not type `truth-collective.com` or `tcstaging`.

---

## 5. What to send this Cloud run after a peek

- The PowerShell table from step 1 (full names + sizes).  
- Or the **23 July `-db`** file only (~19 MB) if search in step 3 looks dense.  

Do not send 392 MB uploads here. Do not restore onto staging until this Cloud run has seen the name list and, ideally, the 23 July database.

---

## 6. Why these CPU files are not on Hostinger, and which row to open

The five rows in the 12 Oct Explorer window (page 1 of 13, 23 July highlighted) are **copies you saved off the server**. Hostinger’s live Updraft list is a **rotating slot** of recent archives in `wp-content/updraft/`. Those two places are not the same pile.

**Why Hostinger no longer lists 23 July / 24 July**

- Those names are UpdraftPlus archives (`backup_YYYY-MM-DD-HHMM_The_Truth_Collective_…`). On the server they live only while the plugin still keeps that timestamp.
- Updraft keeps a limited number of backups. A new save drops the oldest.
- 10Web’s 30 Sep letter admits they **used Updraft to create a new backup** during the migrate window. That new save is enough to push a healthy July copy out of the slot.
- After about 3 August the same plugin kept saving the **already damaged** site on a schedule. Each of those also rotated out older files.
- The 10 Oct Hostinger/Updraft dump lists 16 timestamps. **Oldest on the server: 15 September 2026.** No June, July, or August filenames. The Drive SHA256 of this 23 July `-db.gz` is **not** in that dump.
- Your CPU/Drive copies do not rotate. That is why you still have 19,827 KB from 23 July 7:30 PM and the four 24 July 5:00 PM files, and Hostinger does not.

What this does **not** require: a proof that 10Web clicked Delete on each Hostinger file. Replacement by new saves is enough. Hostinger’s separate “Website Backup” product is also not these five files.

**Why the sizes differ (this exact window)**

| Row | Date in Explorer | Size | What it is | Open as a website? |
| --- | --- | --- | --- | --- |
| Highlighted | 7/23/2026 7:30 PM | 19,827 KB | **Database** (`-db.gz`) for `2026-07-23-1930` | No. Peek SQL only. |
| 2 | 7/24/2026 5:00 PM | 50,111 KB | **Database** for `2026-07-24-1659` | Only together with the three files below. |
| 3 | 7/24/2026 5:00 PM | 10,774 KB | **Plugins** | No, not alone. |
| 4 | 7/24/2026 5:01 PM | 392,691 KB | **Uploads** (photos) | No, not alone. |
| 5 | 7/24/2026 5:01 PM | 392,197 KB | **Uploads** part 2 | No, not alone. |

They are different sizes because they are different **parts** of a backup, the way a database is smaller than a photo library. The two ~392 MB files are almost the same size because they are two halves of media, not two sites.

**Which one to open**

1. **First:** the highlighted 19,827 KB file (`c9570a105596-db.gz`). 7-Zip → inner `.sql` → search `tc-overlay-card` / `amzn.to`. That answers “are catalogs in the last hashed night before migrate.”
2. **To see a website:** all **four** 24 July rows together in Local WP (50,111 + 10,774 + 392,691 + 392,197). Same stamp `1659`. Never one of the 392 MB files by itself.
3. **Do not** pour the 23 July database into the 24 July photos. That mix already crushed Computers once.

If 23 July SQL is dense, attach that one 19,827 KB file here. Leave the 392 MB files on the PC.
