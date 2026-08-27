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
    ' frameRun: frameRun, recall: recall, yours: yours }; };'
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
    ' poolFits: poolFits, PACES: PACES, repliesTo: repliesTo, otherGenderOf: otherGenderOf,'
    ' RITUAL: RITUAL, ritualFor: ritualFor,'
    ' englishFor: englishFor, courseIndex: courseIndex, normalise: normalise,'
    ' sameSaid: sameSaid, tokens: tokens, canMake: canMake, coreCounts: coreCounts,'
    ' lessonNo: lessonNo, RECHECK_AFTER: RECHECK_AFTER, HOLDS: HOLDS, today: today,'
    ' strengthOf: strengthOf, isFading: isFading, rateFor: rateFor,'
    ' suggestionsAfter: suggestionsAfter, flattenArabic: flattenArabic,'
    ' heardScore: heardScore, talkIndex: talkIndex, bestMatches: bestMatches,'
    ' replyFor: replyFor, talkScope: talkScope, romanise: romanise,'
    ' nearestTranslit: nearestTranslit, disp: disp, spk: spk, variety: variety,'
    ' dictIndex: dictIndex, dictSearch: dictSearch, kindOf: kindOf, KINDS: KINDS,'
    ' wordDrill: wordDrill, wordPool: wordPool, levFormOf: levFormOf,'
    ' topbarHTML: topbarHTML, navHTML: navHTML, ARCS: ARCS,'
    ' arcLessons: arcLessons, pickedIds: pickedIds, buildRun: buildRun,'
    ' TALK_ROLES: TALK_ROLES, talkRole: talkRole, fromVisitor: fromVisitor,'
    ' openersFor: openersFor, newTalk: newTalk, ROOTS: ROOTS, rootOf: rootOf,'
    ' holdScreen: holdScreen, AWAKE_ON: AWAKE_ON, saidBefore: saidBefore,'
    ' EAR_SOUNDS: EAR_SOUNDS, noteSounds: noteSounds, earReport: earReport,'
    ' EAR_ENOUGH: EAR_ENOUGH, PACE_FROM: PACE_FROM, PACE_STEP: PACE_STEP,'
    ' PACE_CEIL: PACE_CEIL, PACE_FLOOR: PACE_FLOOR, PACE_LENGTH: PACE_LENGTH,'
    ' paceLabel: paceLabel, rateFor: rateFor, UNSURE: UNSURE, unsureOf: unsureOf, unsureMark: unsureMark,'
    ' YOURS: YOURS, yoursOpen: yoursOpen, yoursRead: yoursRead, yoursSaid: yoursSaid,'
    ' keptTalks: keptTalks, keepTalk: keepTalk, talkDrill: talkDrill,'
    ' TALK_KEEPABLE: TALK_KEEPABLE, TALKS_KEPT: TALKS_KEPT,'
    ' TRIP_WEEKS: TRIP_WEEKS, daysToTrip: daysToTrip, setTrip: setTrip, tripOn: tripOn,'
    ' packing: packing, packedSet: packedSet, packedAside: packedAside,'
    ' packCounts: packCounts, setPacked: setPacked, visiblePhrases: visiblePhrases,'
    ' studied: studied, firstLessonOf: firstLessonOf, myWayRead: myWayRead, glossHTML: glossHTML };'
)

START = '\n  applyHash(typeof window.location !== "undefined" ? window.location.hash : "");'
(HERE / "extracted.test.js").write_text(js.replace(START, HOOKS + START), encoding="utf-8")
print("extracted.js and extracted.test.js regenerated")
