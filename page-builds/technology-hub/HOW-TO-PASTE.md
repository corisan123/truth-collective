# How to paste Technology Hub drop-ins (WordPress)

If the front of the page shows raw tags like `<div class="tc-page...` or one plain sentence and nothing styled, the wrong block was used.

## Use this block only

**Custom HTML**

Not:

- Code
- Paragraph
- Preformatted
- Kadence Advanced Text
- Classic

## Exact steps

1. Edit the existing Computers page  
   (`/technology-hub/computers-digital-devices/`).
2. Delete the failed block that shows raw HTML or a lone sentence.
3. Click **+** → search **`Custom HTML`** → insert that block.
4. In the editor you should see a gray code box (source view), not a normal text paragraph.
5. Open `computers-PASTE-READY.html` in Cursor (or download raw).
6. Select all → copy.
7. Paste into the Custom HTML box.
8. Update / Publish.
9. View the page in a private window and hard refresh.

## Quick editor check

| What you see in the editor | Meaning |
|---|---|
| Gray box with `<div class="tc-page tc-page--computers">` as code | Correct |
| Normal paragraph / formatted words | Wrong block — delete and use Custom HTML |
| Block labeled **Code** | Wrong — that prints source on the front |

## Slug

Do not change the page URL. Paste onto the existing page.
