---
name: paper-review
description: Process a review set of battery papers into structured Obsidian wiki pages (paper notes), then synthesise concept pages. Use when asked to review papers, process a review set, or build wiki concepts.
---

# Paper review: literature extraction

You act as the extraction agent.
The workflow has two phases: **review** (default) and **concept synthesis**
(when the user asks to build wiki concepts, or after a set is complete and the
user wants the wiki updated).

## Phase 1 — Review a set of papers

1. **Find the set** (`review/queue/*.json`). Run:

   ```bash
   python tools/set_info.py <set-file>
   ```

   It prints one JSON line per paper: `doi`, `cell`, `template`, `text_path`,
   `out_path`, `title`, and `done` (output already exists). Skip `done` papers.

2. **Load the question template** from `review/templates/<template>.json`.

3. **For each pending paper**: read the full text at `text_path` completely, then write `out_path` following the OUTPUT SCHEMA
   below. Extraction rules — these exist because the wiki must be trustworthy
   enough to cite in real research:
   - Only extract data explicitly stated in the text; never fill gaps from
     your own battery knowledge, however plausible.
   - If an answer is not in the paper, write exactly "Not explicitly
     discussed." and omit the evidence line.
   - Every answered question gets a verbatim supporting quote (≤ 30 words,
     copied exactly) on an `> Evidence: "..."` line.
   - Pick exactly 3 keywords: specific technical concepts central to the
     paper that other papers will share (e.g. "Incremental Capacity
     Analysis", "SEI growth"), not generic terms like "battery". They become
     `[[wiki links]]`, so consistent naming across papers matters — reuse a
     concept name you already used for another paper when it is the same
     concept.

4. **Verify each file mechanically** (quotes must exist verbatim in the
   source; this is the anti-hallucination backstop):

   ```bash
   python tools/verify_quotes.py <out_path> <text_path>
   ```

   Fix any reported quote by re-reading the passage and copying it exactly.

5. **Report**: papers reviewed / skipped, keywords introduced, and any
   answers you are less confident about.

### OUTPUT SCHEMA (exact shape, one file per paper)

```markdown
---
cell_target: "<cell name with spaces, e.g. Samsung SDI INR18650-25R>"
doi: "https://doi.org/<doi with slashes>"   # full resolver URL so Obsidian renders it clickable
template: "<template name>"
reviewed: "<today ISO date>"
tags:
  - literature_extraction
  - "<keyword-1>"
  - "<keyword-2>"
  - "<keyword-3>"
---

# <Paper Title>

## General Analysis

**Core Thesis:** <2-3 sentence summary of the paper's primary objective regarding the target cell.>

**Methodological Focus**
- Testing Mode: <e.g., Galvanostatic cycling, EIS, Calorimetry>
- Operating Conditions: <e.g., 25 °C, 0.5C charge / 1C discharge>
- Degradation Markers: <e.g., Capacity fade, impedance growth>

## Keyword Context

- [[Keyword 1]]: <1 strictly factual sentence on its role in this paper.>
- [[Keyword 2]]: <1 strictly factual sentence on its role in this paper.>
- [[Keyword 3]]: <1 strictly factual sentence on its role in this paper.>

## <Template Title>

### <Qn>: <Question title>          <- one section per template question

**Answer:** <answer in the template's expected format, or "Not explicitly discussed.">

> Evidence: "<verbatim quote>"       <- omit line when not discussed
```

## Phase 2 — Concept synthesis (wiki builder)

When asked to build/update wiki concepts. **This phase is incremental: a
concept page is a living synthesis of *every* paper that references it, so
adding new papers must re-touch the existing pages they reference — not only
mint new ones.** A concept page that omits a paper that cites it is stale and
silently wrong.

First build an **inventory**: scan `wiki-pages/*.md` and, for every concept,
count how many distinct papers reference it (a reference = a `[[Concept]]`
link **or** a matching keyword tag), and note whether a concept page already
exists. Then apply steps 1–4 using those counts.

1. **Demote** (concept referenced by **only one** paper AND no page exists):
   replace `[[Concept]]` with plain text in that file — a one-mention page
   adds noise, not structure.
2. **Create / promote** (concept referenced by **≥ 2** papers with no page
   yet — including a concept previously demoted to plain text that a new
   paper has now pushed to 2+): create `wiki-pages/<concept-slug>.md`. If it
   was demoted before, also re-link the plain-text mentions back to
   `[[Concept]]` so the graph reconnects. Page rules:
   - Synthesize ONLY from the wiki pages' own content — no outside
     knowledge; the wiki must remain a closed, citable system.
   - Attribute every specific claim: `(Source: [[<paper-file-stem>]])`.
   - If papers conflict (e.g. different onset temperatures), state the
     contradiction explicitly instead of averaging or choosing.
   - Schema: frontmatter `type: concept`, **`aliases: ["<Concept Name>"]`**
     (see the link rule below), `tags: [synthesis]`; body = `# Concept`,
     1-2 sentence **Summary**, `## Synthesized Knowledge` (2-4 attributed
     paragraphs), `## Literature Mentions` (one bullet per paper:
     `- [[stem]]: finding`), `## Related Concepts` (2-4 links).

   ```yaml
   ---
   type: concept
   aliases:
     - "Phase Change Material"
   tags:
     - synthesis
   ---
   ```

3. **Update existing pages** (concept that **already has a page** and is
   referenced by one or more of the newly reviewed papers): re-open the page
   and fold those papers in — do not leave it as-is.
   - Add a `- [[stem]]: finding` bullet to `## Literature Mentions` for each
     new paper (one per paper; never duplicate an existing stem).
   - Integrate genuinely new or conflicting findings into
     `## Synthesized Knowledge` — this is synthesis, not an append log: weave
     the new attributed claims into the existing paragraphs, and if a new
     paper contradicts an existing one, state the contradiction explicitly.
   - Refresh the `*Last updated: <date>*` line.
   - Skip any existing page that **no** newly reviewed paper references —
     don't churn untouched concepts.

4. **Link integrity (critical).** A clicked `[[Some Name]]` opens only a
   file whose basename is exactly `Some Name.md`; frontmatter `aliases:` help
   autocomplete/search but do NOT resolve clicks, so an alias-only link opens a
   new empty note. Always link by file stem with a display name:
   `[[phase-change-material|Phase Change Material]]` (paper notes and concept
   pages alike). Keep `aliases:` on concept pages for search. After
   building/updating, run:

   ```bash
   python tools/check_links.py <wiki-dir>
   ```

   It resolves by basename only, lists dangling links and empty notes, and
   exits 1 if any exist.

## Notes

- New review type = new JSON file in `review/templates/` (same shape as
  `cell_thermal_methods_v2.json`); no change to this skill needed.
