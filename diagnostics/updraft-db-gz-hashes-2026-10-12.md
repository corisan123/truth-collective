# Updraft database `.gz` SHA256 hashes — Drive copies dated 12 Jul and 23 Jul 2026

**Recorded:** 12 October 2026  
**Source:** owner-pasted Windows PowerShell from `C:\Users\dreid\My Drive\UpdraftPlus\`  
**Command:** `Get-ChildItem "C:\Users\dreid\My Drive\UpdraftPlus\*.gz" | Get-FileHash -Algorithm SHA256 | Format-List`  
**This agent has not opened the `.gz` files.** Hashes and paths are transcribed as pasted.  
**Do not restore these into staging or live.**

## Hashes (copy exactly)

| Backup timestamp in filename | Full path on Drive | SHA256 |
| --- | --- | --- |
| 12 Jul 2026 19:30 | `C:\Users\dreid\My Drive\UpdraftPlus\backup_2026-07-12-1930_The_Truth_Collective_a2f57e449b46-db.gz` | `D2F31A9413BE076C04028C79C3BF2A0B875DEBD7545CA6DDE2E36296C777D581` |
| 23 Jul 2026 19:30 | `C:\Users\dreid\My Drive\UpdraftPlus\backup_2026-07-23-1930_The_Truth_Collective_c9570a105596-db.gz` | `03FD3A90954285632778C47B0B033E66171C3263117114971EE4D85DAD04284A` |

Both filenames end in `-db.gz`. That is the **WordPress database** slice of an UpdraftPlus backup, not plugins, not uploads, not `others`.

## What this proves

1. Daniel has **Google Drive** copies of two Updraft **database** archives dated **12 July** and **23 July 2026**. Both dates are **before** the owner-stated 25 July migrate start. 23 July 19:30 is the last hashed DB night before migrate.
2. The hashes are fingerprints. If the same filenames still exist on Hostinger (`wp-content/updraft/` or File Manager), matching SHA256 means the server copy is byte-identical to the Drive copy. A different hash means the server file was rewritten. A missing file means the Drive copy is the remaining original for that timestamp.
3. The Windows Explorer listing from earlier today showed a **17,391 KB** file at 12 Jul 7:30 PM and a **19,827 KB** file at 23 Jul 7:30 PM. Those sizes fit these `-db.gz` archives. The earlier size-guess of “one slice of a smaller set” is now **named**: they are database dumps.
4. `Get-ChildItem *.gz` returned **only these two files**. 30 June and 24 July database slices in the Explorer shot are almost certainly **`.zip`**, not `.gz`. That is why they did not appear in this hash run.

## What this does not prove

- That the SQL inside either `.gz` is the healthy migrate-source site (files not opened here).
- That 10Web deleted the server copies (no File Manager listing compared yet).
- That 24 July 16:59 is hashed or present in this Drive `*.gz` folder.

## Next commands (same PowerShell window)

Hash the zip slices in the same Drive folder (24 Jul and 30 Jun live here if they were copied):

```
Get-ChildItem "C:\Users\dreid\My Drive\UpdraftPlus\*.zip" | Get-FileHash -Algorithm SHA256 | Format-List
```

List every file name, size, and date so truncated Explorer names are complete:

```
Get-ChildItem "C:\Users\dreid\My Drive\UpdraftPlus" | Select-Object Name, Length, LastWriteTime | Format-Table -AutoSize
```

If the 23 July `-db.gz` can be uploaded here (about 19 MB), this agent can inspect it **offline** for page counts, `amzn.to`, and `tc-*` classes. That is a read of a local archive, not a restore onto staging.
