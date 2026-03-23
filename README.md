# Milky Way Language (MWL) - Introduction
For readers under a night sky: humans, other space‑faring species, and camera‑equipped AIs. 

> **Core idea:** A pictographic script built from astronomical phenomena. Clauses are compact. Time is **vertical** (future ↓ , past ↑) on the page, line by line. Direct causality is laid out with a dedicated linker between lines.
> 
> In the script, **layout** conveys meaning-**not punctuation**. 
> 
> **Purpose:** Tell **adventure fiction** using **shared celestial referents**.  


MWL Samples: 
* [Star Wars 4 crawl in MWL](https://alex987654.github.io/MWL/Star-Wars-4-Crawl-in-MWL.html)
* [“The Twin Exodus” sample story](https://alex987654.github.io/MWL/The-Twin-Exodus-MWL-Sample.html)

Authoring Tool for MWL: 
* [MWL Story Constellator](https://alex987654.github.io/MWL/MWL-Story-Constellator.html)

Number Glyphs for MWL: 
* [Number Generator](https://alex987654.github.io/MWL/MWL-Numeral-Generator.html)

Symbol Definitions demo page: 
* [Symbol defs](https://alex987654.github.io/MWL/MWL-symbol-defs/demo.html)


## What This Experimental Language Is

- **Audience:** Readers who can view the night sky, space-faring beings, including AIs with cameras, who are familiar with the night sky on planetary surfaces or in space. Pages are meant to be legible by eye or camera without requiring spoken language. 
- **Purpose:** Tell stories using mostly **astronomical icons** as a shared reference.  
- **Design constraints:**  
  - Minimal **grammar**: very few glyphs per clause; up to one descriptive and one numeral **qualifier**.  
  - **Minimal grammar, maximal iconics**
  - **No tense** morphology; use the time arrow encoded in the vertical axis, and use Doppler effect - grounded **CAUSE-THEN** to express a causal relationship.
  - **Legibility:** Uniform **on‑rail** layout (single baseline), few metas, and **determinatives** for categories unrelated to astronomical phenomena (e.g., emotions).

## How the Script Works

- **Glyph categories:**
  - **Objects/Events** (physical things): stars, planets, eclipses, supernova, black hole, quasar, etc.  
  - **Properties/Adverbs** (qualities & manner): outside/inside, converging/diverging, shrinking/expanding, above/below, etc.  
  - **Verbs/Kinematics**: rise, set, accelerate, capture, approach, etc.  
  - **Meta/Discourse**: direction, scale, cause-then (Doppler), proper name (aka proper-name-cartouche / PNC aka photo glyph), emotion marker.  
  - **Emotions**: fear, anger, joy, sadness, surprise, disgust, hope, courage, love, betrayal.
  - **Convertible glyphs**: a curated subset may act as **head or verb** (e.g., `WANDER` ⇄ `PATH`)
- **Linkers and frames:** **cause-then** for temporal/causal flow; **signal/dialog** for dialog; **scale/level** for spatial scale and spatial reference frame.
- **Everything is on-rail**
  - **Uniform look:** All glyphs share the same baseline, size, and stroke. No stacking, no superscripts, no edge ornaments.
  - Do **not** stack two clauses on one line.
  - **Clause grid:** Each **content line** is exactly **one clause**. Except for nominal clauses, it is laid on a **three-slot rail** with two conceptual gutters:
    - **Left Head** | **Verb (center, exclusive)** | **Right Head**
  - **One verb per clause:** The **center slot** may contain exactly **one** token from **{VERB ∪ ConvertibleGlyph}**. Heads sit on the side slots (also **{HEAD ∪ ConvertibleGlyph}**).
- **Spatial reference** and **Temporal order**
  - **Scale:** frame line starts with `• [scale object level object level …]` (scale is hierarchical and gets spatially smaller with each level, e.g. local galaxy … spiral arm …) within story. No verbs allowed in line, only objects; sets spatial frame/anchor.
  - **Temporal order is vertical**, the next content line is **later** (future = DOWN) unless it is a frame or linker line. 
  - **Linker line:** `[cause-then]` alone between two content lines to assert **causal** order.
- **Clause types**
  - **Verbal Clause (default):** has a **center** nucleus (verb or CG-as-verb), expressing action/change/process. Example:  
    `[⟦LUMEN⟧ + star-ship]   [approach]   [planet]`
    - **Location or positional presence** is expressed using this clause type, by leveraging the verb `[linger]`. 
  - **Typing / Membership Clause:** center is **`[is-type]`**. A **non-verbal** clause establishing **class membership** or **type identity**. **`[is-type]`** establishes a strong force linking objects or proper names. Examples:  
    `[signal] [is-type] [PATH MOD constructed]`  
    `[⟦WANDERER⟧ + star-ship] [is-type] [constructed]`
    `[star-ship] [is-type] [⟦REBEL‑ALLIANCE⟧]`
  - **Relational Clause:** center is **`[is-related-to]`**. A **non-verbal** clause establishing **association**. **`[is-related-to]`** establishes a weak force linking objects or proper names. Examples:  
    `⟦PNC Leia⟧ [is-related] [⟦REBEL‑ALLIANCE⟧]` 
    `[signal] [is-related] [pulsar-beacon]`
  - **Nominal Clause (mono/state assertion):** A **non-verbal** clause, describing state/attribute/quantity of a single head using **MOD**. MOD modifies or qualifies the **internal state** of a head. Example:  
    `[gas-giant MOD magnetosphere]`  or  `[star-ship MOD dimming MOD three]`
    - **AG** is not used in nominal clauses (no action/roles).
- **Convertible glyphs (CGs)**
  - A curated subset may act as **head or verb** (e.g., `WANDER` ⇄ `PATH`) **or qualifier**.
  - **Slot casting by position:** Center = **verb role**, sides = **head role**.
  - **Constraints (to avoid ambiguity):**
    - **No single-glyph content lines** with CGs (force context).
    - **No CG qualifies its paired form.**     
    - Use **AG** whenever both heads could plausibly be agents (see below).
- **Agents and roles (use of agent AG meta glyph)**
  - **Default:** Agent = **left head** on a **verbal clause**.
  - **AG meta (with MOD) is authoritative:**
    - **Mark a head:** `[HEAD MOD AG]` → this head is the **agent**, regardless of side.
    - **Ellipsis:** `[VERB MOD AG] [HEAD]` → agent **carries over** from the **previous content line** in the same frame.
  - **Use AG when:**
    1) **CG verbs** appear between **capable heads** (two star-ships).
    2) **Symmetric verbs** (join/converge/diverge/crossing paths) when initiation matters.
    3) **Agent-right** or **focus inversions**.
    4) **Ellipsis** (agent omitted).
  - **Validation:** At most **one** head may bear `MOD AG` per content line. 
- **Qualifiers on heads vs verbs**
  - **Binder:** `MOD` (only). It binds the **next glyph** as a modifier of the **previous target**.
  - **Head budget (per head):** **1 descriptive qualifier + 1 numeric qualifier**.
    - Descriptive: property/state (`constructed`, `dimming`), spatial (`near/far/above/below`, `outside`), emotion (`[hope] EMOTION`), convertible glyphs if used as property
    - *`MOD FALSE`* on a head is considered a descriptive qualifier
    - *`MOD AG`* on a head is a qualifier but does not consume budget
    - Numeric: binary numeral glyphs (see Numbers).
- **Verb budget (per verb nucleus):** **1 descriptive + 1 numeric**.
  - Descriptive: **first/next/last**, **emotion stance**, **FALSE** (polarity), **MAYBE**.  
  - *`MOD FALSE`* on a verb is considered a descriptive qualifier
  - *`MOD AG`* on a verb is considered a descriptive qualifier
  - Meaning of numerals on verbs: frequency/iteration.
- **Order in a chain (readability convention):**
  - `…  MOD [descriptive]  (MOD [number])  (MOD AG on head if agent)`
  - For emotions: `… MOD [anger] EMOTION` (EMOTION determinative immediately after the emotion glyph).
  - For negation of a **qualifier**, place `MOD FALSE` **after** that qualifier.
- `OUTSIDE` is legal only after an **SCALE** line.
- **Metas and linkers you will see**
  - **SCALE  / LEVEL (>)** - use to determine the spatial theater of action in content lines below SCALE. With each use of LEVEL, the spatial scale get smaller. Frame line forms:  
    - Canonical: `• [scale object > ⟦TARGET⟧]`  
    - Shorthand: `• [scale ⟦TARGET⟧]` (LEVEL inferred or inherited within story)
    - Example:    `[scale] [local galaxy] [level] [nebula]` where nebula may be a proper name of type nebula.
  - **CAUSE-THEN** - line-level linker (Doppler visual, direction of motion vertical, future down). Place **between** two cause/effect content lines.
  - **TRUE / FALSE:** expressed through meta `[true]` (100% likelihood, visually RGB 255,255,255), used in dialog (affirmative responses to questions). Negation is expressed through meta `[FALSE]` (0% likelihood, RGB 0,0,0). Uncertain/maybe is visually a gray meta glyph and expressed through `[UNCERTAIN]`. To negate a head or verb, use `MOD FALSE`. This occupies the **descriptive** slot for that head or verb.
  - **Determinatives (postfix, zero-budget):**  
    - **EMOTION** - follows an **emotion glyph**; aids non-human parsing to distinguish emotions from other glyphs: `… [anger] EMOTION`.  
    - **DIALOG** - used to indicate dialog (questions and answers) and follows an **utterance head** in dialog: `… [UTTERANCE …] DIALOG` (question/answer context).
- **Ordered lists without numerals (use FIRST / NEXT / LAST)**
  - Ordinals are **lexical metas**, not numbers. Attach via `MOD`:
    - `[WAYPOINT] MOD [FIRST]` - “foremost”
    - `[WAYPOINT] MOD [NEXT]`  - “next in sequence”
    - `[WAYPOINT] MOD [LAST]`  - “final in sequence”
  - These consume the **descriptive** slot on their target. 

## Reading Direction & Page Layout

- **Reading direction:** A story begins with the **direction** meta glyph (horizontal pointer reminiscent of a compass) to define reading direction on a page.
- **Horizontal reading:** **Left → Right** within a line. 
- **Arrow of time:** **Time is vertical, i.e. it is orthogonal** to the pointer shown in the **direction meta glyph:** **Future is DOWN (↓)** and **Past is UP (↑)** on pages, always.  **New line = later**, always in the **narrator’s proper time** (future is **down**).  
  The **CAUSE‑THEN** linker lives on a **separate line** between cause (content line above) and effect (content line below). 
- **Contextual existence:** Existence is assumed (zero-marked) by the narrator whenever and as soon as an entity is introduced with a glyph in a content line. 
  - Exception: an object is introduced in a content line solely to express that it does not exist.  (`object mod FALSE`)
- **Planetary surface:** the **planetary surface** glyph must appear before **above/below**; these properties read relative to last used planetary surface glyph.
- **Spatial scales (SCALE and LEVEL glyphs):**
  - **Canonical:** `• [scale object level ⟦TARGET⟧]`
    - E.g. `[scale] [local galaxy] [level] [nebula]`
  - **Anchored shorthand:** `• [scale ⟦TARGET⟧]` - LEVEL is **inferred** from target type or **inherited** from the previous frame.  
  - **Use one or more explicit LEVEL** (e.g. nebula or star system or a proper noun of type nebula or star system) for ambiguous anchors (e.g., **star-ship**), **to approximate spatial size** (e.g., `level [small moon] level ⟦DEATH‑STAR⟧`), and **event anchors** (add **linger** as modifier to stabilize).  
- **End of a sentence:** Two sentences must be in separate lines. 

## Grammar Essentials

### Clause Shapes

1) **Mono (property on a head; optional count)**  
   ```
   [HEAD]  MOD [descriptive]  (MOD [number])
   ```
   - **Budget (per target):** **1 descriptive + 1 numeric** max. Descriptive includes property/state/spatial/orientation/emotion‑typed property. Determinatives don’t count towards budget. 

