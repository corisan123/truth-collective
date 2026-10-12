# “pasted confirmed clean css code _files” — ChatGPT page chrome, not Additional CSS

**Reviewed:** 12 October 2026  
**Owner:** folder dated 7/24/26 in Notepad; “pasted confirmed clean css code _files”; more files remain on disk.

This batch is a browser **Webpage, Complete** save of **chatgpt.com**. The `_files` folder is ChatGPT’s UI (conversation layout, code-block highlighter, Sentinel SDK). It is not Appearance → Customize → Additional CSS and not an Updraft backup.

## What the bytes are

| Owner filename | What it is |
| --- | --- |
| `frame.html` | `saved from url=https://chatgpt.com/backend-api/sentinel/frame.html` |
| `saved_resource.html` | `saved from url=about:blank` plus `chatgpt.com/cdn-cgi/challenge-platform` |
| `sdk.js.download` `sdk(1).js.download` | ChatGPT **SentinelSDK** (`chatgpt.com/sentinel/…/sdk.js`) |
| `conversation-small-*.css` `cot-message-*.css` `code-block-*.css` `root-*.css` (~1.4 MB, twice) `silk-hq-*.css` `model-cursor-*.css` `payment-cards-skeleton-*.css` `product-variants-*.css` `ADAVisualizationComponent-*.css` `table-components-*.css` `ansi-*.css` | Hashed ChatGPT frontend CSS (`general-agent-cot-root`, ProseMirror composer, code-block fullscreen). `product-variants` is ChatGPT shop UI, not TC products. |

Zero matches for `tc-overlay-card`, `tc-explore-hub`, `tc-book-card`, `amzn.to`, `wp-custom-css`, Kadence, or Truth Collective.

The orange **DR** avatar in the same send is a chat-profile thumbnail, not a site file.

## Why the name fooled the hunt

Windows “Save as Webpage, Complete” creates:

```
pasted confirmed clean css code.html      ← the conversation (maybe has the pasted CSS in the chat text)
pasted confirmed clean css code_files\    ← this dump (ChatGPT chrome only)
```

The `_files` folder can be dated 7/24 because that is when the page was saved. That date is **not** an Updraft timestamp.

## Do not send the rest of `_files`

More hashed `.css` from that folder will be the same chrome.

**If the goal is the CSS ChatGPT confirmed:** open the **sibling** `pasted confirmed clean css code.html` (no `_files`) in Notepad++. Search `tc-overlay-card`. If that string is in the chat transcript, send **that one HTML** (or a copy of the CSS block only). That is still a ChatGPT transcript, not the live Customizer, but it can be a dated copy of the rules.

**If the goal is the 7/24 website:** hunt `backup_2026-07-24-1659_The_Truth_Collective_*`. See `diagnostics/FIND-CLEAN-JULY-BACKUPS-ON-CPU-AND-USB-2026-10-12.md`.
