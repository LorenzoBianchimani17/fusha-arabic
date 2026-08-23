# Agreed, not yet built

Decided on 2026-08-23, after four audits of the app (Levantine accuracy,
code, visual design, learning design) and four rounds of choices.

Everything below was chosen deliberately. Nothing here is a suggestion
waiting for approval; it is a list of work waiting for a turn.

## The plan

Order chosen 2026-08-23: the source into the repository first, then the
sixteen learning mechanisms, in four deliveries. Each one ends with the
test suite green in all four configurations, the hundred-and-fifty-day
simulation re-run, and the app live on Pages, so it can be used before
the next one starts.

**Delivery 0, the source into the repository.** `src/fusha.html`,
`src/suite.js` and the two scripts that generate `index.html` and the
test copy. Small, and it removes the only real risk in the project.

**Delivery 1, what happens when you are wrong.** In this order, because
three of the four need the same thing underneath: a count of how many
times each phrase has been missed. Then the second attempt before the
answer; then naming what you confused it with; then yesterday's misses
leading today; then leeches, which need all of the above to know what a
leech is. This delivery changes the moment you feel most.

**Delivery 2, difficulty that follows your strength.** Fading support
first, because it is the one that reclaims wasted rounds. Then how sure
you were, which changes the interval arithmetic and therefore needs the
simulation re-run before anything else lands on top of it. Then timed
rounds above strength 3, then session length following the run.

**Delivery 3, how a phrase arrives.** Guess before you see, expanding
rehearsal inside a session, backward buildup, contrast with the twin.
These touch the study screen and the round dealer, which were both
rewritten on 2026-08-23, so they come after the two deliveries that do
not.

**Delivery 4, the mouth and the ear.** Shadowing, whole-sentence
dictation, an ear-only session, speaking at a run. Three of the four
need a voice or a microphone and must degrade honestly without them,
which is why they are last: they are the least certain to be usable on
every device.

Sections 5 to 11 below are not scheduled. They are the decided list to
draw from once the mechanisms are in and have been used for a week.

## Done, 2026-08-23

Delivery 0 (the source into the repository) and deliveries 1 to 4 (the
sixteen learning mechanisms) are built and live. Sections 1 to 4 below
are kept as the record of what they were meant to do; the code is in
`src/fusha.html` and the tests that hold each one in place are in
`src/suite.js`.

What is left to draw from: sections 5 to 11.

## 0. Before anything else

- **The source of truth goes into this repository.** `fusha.html` and
  `suite.js` live in a scratchpad today. That scratchpad has emptied
  itself once already in this project and the rebuild cost a day.
  `index.html` stays generated from `fusha.html`.

## 1. How a phrase arrives

Today: you see it, then it is asked of you. All four of these change the
first encounter, which is where retention is won or lost.

- **Guess before you see.** The study card asks for a guess before it
  shows the answer. Getting your own guess wrong and then seeing the
  right one beats reading the right one first.
- **Expanding rehearsal inside a session.** A new phrase returns after
  2 rounds, then 5, then 10. Today it can return immediately or never.
- **Backward buildup.** Long phrases are learned from the tail:
  `min fàdlik`, then `qàhwa min fàdlik`, then `urìd qàhwa min fàdlik`.
- **Contrast with the twin.** A new phrase that resembles one you know
  is introduced next to it, with the difference named. Confusions are
  cheaper to prevent than to unpick.

## 2. Difficulty that follows your strength

Today: a phrase you have known for a month is asked exactly like one you
met yesterday.

- **Support fades.** Four options while weak, three at strength 3, none
  at 4: produce it.
- **How sure were you.** After a right answer, "sure" or "only just".
  Sure lengthens the interval, only-just shortens it.
- **Timed, once you know it.** Above strength 3, three seconds. Not
  knowing it and not having it ready are different failures.
- **Session length follows the run.** Longer while you are getting them
  right, shorter while you are not, instead of always 10 to 12 rounds.

## 3. The mouth and the ear

- **Shadowing.** Hear it, repeat it at once, the microphone says how
  close you were. The only exercise that loosens the sounds Italian does
  not have: the ayn and the kh.