2) **Dyad (two heads and a verb; each side may have its own modifiers)**  
   ```
   [HEAD₁  (MOD …)]   [VERB  (MOD descriptive) (MOD number)]   [HEAD₂  (MOD …)]
   ```
   - **Agent default:** **left head**.  
   - **Disambiguate with AG** when ambiguous, inverted, or ellipsis:
     - `[HEAD₁ MOD AG] [VERB] [HEAD₂]` (mark left explicitly)
     - `[HEAD₁] [VERB] [HEAD₂ MOD AG]` (agent‑right)
     - `[VERB MOD AG] [HEAD]` (agent carries over; no agent head shown)
   - AG does not count towards the descriptive or number MOD budget.

3) **Typing Clause - identity/class**
   ```
   [X]  [is-type]  [Y (MOD property)]
   ```
   - Class membership and identity. **Negation**: `[is-type MOD FALSE]`.

4) **Relational Clause** **-  belonging/association** 
   ```
   [X]  [is-related-to]  [Y (MOD property)]
   ```
   - Belonging, provenance, or association, somewhat similar to English “of”. **Negation**: `[is-related-to MOD FALSE]`. Weaker than `[is-type]`.

5) **Causal linkage (line‑level)**  
   ```
   [CAUSE line]
   [cause‑then]
   [EFFECT line]
   ```
   Negate effects by negating the **effect verb** (see FALSE).

