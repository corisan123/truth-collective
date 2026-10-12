# 10Web-related lines in the 10 October 2026 `tcstaging` error log

**PDFs:** `docs/legal/source-pdfs/WP-error-debug-log-2026-10-10.pdf` and `Hostinger-error-log-2026-10-10.pdf` (same log family).

| Time (UTC) | What the log actually says |
| --- | --- |
| 25 Jul 2026 20:00:05 | `10web-manager/includes/class-rest-api.php` line 444: Undefined array key `sftp_credentials` |
| 3 Aug 2026 15:57:07 | Same 10Web Manager REST warning |
| 7 Aug 2026 14:15:06–07 | Rank Math Pro file missing; Kadence `Shutdown_Collection.php` missing; ActionScheduler fatal; PHP `include_path` lists four `10web-manager/vendor/pear/...` paths |
| 7 Aug 2026 15:31:32 | ActionScheduler `Unidentified action 27828` fatal (Hostinger plugin vendor path) |

No log line contains the sentence “10Web destroyed the site.” The 25 Jul and 3 Aug rows are 10Web Manager executing on staging. The 7 Aug rows are missing plugin files during the incident-letter day, with 10Web Manager still on the include path.
