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

**First, before anything else: pick lessons from the course list.**
Asked for on 2026-08-27, from a phone, looking at the list. The
machinery is already there and in the wrong place: `chosenLessons()`
and `store.chosen` exist, `buildReview({only})` honours them, and
`chooseHTML()` puts them behind `#/choose` as a grid of bare numbers
reachable only from the review area. What is missing is the obvious
thing: tick one or more lessons **on the course list itself**, where
you are already looking at them, and act on the selection from there.
Tapping a lesson must still open it, so the selection needs a way in
that does not fight the tap.

Decided 2026-08-27: once lessons are ticked, offer **both** modes -
review drawn from those alone (the existing plumbing) and studying
them back to back as one run (new session code).

## Agreed on 2026-08-27, in the order they were agreed

1. **Pick lessons from the course list** - above.
2. **Free talk that opens the other way round.** `talkScope()` and
   `setTalkScope()` already exist and already take several lessons, and
   the scope picker is already on the screen: that half is built. What
   is missing is who starts. Today the other side always opens and you
   always answer. Wanted: you opening as the foreigner, and then the
   reverse - you playing the local answering a tourist, which makes you
   produce answers instead of questions. Held to the lessons fed in.
3. **Roots.** Group the dictionary by consonantal skeleton, so k-t-b
   shows kitàb, àktub, màktab together. Vocabulary that costs the
   review pool nothing, which is the only kind left worth having.
4. **A speed drill.** Today the voice has one slow/normal switch. Want
   a drill that starts near 0.7 and ratchets towards 1.15 as you get it
   right, and tells you where you stopped. Comprehension speed is what
   fails in the street, not vocabulary.
5. **Which sound you personally get wrong.** The mic compares whole
   phrases. Aggregate what the recogniser returns by sound and report
   it: your ح is heard as h eight times in ten, your ع is fine.
6. **Answer in your own words.** Every drill runs English to Arabic or
   back. Nothing asks you to answer a question with your own true
   information. Ilà matà ànta hùna? and you type the real answer.
7. **A warning before a phrase that commits you.** The `how: "direct"`
   tag exists and is never surfaced in a session. Show it once, the
   first time.
8. **Words the author is not sure of, marked in the app.** Replaces the
   idea of a printable sheet for a native speaker, which was rejected
   on 2026-08-27 as too slow: he wants to be speaking it when he lands.
   Instead, flag the entries whose Levantine or vocalisation is a
   judgement call, verify the ones that can be verified, and leave the
   rest carrying a visible mark so a native can be asked about exactly
   those and nothing else. Every agent draft in this repo ended with a
   "least sure about" list; that is the raw material and it is
   currently thrown away.
9. **Trip triage, opt in only.** Naming a departure date lets the app
   put everything you will not need in the first week below the line
   and bring the daily pool back under what a session can carry.
   Agreed on condition it is **never the default**: the app must not
   ask for a date, and must work exactly as now until one is given.


- **Two-turn chains** in the conversations, a **weekly plan**, and the
  **same phrase from two voices**. All three were agreed and none is
  built.
- **The search remembering what it could not find**, and a
  **circumlocution drill** (no word for it, so describe it with the
  words you have). Agreed, not built.
- The dictionary builds a session from a word. It does **not** invent
  new dialogue on it, and it cannot: there is no model in a static
  file, only `FRAMES` recombination. Extending `FRAMES` is the honest
  version of that idea.
- `numberWords()` still stops at 99. It only powers ages and the
  counting drill, so nothing is broken; the hundreds and thousands are
  taught as phrases in lesson 56 instead.

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