> **Important:** **Qualifiers never occupy their own separate rail slot**; they attach to a head or verb using **MOD**. PNC (proper names) never take qualifiers. 

---

### Temporal Framing

- **Vertical axis encodes the narrator’s proper time.** Each new line advances time.  
- MWL must be written in the **narrator’s reference frame**. 
- **CAUSE‑THEN** sits alone between two lines to enforce **order and implication** without tense morphology.  
- Use **pulsar + SIGNAL** as a metronome when needed; numeric frequency attaches to verb via MOD.

---

### Convertible Glyphs

A small subset of glyphs may appear as **head** or **verb** (e.g., **WANDER** (verb) vs **WANDER as PATH** (head)). **Position** casts role as **head vs verb**; **MOD-docking** determines a **qualifier** and is allowed for CG when the CG is used as a property. 

**Rules to keep pages unambiguous:**  
- **Position casts role:** center = **verb**, sides = **head**.  
- **Convertible glyphs gain qualifier status only when preceded via MOD.** They cannot function as qualifiers by adjacency alone. 
- **No single‑glyph clauses** with CGs (force context).  
- **No CG qualifies its paired form** (e.g. WANDER cannot qualify PATH).  
- Use **AG** whenever two capable heads could be agents, you invert roles, or you elide the agent.

