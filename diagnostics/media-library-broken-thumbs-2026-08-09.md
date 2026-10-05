# Media Library broken thumbnails (2026-08-09)

**Symptom (Daniel):** All rows in Media Library list show broken file icons; Imagify column says **Invalid API key**.

## Diagnosis
1. **Not mainly Imagify.** Invalid API key is real but separate. It does not explain missing files.
2. **Library DB entries exist (~2289); many newest files are gone from disk.**  
   Sample of newest attachments (`uploads/2026/07/…`) → **HTTP 404** for both full file and thumbnail.  
   Older sample (`uploads/2026/06/…`) → many **HTTP 200**.  
   Known Tech Hub tile URLs in June still **200**.
3. Media Library sorts **newest first**, so page 1 looks “all broken” even though older months still have working files.
4. Matches standing recovery note: Jul-era uploads path damage after restores; **do not** Jul 24 full-site restore.

## What to do now (safe)
1. Ignore Imagify for this task (or later: Imagify → Settings → paste valid key / disconnect).  
2. **Upload new** 1600×1000 category images via Add New — new files should land in a current uploads month.  
3. Or search/filter Media for older months that still preview.  
4. Later (Hostinger File Manager): selective restore of missing `wp-content/uploads/2026/07/` only if needed — never Website backup restore / Jul 24 full roulette.

## For Tech Hub tiles
Continue plan: Daniel uploads eight new/cropped **1600×1000** files → Cursor swaps URLs on page 111 via REST.
