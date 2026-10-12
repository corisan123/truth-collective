# Find the clean July backups on the CPU and jump drive

**Prepared:** 12 October 2026  
**Owner:** saved copies in several places (Hostinger, CPU, jump drive). Hostinger no longer lists July. Hunt **off the server**.

Do not restore Hostinger. Do not upload “first 20 files” from a mixed folder.

## 1. What a real backup looks like

Updraft names, not Notepad++ and not plugin CSS:

```
backup_2026-07-23-1930_The_Truth_Collective_<hex>-db.gz
backup_2026-07-24-1659_The_Truth_Collective_<hex>-db.zip
backup_2026-07-24-1659_The_Truth_Collective_<hex>-plugins.zip
backup_2026-07-24-1659_The_Truth_Collective_<hex>-uploads.zip
backup_2026-07-24-1659_The_Truth_Collective_<hex>-uploads2.zip
backup_2026-07-24-1659_The_Truth_Collective_<hex>-themes.zip
backup_2026-07-24-1659_The_Truth_Collective_<hex>-others.zip
```

A **clean night** is every suffix with the **same** `YYYY-MM-DD-HHMM` stamp. Best windows: **23 July 19:30** and **24 July 16:59**.

## 2. Already found (do not hunt these again as if missing)

| Place | What it is |
| --- | --- |
| Drive `C:\Users\dreid\My Drive\UpdraftPlus\` | 12 Jul and **23 Jul** `-db.gz` (hashed). 23 Jul SHA256 `03FD3A90…4284A` |
| CPU Explorer shot | Four **24 Jul 16:59** files: 50,111 / 10,774 / 392,691 / 392,197 KB plus the 23 Jul 19,827 KB db |
| Hostinger Updraft list 10 Oct | Oldest **15 Sep 2026**. July is gone from the **server** slot. Local copies are the remaining originals. |

## 3. Not a website backup (skip these folders)

| Folder / files already opened | What they actually are |
| --- | --- |
| Code Snippets `menu.scss` / `manage.css` / webpack js | WP plugin admin assets |
| 7/25 `10web-manager.php` + CSS + EvergrowSans fonts | 10Web Manager v1.20.21 (vendor tool, useful; not catalogs) |
| `nppPluginList.dll` `Monokai.xml` `Hello Kitty.xml` | **Notepad++** plugins and color themes. Path is usually `AppData\Roaming\Notepad++` or `Program Files\Notepad++` |
| `pasted confirmed clean css code_files\` (`frame.html`, `root-*.css`, `sdk.js.download`) | **ChatGPT.com** “Webpage, Complete” chrome. Not Additional CSS. |

Notepad++ is the **editor** you use to peek SQL. Its themes folder is not the backup. A 7/24 date on those files only means that copy of Notepad++ data was touched or saved that day.

## 4. Paste this in PowerShell (plug the jump drive in first)

Lists every drive, then finds Updraft `backup_2026-07*` names and July `.sql` / `-db.gz` / `-db.zip`. It does not open Hostinger. It does not restore anything.

```
Get-PSDrive -PSProvider FileSystem | Select-Object Name, Root, Used, Free | Format-Table -AutoSize

$roots = @()
Get-PSDrive -PSProvider FileSystem | ForEach-Object { $roots += $_.Root }
$roots += "$env:USERPROFILE\My Drive"
$roots += "$env:USERPROFILE\Desktop"
$roots += "$env:USERPROFILE\Documents"
$roots += "$env:USERPROFILE\Downloads"
$roots += "$env:USERPROFILE\TC-backup-review"
$roots = $roots | Select-Object -Unique

$hits = foreach ($root in $roots) {
  if (-not (Test-Path $root)) { continue }
  Get-ChildItem -Path $root -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object {
      $_.Name -like 'backup_2026-07-*The_Truth_Collective*' -or
      $_.Name -like 'backup_2026-06-30-*The_Truth_Collective*' -or
      ($_.Name -match 'Truth.?Collective' -and $_.Extension -in '.gz','.zip','.sql')
    }
}

$hits |
  Select-Object FullName, @{N='KB';E={[int]($_.Length/1KB)}}, LastWriteTime |
  Sort-Object FullName |
  Format-Table -AutoSize
```

If a full `C:\` recurse is too slow, run it on the jump drive letter only (example `E:\`):

```
Get-ChildItem E:\ -Recurse -File -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like 'backup_2026-07-*' } |
  Select-Object FullName, @{N='KB';E={[int]($_.Length/1KB)}}, LastWriteTime |
  Format-Table -AutoSize
```

## 5. How to know a hit is worth opening

| Stamp in the name | Slices you want | First action |
| --- | --- | --- |
| `2026-07-23-1930` | `-db` plus uploads if they exist | 7-Zip the db. Search SQL for `tc-overlay-card` / `amzn.to`. Attach that **one** ~19 MB db here if dense. |
| `2026-07-24-1659` | db + plugins + both ~392 MB uploads (+ themes/others if present) | Keep as **one** night. Do not mix with 7/23. Local WP only after SQL peek. |
| `2026-07-12-1930` or `2026-06-30-1930` | Real, but earlier than migrate-ready | Proof copies exist. Not the best night. |
| Anything in `Notepad++`, `code-snippets`, or only `.xml`/`.dll` | Skip | Wrong folder. |

Copy each complete night into `%USERPROFILE%\TC-backup-review\<stamp>\` before peeking. Originals stay put.

## 6. What to send this Cloud run

Paste the PowerShell **table** (full paths + sizes). That is more useful than another 20-file dump.

Then, if 23 July `-db` is in the table, attach that **one** file. Do not attach 392 MB uploads. Do not restore Hostinger from a jump-drive copy until this run has seen the listing.