**Examples:**  
- Verb: `[star-ship]  [wander]  [spiral arm]`  
- Head: `[path]  MOD [constructed]` 

**Table of Convertible Glyphs:** 

| Name of Glyph | Primary Role | Secondary Role       | Tertiary Role                     |
|---------------|--------------|----------------------|-----------------------------------|
| increase      | meta         | property: increasing |                                   |
| decrease      | meta         | property: decreasing |                                   |
| spiral        | verb         | object: spiral arm   |                                   |
| orbit         | meta         | verb: linger         |                                   |
| wander        | verb         | meta: path           |                                   |
| dimming       | property     | verb: fade           | meta: low-energy, <br>depletion   |
| bright        | property     | verb: glow           | meta: high-energy, <br>saturation |
| expanding     | property     | verb: expand         |                                   |
| shrinking     | property     | verb: shrink         |                                   |
| constructed   | property     | verb: construct      |                                   |
| destroyed     | property     | verb: destroy        |                                   |
| signal        | verb         | meta: message        |                                   |
| gate          | meta         | verb: cross          |                                   |

---

### Paratactic clause chaining

Beyond a small number of meta glyphs, relations such as “for”, “and”, “but”, “about”, or non-spatial use of “at/to” in cognitive, evaluative or emotional clauses are expressed through **paratactic clause chaining**: a sequence of clauses placed in direct adjacency, in which **order and proximity infer meaning in MWL**. The first clause establishes the **setting** (where necessary, e.g. to describe a place to launch from in `ascend to`) or defines a type or relationship, the second clause establishes the **topic or action** (≈ “about” / topic), the third and fourth express the **more details or the conceptual state or the target or the consequence**. Interpretation arises from **proximity and clausal alignment**. 
Clause order should - where applicable - match the idea that time is vertical in MWL. 
Parataxis should only be used where preferable over the use of `MOD`, `is-type`, `is-related-to`, or `because-then`.

**Example:**  
- [star-ship] [is-type] [⟦EMPIRE⟧]
- ⟦PNC Vader⟧ [is-related] [⟦star-ship⟧]
- [star-ship] [mod] [destroyed]
- [cause-then]
- ⟦PNC Vader⟧ [mod] [angry] [EMOTION] [signal]
- ⟦PNC Leia⟧ [mod] [joy] [EMOTION]

---

### Yes/No

Use the **TRUE/FALSE/UNCERTAIN** metas for certainty or dialog cues. For negation, attach `FALSE` with **MOD** to the **target** you negate:
- Verb: `[approach MOD FALSE] [station]` → “does **not** approach”
- Qualifier: `[approach MOD FROM OUTSIDE MOD FALSE] …` → “approaches, but **not** from outside”
- Property on head: `[gas-giant MOD magnetosphere MOD FALSE]`
- Existence: `[PATH MOD FALSE]` → “no path”

**Note:** `MOD FALSE` on a verb occupies the verb’s **descriptive** slot for that clause.

---

## Using Proper Nouns with PNC (Proper‑Name Cartouche)

**What the PNC glyph does:** wraps a head with a **name** (color or b/w photo; alien rune; icon). It **names**, it does **not type**. Use a **typing clause** to type/classify. Generally every PNC should be typed with `is-type` first before it is used in MWL.

### Core rules
- **No MOD for initial typing on PNC:**  
  `[⟦WANDERER⟧] [is-type] [star-ship MOD constructed MOD interstellar]` ✅  
  `[⟦WANDERER⟧ MOD star-ship]` ❌
- **First mention:** use an initial, explicit typing clause for readability.  
  After that, a bare PNC (`[⟦WANDERER⟧]`) can stand as the **head anchor**.
- **Qualifiers after typing:** you may attach qualifiers to later PNC mentions; they apply to the **typed entity**:  
  `[⟦WANDERER⟧] [drift MOD dimming] [⟦GOLDEN-STAR⟧]`
