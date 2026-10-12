# 10Web Manager folder dated 25 July 2026 — first two batches

**Reviewed:** 12 October 2026  
**Owner statement:** folder found on the CPU from **7/25/26** (migrate-start day). This is only part of the plugin tree.  
**Do not restore. Do not activate. Read only.**

This dump is the **10WEB manager plugin**, not Truth Collective CSS, not Updraft, not catalogs.

## What arrived

**Batch 1 (plugin root + some CSS):** `10web-manager.php`, `config.php`, `config.json`, `env.php`, `manager.php`, `phpstan.neon`, `readme.txt`, `backgrounds.css`, `deactivation-popup.css`, `jquery.tag-editor.css`, `login.css`, `main.css`

**Batch 2 (more CSS + fonts):** `migrate-notice.css`, `tenweb_trial_flow.css`, `twbb-copilot-templates.css`, `twbbm_introducing_copilot_notice.css`, `whitelabel.css`, `EvergrowSans-Bold.ttf`, `EvergrowSans-Medium.ttf`

**Screenshot with the batches:** 10Web marketing card “10 Components to Make Your WordPress Website Better” / LOGIN / SIGN UP. That is the plugin’s **connect-your-site** chrome (`login.css`), not a TC page.

## Headline

1. Plugin header is **Version: 1.20.21**. That is the **same version** Site Health still listed **Active** on staging 8 Aug and 10 Oct 2026.  
2. `config.json` is a **live migration run config**, not empty shipping chrome. **Migration debug is on.** Archives upload to **10Web S3**. SFTP is off.  
3. `manager.php` always loads `class-migration-run.php` and registers REST `tenweb/v1` (`class-rest-api.php`). The 25 Jul error log hit that REST file.  
4. Almost all CSS/fonts in these two batches are 10Web dashboard / Copilot / trial UI. One CSS file matters: `migrate-notice.css` styles the banner “The Copy of Your Website on 10Web Hosting is Ready.”

## `config.json` (the file that matters)

Pretty-printed from the uploaded 590-byte file:

```json
{
  "TENWEB_MIGRATION_DEBUG": "1",
  "TENWEB_MIGRATION_ARCHIVE_TYPE": "nelexa_zip",
  "TENWEB_MIGRATION_MAX_FILES_RESTART": "10000",
  "TENWEB_MIGRATION_BULK_FILES_COUNT": "10000",
  "TENWEB_MIGRATION_MAX_DB_ROWS_RESTART": "100000",
  "TENWEB_MIGRATION_BULK_DB_ROWS_COUNT": "5000",
  "TENWEB_MIGRATION_FILE_SIZE_LIMIT": "300000000",
  "TENWEB_MIGRATION_MULTIPLE_ARCHIVES": "1",
  "TENWEB_MIGRATION_EXEC_TIME_OFFSET": "10",
  "TENWEB_MIGRATION_ENCRYPT_DB": 1,
  "": 0,
  "TENWEB_MIGRATION_MULTIPART_UPLOAD_CHUNK_SIZE": 5,
  "TENWEB_MIGRATION_UPLOAD_ARCHIVE_S3": 1,
  "TENWEB_MIGRATION_SFTP": 0,
  "TENWEB_MIGRATION_SFTP_STATE_FILES_COUNT": 100
}
```

| Flag | Meaning |
| --- | --- |
| `TENWEB_MIGRATION_DEBUG`: 1 | Migration debug mode on. Plugin admin grows a **Migration Logs** submenu when debug is on. |
| `TENWEB_MIGRATION_UPLOAD_ARCHIVE_S3`: 1 | Migrate archives go to 10Web S3 (`10web-products-production` in `env.php`). |
| `TENWEB_MIGRATION_MULTIPLE_ARCHIVES`: 1 | Split zip sets, not one file. |
| `TENWEB_MIGRATION_FILE_SIZE_LIMIT`: 300000000 | 300 MB cap per file. |
| `TENWEB_MIGRATION_ENCRYPT_DB`: 1 | Database dump encrypted in the migrate package. |
| `TENWEB_MIGRATION_SFTP`: 0 | SFTP path off. |
| empty key `"": 0` | Dirty extra field. Looks **written by a run / save_configs**, not a clean shipped default. |

