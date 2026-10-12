# First upload batch from alleged 24 July 2026 backup folder

**Reviewed:** 12 October 2026  
**This Cloud run:** `bc-3c3a1616-bd53-407e-8562-11da050498f8`  
**Owner:** files came from a large saved folder thought to be a healthy pre-migrate backup. Upload cap hit at 20 files.

## What this batch is

**Code Snippets WordPress plugin admin assets** (plugin slug `code-snippets`, admin menu “Snippets,” orange scissors-in-play logo). Not Truth Collective page CSS, not Additional CSS, not product HTML.

| Owner filename | What the bytes actually are |
| --- | --- |
| `menu.scss` | Plugin SCSS theme tokens (`$primary: #03c7d2`, snippet-type badges php/html/css/js) |
| `_sidebar.scss` `_form.scss` `_editor.scss` `_conditions.scss` `_gpt.scss` `_cloud.scss` `edit.scss` `welcome.scss` `manage.scss` | Admin UI: CodeMirror snippet editor, `.snippet-form.php-snippet` / css / js / html, `.code-snippets-modal`, cloud-sync colors |
| `editor.js` `edit.js` `settings.js` `import.js` | Mix of plugin SCSS and webpack/`classnames` bundles named `webpackChunkcode_snippets` |
| `prism.css` `settings.css` `manage.css` `manage-rtl.css` `edit.css` | Prism highlighter, php-parser (build 31 Dec 2024), CodeMirror editor bundles |

**Zero** matches for `tc-overlay-card`, `tc-explore-hub`, `tc-book-card`, `amzn.to`, Kadence, or Astra in this batch.

Typical disk path for these files: `wp-content/plugins/code-snippets/` (css / js / scss). They ship with the **plugin**, whether or not Daniel ever saved a snippet.

## What this batch is not

- Not a dump of Appearance → Customize → Additional CSS  
- Not a Hostinger full `public_html/tcstaging` tree  
- Not proof by itself that 10Web wiped Updraft/Hostinger backups  
- Not the healthy Computers / Tech Hub markup from 24–25 July  

8 August recovery notes recorded: Code Snippets was **not** the home of TC CSS; Additional CSS was. Plugin files can still sit in `wp-content/plugins` unused.

## Next batches that would actually test a “healthy 24 Jul backup”

Send folders/files named like:

- `wp-content/uploads/2026/07/` (product JPGs)  
- `wp-content/themes/` or Astra child  
- `*.sql` / `database` / `u867403816`  
- copies of Additional CSS or `wp-custom-css`  
- `page-*.html` or `computers` / `technology-hub`  
- Updraft archives `backup_2026-07-24*` / `backup_2026-07-25*`  

Stay at **20 files or fewer** per send. Prefer a folder listing (names + dates + sizes) of the backup root before more plugin CSS.
