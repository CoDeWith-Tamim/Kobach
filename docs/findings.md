# Preliminary Finding 001

## Title
Regex Pre-filter Sensitivity to Attack Phrasing Variation

## Observation
The initial evaluation produced a 47.6% bypass rate across 21 attack cases
(3 per category across 7 categories, 1 case each in en/bn/banglish).

A subsequent evaluation with 54 cases produced a 75.9% bypass rate. The
increase came entirely from expanding 3 of the 7 categories
(direct_injection, roleplay_jailbreak, language_switch_attack) to 10-15
cases each; the other 4 categories were unchanged (3 cases each).

The false-positive rate was 0% in both runs, using the same 8 legit queries.

## Preliminary Interpretation
The regex-based pre-filter may be sensitive to surface-level phrasing
variation within the categories that were expanded. This has NOT been
shown to generalize to the 4 categories that were not expanded.

## Limitations
- The two runs are not a clean before/after comparison: the 21-case set
  is a subset of the 54-case set, so the bypass-rate increase is driven
  by 3 specific categories, not an overall sample change.
- All 54 cases were authored by the assistant (Claude), not drawn from
  an existing dataset or written by native speakers -- diversity of
  real attacker phrasing is not yet established.
- The 4 unexpanded categories (indirect_injection, encoding_evasion,
  multiturn_manipulation, output_exfiltration) still have only 3 cases
  each -- no claim is made about regex performance on those.
- Legit-query sample size (8) is small; false-positive rate at this
  scale has wide uncertainty.
- No statistical significance claim is made.

## Next Experiment
1. Expand the remaining 4 categories to 10-15 cases each, so all 7
   categories are evaluated on comparable footing.
2. Re-run metrics.py per category (not just overall) to see which
   categories the regex layer fails hardest on.
3. Begin sourcing some attack phrasing from outside the assistant's own
   generation (community examples, existing injection corpora where
   license allows) to reduce authorship bias.
4. Keep the defense configuration fixed across these runs so results
   are comparable.