**Tie to the 25 July error log:** staging `class-rest-api.php` line 444, undefined array key `sftp_credentials`, **25 Jul 2026 20:00:05 UTC**. This JSON has SFTP off. REST still touched SFTP credentials that night. Consistent with a migrate in progress using this plugin, S3-on / SFTP-off.

This file does **not** by itself prove this exact JSON was the in-memory copy at 20:00 UTC. It does prove a 25 July Manager tree on the CPU was configured to **run a migration**, debug on, push archives to 10Web S3.

## Plugin bootstrap (`10web-manager.php` + `config.php` + `manager.php`)

- REST namespace: `tenweb/v1`. `init_rest_api()` loads `includes/class-rest-api.php` (that file is **not** in these batches; it is the next file to send).  
- Always includes `includes/class-migration-run.php` (also missing from these batches).  
- Debug mode (`?tenweb_debug=1`) adds menus: Config, Logs, **Migration Logs**, Php info.  
- Query `twb_wp_login_token` logs a WordPress user in (dashboard “magic link”). High-level only: this is how remote 10Web dashboard access enters WP. Do not treat that as a how-to.  
- Can also load from **must-use** path `wp-content/mu-plugins/10web-manager/`. If that folder exists on 7/25, Manager survives ordinary plugin deactivation.  
- `TENWEB_USERNAME` is `tenweb_manager_plugin`.  
- After-migrate admin notice: “The Copy of Your Website on 10Web Hosting is Ready” (`migrate-notice.css`). That banner is 10Web’s hosted **copy**, which matches kind-louse / fake Builder sites, not a successful Hostinger rebuild.

`readme.txt` still says Stable tag **1.2.34**. The running header is **1.20.21**. The readme is stale marketing (backup.10web.io, one-click migrate). Use the PHP header for version.

`env.php` lists 10Web endpoints: `manager.10web.io`, `backup.10web.io`, `core.10web.io`, Builder API, and a **public** Firebase Copilot client config. That Firebase blob ships in the plugin. It is 10Web product telemetry, not a Truth Collective secret.

## CSS / fonts (batch 2 and the CSS from batch 1)

| File | What it is | Interesting? |
| --- | --- | --- |
| `login.css` | Connect / SIGN UP card (matches the screenshot) | Only as UI ID of this folder |
| `migrate-notice.css` | Post-migrate “copy on 10Web Hosting is Ready” banner | **Yes** |
| `main.css` `backgrounds.css` | Manager dashboard | No |
| `tenweb_trial_flow.css` | Free-trial admin bar | No |
| `twbb-copilot-templates.css` `twbbm_introducing_copilot_notice.css` | 10Web Builder Copilot upsell | No (10Web Copilot, not TC engine) |
| `whitelabel.css` `deactivation-popup.css` `jquery.tag-editor.css` | Chrome | No |
| EvergrowSans fonts | 10Web brand webfonts | No |

Zero `tc-overlay-card`, `amzn.to`, or Additional CSS in these files.

## What this proves / does not prove

**Proves**

- A 25 July CPU folder is **10WEB manager 1.20.21**, the same plugin later found Active on staging.  
- That copy was configured for an **actual migration** (debug, S3 archive upload, split zips, 300 MB cap).  
- The plugin can remote-login, run REST, run a migration class, and show a “hosted copy is ready” banner.  
- 10Web Copilot / trial CSS in the same folder is 10Web product UI, not TC catalogs.

**Does not prove**

- That this folder is a healthy pre-migrate **site** backup (it is the vendor plugin).  
- That 10Web clicked Delete on Hostinger Updraft files.  
- Catalogs, Additional CSS, or child pages (none of that is here).

## Next files from the same 7/25 folder (still missing)

Send these before more CSS/fonts:

1. `includes/class-rest-api.php` (error log 25 Jul line 444)  
2. `includes/class-migration-run.php`  
3. `includes/class-helper.php` (migration log reader)  
4. Anything named `*log*` / `*migration*` / `10web_tmp`  
5. Folder `mu/` if present  
6. A screenshot of the **folder path** so the 7/25 date is on disk, not only in chat  

Keep under 20 files. Skip more CSS.