# The teacher's audit

The suite checks that the data is consistent. It cannot check that the
Arabic is right. Nothing in this repo can, which is why a new batch of
lessons is not finished until something adversarial has read it.

This is the brief. It is written down so that every audit asks the same
questions and two audits can be compared. It was used on lessons 42 to
55 on 2026-08-26 and found 21 real errors, including a pair of hands in
the nominative where an imperative needs the accusative, which the
speech synthesiser was saying out loud.

## What to give the auditor

- The file: `src/fusha.html`
- The range: which `id:` values, and no more than about eight lessons
  at a time or the reading gets shallow
- Read-only. The auditor must not edit anything. One person applies the
  findings, in one place, because the file is one file.

## The six questions

1. **Wrong or unnatural Arabic.** A fus-ha phrase no native would say,
   a case ending that changes the meaning, a verb form that does not
   exist, a gender disagreement between a phrase and its `f:` variant.
2. **Wrong or unnatural Levantine.** A `lev:` form that is really
   Egyptian or Gulf, a q-reflex applied where it should not be, a word
   not used in Syria, Lebanon, Jordan or Palestine, an Arabic script
   line that does not match its own transliteration.
3. **Vocalisation errors in SCRIPT.** A missing or wrong short vowel, a
   shadda in the wrong place, a hamza on the wrong seat. SCRIPT is fed
   to a speech synthesiser, so an error there is heard, not just read.
4. **Stress marks.** The file marks the stressed vowel with a grave
   accent, exactly one per word. Flag any entry with the accent on the
   wrong syllable by the ordinary rules (superheavy final syllable
   stressed; else heavy penult; else default leftward), with two
   accents, or with none.
5. **Duplicates and near-duplicates**, within the range and against the
   rest of the course: two phrases teaching the same thing, or an
   English gloss that collides with an existing one.
6. **Notes that state something false**, about the language or about
   what the course teaches elsewhere. A note that says a word appeared
   in a lesson where it does not is worse than no note.

## What a finding must carry

The lesson id, the exact `ar:` string, what is wrong, and the exact
replacement text. Ordered most serious first. Lessons that are clean
are named in one line rather than padded.

## What is not a finding

Style preferences. Missing content - that is a different audit, the one
that walks seven real days and reports what cannot be said. Anything
that cannot be pointed at a specific string.

## The other audit

Worth running whenever the course grows by more than a few lessons:
give an agent the whole `LESSONS` array and the learner's actual goal,
and have it walk real situations end to end - arriving, a whole meal,
falling ill, something going wrong, a conversation with somebody he
likes, filling a silence, being a guest - reporting for each what the
course can produce and what it cannot, ranked. Run on 2026-08-26 it
produced ten gaps, all of which were real and none of which a topic
list would have surfaced.