- **Negation:** don’t negate the PNC. Negate the **relation**:  
  `[⟦WANDERER⟧] [is-related-to MOD FALSE] [⟦EMPIRE⟧]`

Proper Name Glyph Maker for MWL: 
* [Proper Name Glyphs](https://alex987654.github.io/MWL/MWL-Proper-Name-Glyph-Maker.html)

---

## Dialog in MWL: Signal–Dialog/Echo

**Goal:** binary or ternary dialog readable by sensors; express boolean questions/answers without punctuation, with robust Q↔A matching over long distances.

### Syntax
* Center verb: signal.
* Utterance head: the topic or phrase.
* Determinative: DIALOG postfix (no budget).
* Responses/Polarity: attach exactly one of [true], [false], [uncertain] before DIALOG.

### Building blocks
- **`[signal]` is a verb** (center) for sending signals without information content, for transmitting messages, and for simple dialog (yes/no questions and responses).
- **`DIALOG` is strictly a *dialog determinative***. It is placed **after** the **utterance head** (postfix) in the question transmitted. Very much like an EMOTION determinative, **DIALOG does not consume budget**.
- **Answer polarity:** attach exactly one of **`[true]`**, `[false]`, or **`[uncertain]`** to the **utterance head** **before** `DIALOG`. 
- **Agent (optional):** mark the **speaker** with `MOD AG` if needed.
- **Matching utterance:** the **utterance head tokens** in the response **must match** the question’s utterance exactly, so question/answer pairs can be unambiguously linked.

### Patterns

**Yes/No Question (one clause):**
```
[⟦SPEAKER⟧ MOD AG]   [signal]   [UTTERANCE  DIALOG]
```
> Presence of postfix `DIALOG` **without** polarity marks this as a **question**.

**Answer (one clause):**
```
[⟦RESPONDER⟧ MOD AG]   [signal]   [UTTERANCE  [TRUE]    DIALOG]   // YES
[⟦RESPONDER⟧ MOD AG]   [signal]   [UTTERANCE  [FALSE] DIALOG]   // NO
[⟦RESPONDER⟧ MOD AG]   [signal]   [UTTERANCE  [UNCERTAIN] DIALOG]   // MAYBE / UNKNOWN
```
> Use exactly **one** of `yes` / `no` / `uncertain`. Do **not** combine them.
> `DIALOG` is determinative (no budget cost). 

**Emotion on the act of speaking (stance):**
```
[⟦LEADER⟧ MOD AG]   [signal MOD courage EMOTION]   [UTTERANCE DIALOG]
```

### Validator notes
- One clause per line; **`signal` is the center verb**.
- **Question:** postfix `DIALOG` on the utterance **without** yes/no/uncertain.
- **Answer:** the **same utterance head** plus exactly one of `yes` / `no` / `uncertain`, then postfix `DIALOG`.
- **Budgets:** `DIALOG` is a **determinative** and does **not** consume budget. `yes/no/uncertain` attach in front of the determinative and don’t consume budget.
- **Do not** put `FALSE` on `signal` for “No”-that would negate the act of speaking, not the answer’s polarity.

---
## Measurements with DISTANCE‑TIME (H‑hyperfine)

Use the **H-hyperfine transition** (21 cm wavelength / its period) as a shared **ruler/clock**. Combine with **x10** and **/10** shifter glyphs and binary numerals to express **distances** and **durations** compactly.

### Measurement Pack (MP)
A measurement is a **single descriptive qualifier** that attaches via `MOD` to a **verb** or **head**:

```
MP := [DISTANCE‑TIME  MOD <mantissa-number>  (MOD x10 MOD <k>)  (MOD /10 MOD <j>)]
// Value = (mantissa) × 10^(k) × (H-hyperfine λ for length, H-hyperfine period for time)
// Value = (mantissa) × 10^(−j) × (H-hyperfine λ for length, H-hyperfine period for time)
```

- **Mantissa-number:** any MWL numeral (binary positional).  
- Use **either** **x10 or /10:** takes its **own exponent numeral** (attached via MOD).  
- **Budget:** the **MP** as a whole consumes **one descriptive slot** on its **target**; numerals inside the MP do **not** consume the target’s numeric slot.

### Choosing dimension (length vs time)
- Attach MP to a **PATH**, corridor, or **motion verb** (e.g. **drift/accelerate**…) → interprets as **distance/length**.  
- Attach MP to **linger/message** (aspect) → interprets as **duration/time**.

### Examples
- **Distance along a route:**  
  `[⟦WANDERER⟧ MOD AG]  [wander]  [PATH  MOD [DISTANCE‑TIME MOD five MOD x10 MOD eleven]]`

- **Duration of thrust:**  
  `[⟦WANDERER⟧ MOD AG]  [accelerate MOD [DISTANCE‑TIME MOD one MOD x10 MOD eight]]`

- **Fine scale:**  
  `[PATH  MOD [DISTANCE‑TIME MOD seven MOD /10 MOD one]]`

### Validator
- MP is **one** descriptive qualifier on its target.  
- Inside MP: order is `mantissa → (x10)` or `mantissa → (/10)`; parser follows MOD chains.  
- Dimension is determined solely by **where the MP attaches**.  

---

## Numbers / Numerals (Binary Positional)

MWL numerals are **pictographic** and **binary‑based** to aid machine readers while remaining iconic.

- **Glyph anatomy:**
  - **Binary rail:** a horizontal baseline with **bit cells**; **set bits** are drawn as vertical bars **below** the rail.
  - **Weight ticks:** small ticks **above** the rail that **increase in height right→left** (cueing 2,4,8, …).
  - **Least significant bit (LSB) is on the right in binary rail in MWL numeral glyphs**.
  - **2–8 use a ring-with-dots determinative** (count dots inside a circle); **≥9 omit the dot ring** and rely on the rail only.
- **Singular**: unmarked
- **Zero**: expressed through FALSE.
- **Attachment (with MOD):**
  - **On verbs:** frequency/iteration - `[message MOD three]`, `[approach MOD two]`
  - **On heads:** count or cardinality - `[star-ship MOD four]`
  - **Inside a Measurement Pack:** when a numeral **follows `x10` or `/10`**, it is an **exponent** (10^(+n) or 10^(−n)) on the **DISTANCE‑TIME** base; these exponents belong to the **MP** and **do not** consume the target’s numeric slot.
- **Budget:** numerals consume the single **numeric** slot for that target (you may still have one **descriptive**) - *except* when they are **internal to an MP** (see above).

Create Number Glyphs for MWL: 
* [Number Generator](https://alex987654.github.io/MWL/MWL-Numeral-Generator.html)

---

## Morphology & Diacritics (Meta Practices)

- **MOD (binder):** linear operator; **binds the next glyph** as a modifier of the previous. Max **two** per target: **1 descriptive + 1 numeric**.
- **AG (agent role):** used **with MOD**:
  - Mark a head: `[HEAD MOD AG]` (agent‑left explicit or agent‑right when attached to the right head)
  - Ellipsis: `[VERB MOD AG]` (carry over previous agent)
  - **AG** is a **role marker**, not a qualifier; it does **not** consume the descriptive/numeric budget.
- **Determinatives (postfix, zero-budget):**  
  - **EMOTION:** follows an **emotion glyph** immediately: `… [anger] EMOTION`.  
  - **DIALOG:** follows the **utterance head** in dialog: `… [UTTERANCE …] DIALOG`.
- **EMOTION determinative** follows an **emotion glyph** immediately: `… MOD [anger] EMOTION`. It flags the category for parsers; **optional** and **non‑semantic**.
  - **Scope by attachment point:** on **verb** = clause stance; on **head** = local feeling.
- **DIALOG** **is a determinative** on an **utterance head**, use for dialog (Yes/No questions and answers)

- **Orthographic morphology - the gray MWL frame**
  * **What it is:** a neutral gray rectangle around **every glyph** that signals “this is an MWL glyph” and disambiguates it from background pixels or other scripts.
  * **Geometry (scales with size):** outer margin = **8–10%**; stroke = **1.5–2.0%**; corner radius = **3–4%** (square corners allowed); color = **#949698 / rgb(148,150,152)**.
  * **Two variants:**
    * **Regular frame (default):** used for all standard glyphs (e.g., **SCALE**).
    * **Meta‑only frame (wider):** rectangle itself **carries the meaning** for **YES / NO / UNCERTAIN**; inner area is a **uniform fill** (no icon strokes).

- **Probability metas - YES / NO / UNCERTAIN (grayscale tiles)**
  * **Render:**
    * **TRUE** = white fill **rgb(255,255,255)**
    * **FALSE** = black fill **rgb(0,0,0)**
    * **UNCERTAIN** = mid gray **rgb**  #2D2D2D / rgb(45,45,45)
  * **Dialog usage:** attach **behind the UTTERANCE head** **right before** DIALOG. DIALOG is **determinative** (zero‑budget). 

- **Frames, planes, and linkers**
  * **SCALE** is a **frame‑setter on its own line**; **anchored shorthand** is allowed (omit **LEVEL** when inferable/inheritable):
    * Canonical: • [scale > LEVEL > ⟦TARGET⟧]
    * Shorthand: • [scale > ⟦TARGET⟧] 
    * Use **explicit LEVEL** for ambiguous anchors (e.g., a **star-ship**) or interiors;
  * **OUTSIDE/INSIDE**, **NEAR/FAR**, **CENTERED/OFF-CENTERED** is **legal only after** an anchored **SCALE** (or when a local **PLANE** is set), and it refers to the most recent SCALE line.
  * **ABOVE/BELOW** is **legal only after** a **planetary surface** is introduced. 
  * **CAUSE‑THEN**: a **line‑level linker** placed **between** cause and effect lines; negate outcomes by **negating the effect verb**.


---

## Ordering Without Numerals (FIRST / NEXT / LAST)

To describe sequence positions without reusing numerals:

- Use **FIRST**, **NEXT**, **LAST** as **meta ordinals** (distinct from numbers).  
- Attach via **MOD** to the item they qualify:
  - `[WAYPOINT] MOD [FIRST]`
  - `[WAYPOINT] MOD [NEXT]`
  - `[WAYPOINT] MOD [LAST]`
- These are lexemes of order (like ancient “foremost/next/last”), not counts; they occupy the **descriptive** slot on their target.

---

## Authoring Heuristics

- Keep clauses **short** (preferably 2–8 glyphs). 
- One clause per content line. 
- Keep sufficient and consistent spacing between content lines, and use a new line control character at the end of a content line.
- Treat **verbs as clause nuclei**: attach stance, emotion, uncertainty/negation there to mean the whole proposition.
- Use **AG** when roles are ambiguous, inverted, or omitted. Exception: leave out **AG** if you want to intentionally keep ambiguous.
- Express related clauses through paratactic clause chaining, focus on proximity first, use clause order only where temporally or causally or physically applicable.
- **Convertible glyphs:** rely on **position casting** and MOD for properties/qualifiers; avoid CG self‑qualification.
- Reserve **CAUSE‑THEN** for real causality, not mere sequence (for that, use **FIRST/NEXT/LAST** or a new line).

## Lexicon Of Glyphs

### Objects
Astronomical objects, examples: Stars, planets, and celestial structures: single star, black hole, binary star, nebula, star field
### Events
Transient phenomena, examples: supernova, eclipse, aurora, asteroid impact
### Verbs / Kinematics
Motion, change, and interaction, examples: rise, set, accelerate, drift, wander, capture, join, diverge
### Properties / States
Spatial or qualitative, examples: bright, near, outside, shrinking, constructed, interstellar
### Meta / Discourse
Functional symbols, examples: scale, plane, cause‑then, direction, true, false, uncertain, mod, first, next, last
### Emotions
Examples: fear, anger, joy, hope, love, betrayal, etc.
### Numerals
Binary‑positional; 2–8 use **ring‑with‑dots**; ≥9 use **rail only**.

### **Full list:**

1. single star
2. constellation
3. black hole
4. small moon
5. partial moon
6. twin moons
7. planetary surface
8. bright comet
9. dark comet
10. pulsar beacon
11. quasar
12. dark rift
13. star-ship
14. local galaxy (displayed as Milky Way band)
15. other galaxy
16. gas-giant
17. binary star
18. rocky planet
19. Earth-like planet
20. asteroid belt
21. nebula
22. star system
23. star field (many stars)
24. supernova
25. star birth
26. planetary transit
27. total solar eclipse
28. partial solar eclipse
29. asteroid impact
30. comet strike
31. aurora
32. rise
33. set
34. accelerate
35. decelerate
36. drift
37. fall
38. ascend (depart) to
39. spiral (spiral arm)
40. hide
41. reveal
42. join together
43. split apart
44. approach (descend, land)
45. wander (path)
46. capture
47. crossing paths
48. diverging paths
49. converging paths
50. dimming (low on energy)
51. bright (white glowing, strong on energy)
52. above
53. below
54. near
55. far
56. centered
57. off-center
58. enclosed (inside)
59. outside of
60. expanding
61. shrinking
62. constructed (construct)
63. destroyed (destroy)
64. ocean world
65. magnetosphere
66. interstellar
67. signal
68. document
69. life
70. gate
71. orbit (rotation, linger)
72. direction (compass)
73. scale
74. cause-then (Doppler shift, causal flow)
75. level (spatial order of magnitude)
76. dialog marker
77. emotion marker
78. proper name cartouche
79. divide by ten
80. multiply by ten
81. distance-time (H hyperfine transition)
82. true (yes)
83. false (no)
84. uncertain (maybe)
85. mod (modifier, qualifier)
86. is-type
87. is-related-to
88. first
89. next
90. last
91. increase
92. decrease
93. fear
94. anger
95. joy
96. sadness
97. surprise
98. disgust
99. hope
100. courage
101. love
102. betrayal
103. two
104. three
105. four
106. five
107. six
108. seven
109. eight

| Name of Glyph         | Primary Role | Semantic Notes                   |
|-----------------------|--------------|----------------------------------|
| single star           | object       |                                  |
| constellation         | object       |                                  |
| black hole            | object       |                                  |
| small moon            | object       |                                  |
| partial moon          | object       |                                  |
| twin moons            | object       |                                  |
| planetary surface     | object       |                                  |
| bright comet          | object       |                                  |
| dark comet            | object       |                                  |
| pulsar beacon         | object       |                                  |
| quasar                | object       |                                  |
| dark rift             | object       |                                  |
| star-ship             | object       | star-ship in space               |
| local galaxy          | object       | Milky Way band                   |
| other galaxy          | object       |                                  |
| gas-giant             | object       |                                  |
| binary star           | object       |                                  |
| rocky planet          | object       |                                  |
| Earth-like planet     | object       |                                  |
| asteroid belt         | object       |                                  |
| nebula                | object       |                                  |
| star system           | object       |                                  |
| star field            | object       |                                  |
| supernova             | event        |                                  |
| star birth            | event        | protostar                        |
| planetary transit     | event        |                                  |
| total solar eclipse   | event        |                                  |
| partial solar eclipse | event        |                                  |
| asteroid impact       | event        |                                  |
| comet strike          | event        |                                  |
| aurora                | event        |                                  |
| rise                  | verb         |                                  |
| set                   | verb         |                                  |
| accelerate            | verb         |                                  |
| decelerate            | verb         |                                  |
| drift                 | verb         |                                  |
| fall                  | verb         |                                  |
| ascend to             | verb         | depart                           |
| spiral                | verb         |                                  |
| hide                  | verb         |                                  |
| reveal                | verb         |                                  |
| join together         | verb         |                                  |
| split apart           | verb         |                                  |
| approach              | verb         | descend, land                    |
| wander                | verb         |                                  |
| capture               | verb         |                                  |
| crossing paths        | verb         |                                  |
| diverging paths       | verb         |                                  |
| converging paths      | verb         |                                  |
| dimming               | property     | low on energy                    |
| bright                | property     | strong on energy                 |
| above                 | property     |                                  |
| below                 | property     |                                  |
| near                  | property     |                                  |
| far                   | property     |                                  |
| centered              | property     |                                  |
| off-center            | property     |                                  |
| enclosed              | property     | inside, hidden                   |
| outside               | property     | in the open                      |
| expanding             | property     |                                  |
| shrinking             | property     |                                  |
| constructed           | property     |                                  |
| destroyed             | property     |                                  |
| ocean world           | property     |                                  |
| magnetosphere         | property     |                                  |
| interstellar          | property     |                                  |
| signal                | meta         |                                  |
| document              | meta         | information                      |
| life                  | meta         |                                  |
| gate                  | meta         |                                  |
| orbit                 | meta         |                                  |
| direction             | meta         | compass style glyph              |
| scale                 | meta         |                                  |
| cause-then            | meta         | Doppler shift, <br>causal flow   |
| level                 | meta         | spatial order of<br>magnitude    |
| dialog                | meta         | echo style glyph                 |
| emotion               | meta         |                                  |
| proper name           | meta         |                                  |
| divide by ten         | meta         |                                  |
| multiply by ten       | meta         |                                  |
| distance-time         | meta         | H hyperfine <br>transition glyph |
| true                  | meta         |                                  |
| false                 | meta         |                                  |
| uncertain             | meta         | maybe                            |
| mod (modifier)        | meta         | qualifier                        |
| is type               | meta         |                                  |
| is related to         | meta         |                                  |
| first                 | meta         |                                  |
| next                  | meta         |                                  |
| last                  | meta         |                                  |
| increase              | meta         |                                  |
| decrease              | meta         |                                  |
| fear                  | emotion      |                                  |
| anger                 | emotion      |                                  |
| joy                   | emotion      |                                  |
| sadness               | emotion      |                                  |
| surprise              | emotion      |                                  |
| disgust               | emotion      |                                  |
| hope                  | emotion      |                                  |
| courage               | emotion      |                                  |
| love                  | emotion      |                                  |
| betrayal              | emotion      |                                  |
| 2                     | numeral      |                                  |
| 3                     | numeral      |                                  |
| 4                     | numeral      |                                  |
| 5                     | numeral      |                                  |
| 6                     | numeral      |                                  |
| 7                     | numeral      |                                  |
| 8                     | numeral      |                                  |
---


*End of introduction.*
