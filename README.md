# truth-collective
Website files for The Truth Collective

## Snippets

CSS snippets in this repo are meant to be pasted into WordPress
Appearance > Customize > Additional CSS on the staging site only
(tcstaging.truth-collective.com). The live site is frozen.

All CSS here is append only. Do not delete or modify any rules that
already exist in the Customizer when adding a new snippet.

- `css/tc-hero-reveal.css` - Hover driven home page hero. At rest only
  the H1 is visible. On hover the paragraph fades in, then a CSS only
  EXPLORE button (rendered via the Section block's `::after` text and
  `::before` gold arrow) fades in below it. Activated by adding the
  class `tc-hero-reveal` to the hero Section block. Mobile shows all
  elements at rest. See the header comment in the file for details.
