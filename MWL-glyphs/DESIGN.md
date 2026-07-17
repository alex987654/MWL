# MWL Glyph Design System

Rules for drawing and editing MWL glyphs. Every glyph must look deliberate and balanced
when seen **on its own**.

## Canvas

- `viewBox="0 0 512 512"`; all artwork inside one group with the standard transform
  `matrix(0.91464078 0 0 0.91464078 21.85196117 21.85196117)` wrapping a 512×512 tile rect.
  (Legacy meta glyphs drawn on a 500×500 rect use
  `matrix(0.93646123 0 0 0.93646123 21.88469185 21.88469185)`, which produces the same
  on-screen tile. `true`/`false`/`uncertain` are special thick-border cards.)
- Tile: `fill="#000"`, `stroke="#949698"`, `stroke-width="3"`. One gray only.
- No `translate(...)` fudge groups — bake offsets into element coordinates.

## Composition

- Subject centered on **(256, 256)**: the content bounding box center within ~10 px of it,
  judged by rendered pixel mass, not just geometry (a crescent's mass is not its circle's center).
- Exceptions are **semantic placements only**: horizon scenes (`rise`, `set`, `above`, `below`,
  landscape glyphs), the vertical time axis (`stellar-epoch`, `cosmic-epoch`), and directional
  narratives (`capture`). Numerals share one family grid so digits align across tiles.
- Keep elements ≥ 24 px inside the tile border (ambient dot stars included).
- Mirror pairs must be exact reflections sharing all coordinates:
  `rise`/`set`, `above`/`below`, `increase`/`decrease`, `near`/`far`,
  `converging`/`diverging-paths`, `expanding`/`shrinking`, `multiply`/`divide-by-10`,
  `accelerate`/`decelerate`.

## Size & stroke tokens

- Body radii: **dot 9 · S 28 · M 40 · L 56 · XL 70**. A glyph's primary subject is ≥ S.
- Stroke widths: **3 (tile) · 6 (detail/body outline) · 10 (standard line) · 14 (ring) · 24 (hero bar/arc)**.
- Opacity: **0.95** body strokes · **0.85** secondary lines & arrows · **0.35** ghost/echo elements.
- Dashed rings: family radii **104 / 160**, `stroke-dasharray="27.1 23.1"` (whole periods),
  stroke 14 (see `expanding`, `shrinking`, `supernova`, `orbit` at r 136).

## Arrowheads

One shape: solid isosceles triangle, `fill-opacity="0.85"`, aligned to its line's axis.
- Standard: length 24, half-base 14 (ring/motion glyphs).
- Small: length 18, half-base 10 (compact markers, e.g. `near`).
Shafts are solid or dashed lines at stroke 10 (6 for faint echoes).

## Color

- Tile border gray: `#949698` everywhere.
- Star gold: fill `#ffc63d`, stroke `#fff7bf`; gold radial gradient stops
  `#fff → #ffe57f → #ffbf00` (see `rise`/`set`/`above`).
- Warm accent (distance arrows, markers): `#ffd27f`.
- Neutral paths/bodies: `#a2a2a2` (paths), `#d9d9d9` (arrows), `#cbcbcb` (rings).
- "Dim/far" bodies: fill `#6e6e6e`, stroke `#9a9a9a` (never darker — must read on black).
- Emotions keep their chromatic accents (red `#ff3c3c` fear, pinks `#ff6bcd`/`#f98fff` love, …).

## Hygiene

- Gradient/clip ids must be namespaced `<glyph_stem>__RadialN` / `<glyph_stem>__clipN`
  (never `_Radial1`) — glyphs get inlined together in one document.
- After editing glyphs, run `python3 tools/sync-glyphs.py` from the repo root to regenerate
  the sprite (`MWL-symbol-defs/symbol-defs.svg`) and every HTML file embedding the symbol block.
