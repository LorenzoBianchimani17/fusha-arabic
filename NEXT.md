# Where we stopped, 2026-08-26

Everything agreed is built and live. This file is the handover: what is
open, what to watch, and the rules for the repository.

## What went in on 2026-08-26

Twenty-one lessons, 533 phrases to 829. In order: feelings, the body,
more food, places in town, position and time, comparing, more verbs,
asking why, whose it is, distance, learning from a local, character,
fruit and vegetables, the chemist and the jeweller, a night out, the
way they put it, what a price is actually in, when it goes wrong, at
the chemist and what is wrong, coming and going, the match and the
traffic and the family, being someone's guest.

Two features. **The dictionary** (`#/dict`): every word in `GLOSS` and
`GLOSS_LEV` indexed against every line of the course, on both the
fus-ha and the Levantine side, with what it means, what kind of word it
is, and every line it appears in. Open one and it builds a session out
of nothing but those lines. **Four iOS things**: large titles that hand
over to the bar on scroll, the menu as a bottom sheet under 620px, drag
from the grip to dismiss it, and a right answer that arrives and draws
its own tick.

## What the audits found, and the rule they earned

Two agent audits paid for themselves several times over.

A **teacher's audit** of thirteen new lessons found 21 real errors,
including a phrase with the pair of hands in the nominative where an
order needs the accusative, which the synthesiser was saying out loud.
The same audit has **not** been run on lessons 1 to 41. It is the
highest-value thing left in this repo.

A **can-he-say-it audit** walked seven real days with the course and
reported sentence by sentence what it could and could not produce. Ten
gaps came out ranked; all ten are now closed. The method is worth
repeating whenever the course grows: it finds what a topic list cannot.

The rule they earned: **a new lesson is not finished until something
adversarial has read it.** The suite checks that the data is
consistent, not that the Arabic is right.

## Still to build

## Agreed on 2026-08-27, and all of it built the same day

1. **Pick lessons from the course list.** Seven named arcs, tick any of
   them, an arc's All takes a whole stretch, and a bar at the bottom
   offers Review these or Study in a row.
2. **Free talk from all three sides.** They start, you start, and you
   are the local. Which side a question comes from is worked out from
   its kind and whether it names a thing.
3. **Families.** Ninety hand-checked roots, 523 words, a Families
   filter in the dictionary and the relatives on every word's page.
   Written by hand because the Latin spelling collapses the emphatic
   consonants and half of a derived grouping would be false.
4. **Keeping up.** Twelve phrases at a speed that climbs when you
   follow and falls when you do not, reporting the fastest you managed
   rather than a score.
5. **Which sound you lose.** The mic comparison read one consonant at a
   time, four goes before it will say anything, on the drill screen
   that exists to fix them.
6. **In your own words.** Eighteen questions about you, answered in
   Arabic with something true, nothing marked, and what you wrote kept.
7. **The phrase that commits you**, said once in a session the first
   time you get it right, then never again.
8. **Not sure about these.** Forty-two lines where the dialect or the
   vocalisation was a judgement, marked on the card and collected on a
   screen with the Arabic to show somebody.
9. **Conversations you had.** Keep a free talk, drill it later out of
   your own lines.
10. **The screen stays on** while a session is running.
11. **Before you go.** Give a departure date and it will put aside
   everything outside the backbone: 215 phrases stay in the rotation
   against 829, and the pool falls from 28 a day to 8. Never asked
   for, never on by itself, undone in a tap, and it lets go by itself
   when the date passes.

## Still to build

Nothing agreed is outstanding.

Three ideas were raised on 2026-08-27 and not judged:

- **The register cap is now working against the course.** A test holds
  `how:`-tagged phrases under a tenth of the total. That ratio was set
  at about 400 phrases; at 829 it means every lesson about register
  forces a tag off a good card. What it was protecting is that the tag
  should mean something, which is a claim about distribution, not a
  ratio.
- **Nothing says what you can do now that you could not last week.**
  The diary and the capability list both exist; a capability flipping
  to ready is the strongest thing the app could say and it is never
  said on the home screen.
- **No repair for a phrase that landed badly.** The course teaches
  `Ànti jamìla` with a warning and nothing for the moment after.

## One thing to watch, not a task

The pool is 829 phrases and needs 28 reviews a day to hold all of it.
The longest pace gives 30, raised from 22 on 2026-08-26 for exactly
this reason - a pace labelled *as long as it takes* should mean it.
There is no room left above 30 without changing what a session is.
Before agreeing to another twenty lessons, read that number again.

## The standing rules for this repo

- `src/fusha.html` is the source. `index.html` is generated by
  `src/build.py` and is never edited by hand.
- `python3 src/regen.py` then `node src/suite.js` before any commit, in
  all four configurations: plain, `--voice`, `--mic`, `--voice --mic`.
  `--quick` while editing; the four in full before committing.
- Re-run the 150-day simulation when anything touches the spaced
  repetition, and only then.
- Every new phrase needs four things: the lesson entry, a vocalised
  SCRIPT entry, a Levantine form in DIALECT or a line in SAME, and a
  gloss for every new word on both sides. Two tests now enforce the
  last one: every word the course teaches has a dictionary entry, and
  no word is glossed twice in either table.
- The Levantine has still never been read by a native speaker. That is
  the largest unmeasured risk in the project.
