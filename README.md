# Fusha

## What it is

Fusha is a single-page web app for learning to speak and understand Arabic. It teaches Modern Standard Arabic (fus-ha) by default, with Egyptian, Levantine and Gulf Arabic layered on top as switchable varieties, all sharing one course and one set of progress. It never shows the Arabic alphabet: every phrase is written in the Latin alphabet, with an accent mark showing which syllable is stressed. The course is built around speaking and understanding spoken Arabic, not reading a new script, so the script is left out on purpose.

## How to use it

Open https://lorenzobianchimani17.github.io/fusha-arabic/. It is one HTML file with no server behind it: once it has loaded, it keeps working with no connection at all.

Everything - which lessons you have passed, the strength of each phrase, which variety you are studying, phrases set aside, marked recognise-only or hidden, your own name and details - is stored in the browser's local storage, on that one device and browser. Nothing is sent anywhere.

To move progress to another device: open the menu, copy the backup code shown on the home screen, and paste it into the same box on the other device. It asks for confirmation before replacing whatever is already there.

## What is in it

27 lessons, greetings through travel, illness and talking about the past: 357 phrases in total, 80 of them marked core, meaning they can carry a conversation by themselves. 19 scripted conversations, each unlocked once you have passed the lessons it draws on.

Practice screens, beyond the lessons themselves:

- **Today**: one button. It decides what is most needed - the next lesson, core phrases still shaky, or whatever else is weak - and starts it.
- **Mixed review**: everything passed so far, once at least one lesson is passed.
- **Seven games**, one phrase at a time: Quiz (pick the meaning), Build (put the words in order), Match (pair phrase to meaning), Reply (answer what is said to you), Say it (say it aloud, then mark yourself), Listen (hear it, no text, needs a voice on the device), Write (type the transliteration from memory).
- **Free talk**: say or type anything; it answers from the lessons you choose.
- **Numbers by ear**: a number said once, the way a price or a departure time actually arrives, and you type back the digits.
- **What are they asking?**: 100 real questions drawn from the course, by ear. You pick what kind of question it is - where, when, how much, yes or no, and so on - not what it means.
- **What would you say?**: 58 situations with no English to translate. You say or type something that works.
- **Make a sentence**: 125 sentences built from 13 patterns and words the course has already taught, none of them a phrase the course teaches directly.
- **One job, several phrases**: 10 groups of near-synonyms - four ways to say hello, five to say goodbye - so you can pick the one you will actually say and keep the rest for recognising only.
- **Your words** and **Phrasebook**: the phrases you have set aside or hidden, and a search over every phrase and every line of dialogue in the course.

Four varieties, switchable at any time, progress shared across all of them. Fusha is the base text the other three are written against. Levantine is finished: of the 357 phrases, 275 have their own Levantine wording and the other 82 have been checked and are identical to fus-ha, so nothing is left unlooked-at; 66 of the 80 core phrases have a distinct Levantine form. Egyptian and Gulf are much earlier: 91 and 46 of the 357 phrases done, with most of the course not yet looked at for either.

## How the memory works

Every phrase carries a strength from 0 to 5. A right answer raises it one step, up to 5. A wrong answer drops it two steps, or one step for a typing slip, since a typo is not the same as not knowing the phrase.

Each strength holds for a number of days before the phrase is due again: 0, 2, 5, 12, 30 and 75 days for strengths 0 through 5. A day away does not erase progress: a phrase left past its hold drops exactly one step, however long you were gone. A month away does not put a phrase back to zero.

Three ways to take a phrase out of normal rotation, all reversible:

- **Set aside**: you already know it. It leaves rotation at once but comes back once, after 10 days, for a spot check.
- **Recognise only**: you want to understand it but never plan to say it yourself. It is never asked of you in the games that make you produce an answer - Build, Say it, Write, Reply - but keeps turning up in Listen and Match, and the quiz still shows it starting from the Arabic.
- **Hidden**: out entirely. It never comes back and stops counting toward anything. Hiding a phrase also clears any "set aside" mark on it.

## How to work on it

Everything lives in this repository.

    src/fusha.html    the app: title, styles, markup and the whole script
    src/suite.js      the test suite
    src/regen.py      pulls the script out of fusha.html for the tests
    src/build.py      writes index.html from fusha.html
    index.html        the deployed page, generated - do not edit by hand
    BACKLOG.md        the decided work that has not been built yet

`src/fusha.html` is the source of truth and the only file to edit. It
carries no `<head>`: the artifact host it is also published to supplies
one, and `build.py` supplies the same one for the web.

To change something:

    cd src
    # edit fusha.html
    python3 regen.py                # rebuild the copies the tests read
    node suite.js                   # and the other three configurations
    node suite.js --voice
    node suite.js --mic
    node suite.js --voice --mic
    python3 build.py                # write index.html
    cd .. && git add -A && git commit

The two flags describe what the device can do: whether it has an Arabic
voice and whether it has a microphone. Each run prints a checklist and
finishes with "ALL CHECKS PASS" or a list of failures, and exits
non-zero if anything failed. `src/extracted.js` and
`src/extracted.test.js` are generated by `regen.py` and are not
committed.

## What it does not do

- It does not teach the Arabic alphabet, or reading or writing the script, at all.
- Egyptian and Gulf are thin: most of the course has not been looked at for either yet.
- Hearing the phrases needs an Arabic voice installed on the device. Speaking into it needs a microphone, HTTPS, and a top-level page rather than an embedded frame.
- Progress does not sync anywhere by itself; moving it between devices is a manual copy and paste of the backup code.
- No accounts, no server, no analytics.