- **Whole-sentence dictation.** Numbers by ear, extended to sentences.
- **An ear-only session.** A switch that removes the text from every
  game for one session. Reading is the crutch that prevents listening.
- **Speaking at a run.** Ten phrases out loud without stopping, timed,
  unmarked. For making automatic what is already known.

## 4. What happens when you are wrong

- **Leeches.** A phrase missed five times is not re-served identically
  for ever: broken into its words, hung off one you know, or honestly
  set aside.
- **A second attempt before the answer.** One option removed, try again.
  A second try is retrieval; reading the answer is not.
- **Name what you confused it with.** Not "wrong" but "you chose lau
  samàht, which is for getting attention; this one goes on the end of a
  request".
- **Yesterday's misses lead today.** They rejoin the weighted draw now
  and may not come back for weeks.

## 5. The rhythm of using it

- **Say how long you have.** Three minutes in a queue and twenty on the
  sofa are different sessions; there is one length today.
- **Coming back after a break.** A dedicated return: the most important
  things first, the rest deferred, and an honest line about what
  happened while you were away.
- **One phrase at a time.** A single question, full screen, no session
  and no score. For the thirty seconds in a lift, which is when the app
  actually gets opened.
- **A conversation a day.** One short exchange stitched from what you
  know that day, different every time, instead of the fixed nineteen.

## 6. Knowing where you stand

- **A test with no help.** Ten minutes, no hints, no second chances,
  nothing counted toward memory. Every number in the app today measures
  the process; none measures the result.
- **What you can do, not how many phrases you know.** "You can order a
  coffee, take a taxi and introduce yourself. You cannot yet arrange to
  meet, or ask someone to repeat themselves."
- **A diary of what changed.** A line after each session and a weekly
  summary: what went solid, what slipped, what you have not seen.
- **Record yourself and listen back.** Keep the recording in Say it and
  play it against the synthesised voice.

## 7. More to say

- **The answers you do not have.** You can ask now but not answer:
  no "yes I have", "no I have not", "I do not know", "maybe", "as you
  like". Twelve short replies that close an exchange.
- **The past tense, properly.** The past-tense lesson has six verbs in
  the first person only. No "you", no "he", and no questions in the
  past: where were you, what did you eat, did you like it.
- **A second round of situations.** The 58 are nearly all tourist. Thirty
  more from someone who lives there: the neighbour, the colleague, the
  barista who recognises you, someone asking *you* for directions.

## 8. Features

- **Your own words.** Somewhere to put a word you heard in the street:
  write it as it sounded, say what it means, and from then on it is in
  the spaced repetition like everything else. The app cannot learn
  anything from you today.
- **The screen for right now.** One tap from home: twenty large lines
  with audio, the ones you need in the street. The phrasebook exists but
  is ordered by lesson and has to be searched, which is the last thing
  you want to be doing while someone is talking to you.

- **Free talk that can say it did not understand.** Today it answers
  "Là àfham" and starts again. With the repair kit now in the course it
  could instead teach you out of it: ask you to repeat, offer you the
  words.
- **A picture of where you are.** One line per lesson, coloured by
  strength. "52 of 80" says nothing.
- **Revision aimed at a situation.** "Get me ready for the taxi": a
  session built only from what that needs.
- **Export to a file.** The backup is a code to copy by hand. A button
  that downloads, and one that reads it back.

## 9. The dialect

- **Teach the difference.** You will hear both: fus-ha on television and
  on signs, the dialect in the street. A lesson and a drill on moving
  between them: what changes, what does not, when to use which.
- **Levantine as the base.** If that is what is being studied, it should
  be the default and fus-ha the variant, from the first screen on.
- **Egyptian and Gulf stay as they are.** Declared incomplete, not
  extended. One finished variety beats three half-written ones.

## 10. Look at it on the actual phone

Everything measurable from the source has been fixed. Nobody has seen
the screens. Two or three screenshots from the phone would replace a lot
of guessing.

Also chosen and worth doing while the screens are open:

- **The result screen.** The one moment the course speaks to you about
  you. Today it is a big number and three buttons; it could say what
  changed.
- **A warmer light theme.** The light palette is a cool grey-green.
  Ivory rather than white, same accent, reads better over a long sitting
  and looks less like a control panel.
