# Pulls the script out of fusha.html twice: once as plain JavaScript for
# reading and grepping, once with two hooks appended so the test suite can
# see inside the closure. Both are generated; neither is edited by hand.
import re
import pathlib

HERE = pathlib.Path(__file__).parent
src = (HERE / "fusha.html").read_text(encoding="utf-8")
js = re.search(r"<script>(.*)</script>", src, re.S).group(1)

(HERE / "extracted.js").write_text(js, encoding="utf-8")

HOOKS = (
    '\n  global.__peek = function () { return { session: session, view: view, store: store,'
    ' learn: learn, talk: talk, ears: ears, navOpen: navOpen, people: people, made: made,'
    ' moment: moment, asked: asked, numbers: numbers, loud: loud, sounds: sounds, answers: answers,'
    ' frameRun: frameRun }; };'
    '\n  global.__data = { LESSONS: LESSONS, SCRIPT: SCRIPT, CONVOS: CONVOS,'
    ' PHRASEBOOK: PHRASEBOOK, GAMES: GAMES, VARIETIES: VARIETIES, DIALECT: DIALECT,'
    ' SAME: SAME, GLOSS: GLOSS, GLOSS_LEV: GLOSS_LEV, glossesFor: glossesFor,'
    ' glossFor: glossFor, noteFor: noteFor, FRAMES: FRAMES, combos: combos,'
    ' numberWords: numberWords, nameScript: nameScript, yourLines: yourLines,'
    ' COUNTRIES: COUNTRIES, JOBS: JOBS, MOMENTS: MOMENTS, openMoments: openMoments,'
    ' lessonTeaching: lessonTeaching, TWINS: TWINS, openTwins: openTwins,'
    ' twinsToDecide: twinsToDecide, twinReached: twinReached, isPassive: isPassive,'
    ' isLeech: isLeech, missCount: missCount, missedEarlier: missedEarlier, LEECH_AT: LEECH_AT,'
    ' ASK_KINDS: ASK_KINDS, askKind: askKind, askPool: askPool, compose: compose,'
    ' CAN: CAN, canStates: canStates, canAt: canAt, canSentence: canSentence,'
    ' buildExam: buildExam, EXAM_LENGTH: EXAM_LENGTH, examHistory: examHistory,'
    ' dailyConvo: dailyConvo, PACES: PACES, reviewRounds: reviewRounds,'
    ' diary: diary, weekSummary: weekSummary, unseen: unseen, deltaLine: deltaLine,'
    ' NOW: NOW, mineWords: mineWords, mineLesson: mineLesson, MINE_ID: MINE_ID,'
    ' buildAimed: buildAimed, canById: canById, canOpen: canOpen, REPAIRS: REPAIRS,'
    ' STREET: STREET, swapRound: swapRound, varietyCoverage: varietyCoverage,'
    ' ASKING: ASKING, playable: playable, drillable: drillable, speech: speech, rotateVoice: rotateVoice,'
    ' modes: modes, modePct: modePct, earGap: earGap, earBehind: earBehind, byEar: byEar,'
    ' noteMode: noteMode, MODE_WINDOW: MODE_WINDOW, MINIMAL: MINIMAL,'
    ' frameRunnable: frameRunnable, newFrameRun: newFrameRun, MASTERED: MASTERED,'
    ' REPLIES: REPLIES, SIDES: SIDES, replyPool: replyPool, HOW: HOW, howOf: howOf,'
    ' judgeTyped: judgeTyped, sameSaidLoose: sameSaidLoose, endingHint: endingHint,'
    ' sameJob: sameJob, weakestLesson: weakestLesson, chosenLessons: chosenLessons,'
    ' myNote: myNote, standing: standing, stuckList: stuckList, buildTestOut: buildTestOut,'
    ' lessonSkipped: lessonSkipped, openSession: openSession, TESTOUT_PASS: TESTOUT_PASS,'
    ' oneOut: oneOut, phraseTyped: phraseTyped, openMoments: openMoments,'
    ' ITALIAN: ITALIAN, italianFor: italianFor, courseSearch: courseSearch,'
    ' WANTS: WANTS, wantKey: wantKey, nextForWant: nextForWant, forWant: forWant,'
    ' poolFits: poolFits, PACES: PACES,'
    ' englishFor: englishFor, courseIndex: courseIndex, normalise: normalise,'
    ' sameSaid: sameSaid, tokens: tokens, canMake: canMake, coreCounts: coreCounts,'
    ' lessonNo: lessonNo, RECHECK_AFTER: RECHECK_AFTER, HOLDS: HOLDS, today: today,'
    ' strengthOf: strengthOf, isFading: isFading, rateFor: rateFor,'
    ' suggestionsAfter: suggestionsAfter, flattenArabic: flattenArabic,'
    ' heardScore: heardScore, talkIndex: talkIndex, bestMatches: bestMatches,'
    ' replyFor: replyFor, talkScope: talkScope, romanise: romanise,'
    ' nearestTranslit: nearestTranslit, disp: disp, spk: spk, variety: variety };'
)

START = '\n  applyHash(typeof window.location !== "undefined" ? window.location.hash : "");'
(HERE / "extracted.test.js").write_text(js.replace(START, HOOKS + START), encoding="utf-8")
print("extracted.js and extracted.test.js regenerated")
