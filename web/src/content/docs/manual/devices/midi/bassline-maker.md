---
title: "Bassline Maker"
description: "Bassline Maker"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

A MIDI device: makes a bass line of an on-beat phrase and an off-beat one, chosen from busy to sparse and varied through the pattern, its intervals stretched and made minor, transposed from the keys or played as written, with eight patterns.

[Bassline Maker on the website](/solmara/write/#bassline-maker)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Pattern | 1 count to 8 count | 1 count |
| Playback mode | SEQ, SEQ+KEY, KEY | SEQ |
| MIDI pitch | Off, On | Off |
| MIDI velocity | Off, On | Off |
| Octave | -2 count to 2 count | 0 count |
| Shuffle source | Local, Global | Local |
| Pattern 1 root note | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 1 steps | 16 count to 64 count | 16 count |
| Pattern 1 shift | -32 to 32 | 0 |
| Pattern 1 rate | 11 choices: 1/1, 1/2, 1/4, 3/16, … | 1/16 |
| Pattern 1 shuffle | 50% to 75% | 50% |
| Pattern 1 on-beat bank | A, B | A |
| Pattern 1 on-beat phrase | 1 count to 64 count | 24 count |
| Pattern 1 on-beat velocity | 0% to 100% | 100% |
| Pattern 1 on-beat note length | 0% to 100% | 40% |
| Pattern 1 on-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Square |
| Pattern 1 on-beat variator amount | -100% to 100% | 0% |
| Pattern 1 off-beat bank | A, B | A |
| Pattern 1 off-beat phrase | 1 count to 64 count | 12 count |
| Pattern 1 off-beat velocity | 0% to 100% | 80% |
| Pattern 1 off-beat note length | 0% to 100% | 30% |
| Pattern 1 off-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Pulse |
| Pattern 1 off-beat variator amount | -100% to 100% | 0% |
| Pattern 1 note range | -2 to 2 | 0 |
| Pattern 1 minorness | 0 count to 4 count | 0 count |
| Pattern 2 root note | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 2 steps | 16 count to 64 count | 16 count |
| Pattern 2 shift | -32 to 32 | 0 |
| Pattern 2 rate | 11 choices: 1/1, 1/2, 1/4, 3/16, … | 1/16 |
| Pattern 2 shuffle | 50% to 75% | 50% |
| Pattern 2 on-beat bank | A, B | A |
| Pattern 2 on-beat phrase | 1 count to 64 count | 24 count |
| Pattern 2 on-beat velocity | 0% to 100% | 100% |
| Pattern 2 on-beat note length | 0% to 100% | 40% |
| Pattern 2 on-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Square |
| Pattern 2 on-beat variator amount | -100% to 100% | 0% |
| Pattern 2 off-beat bank | A, B | A |
| Pattern 2 off-beat phrase | 1 count to 64 count | 12 count |
| Pattern 2 off-beat velocity | 0% to 100% | 80% |
| Pattern 2 off-beat note length | 0% to 100% | 30% |
| Pattern 2 off-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Pulse |
| Pattern 2 off-beat variator amount | -100% to 100% | 0% |
| Pattern 2 note range | -2 to 2 | 0 |
| Pattern 2 minorness | 0 count to 4 count | 0 count |
| Pattern 3 root note | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 3 steps | 16 count to 64 count | 16 count |
| Pattern 3 shift | -32 to 32 | 0 |
| Pattern 3 rate | 11 choices: 1/1, 1/2, 1/4, 3/16, … | 1/16 |
| Pattern 3 shuffle | 50% to 75% | 50% |
| Pattern 3 on-beat bank | A, B | A |
| Pattern 3 on-beat phrase | 1 count to 64 count | 24 count |
| Pattern 3 on-beat velocity | 0% to 100% | 100% |
| Pattern 3 on-beat note length | 0% to 100% | 40% |
| Pattern 3 on-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Square |
| Pattern 3 on-beat variator amount | -100% to 100% | 0% |
| Pattern 3 off-beat bank | A, B | A |
| Pattern 3 off-beat phrase | 1 count to 64 count | 12 count |
| Pattern 3 off-beat velocity | 0% to 100% | 80% |
| Pattern 3 off-beat note length | 0% to 100% | 30% |
| Pattern 3 off-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Pulse |
| Pattern 3 off-beat variator amount | -100% to 100% | 0% |
| Pattern 3 note range | -2 to 2 | 0 |
| Pattern 3 minorness | 0 count to 4 count | 0 count |
| Pattern 4 root note | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 4 steps | 16 count to 64 count | 16 count |
| Pattern 4 shift | -32 to 32 | 0 |
| Pattern 4 rate | 11 choices: 1/1, 1/2, 1/4, 3/16, … | 1/16 |
| Pattern 4 shuffle | 50% to 75% | 50% |
| Pattern 4 on-beat bank | A, B | A |
| Pattern 4 on-beat phrase | 1 count to 64 count | 24 count |
| Pattern 4 on-beat velocity | 0% to 100% | 100% |
| Pattern 4 on-beat note length | 0% to 100% | 40% |
| Pattern 4 on-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Square |
| Pattern 4 on-beat variator amount | -100% to 100% | 0% |
| Pattern 4 off-beat bank | A, B | A |
| Pattern 4 off-beat phrase | 1 count to 64 count | 12 count |
| Pattern 4 off-beat velocity | 0% to 100% | 80% |
| Pattern 4 off-beat note length | 0% to 100% | 30% |
| Pattern 4 off-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Pulse |
| Pattern 4 off-beat variator amount | -100% to 100% | 0% |
| Pattern 4 note range | -2 to 2 | 0 |
| Pattern 4 minorness | 0 count to 4 count | 0 count |
| Pattern 5 root note | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 5 steps | 16 count to 64 count | 16 count |
| Pattern 5 shift | -32 to 32 | 0 |
| Pattern 5 rate | 11 choices: 1/1, 1/2, 1/4, 3/16, … | 1/16 |
| Pattern 5 shuffle | 50% to 75% | 50% |
| Pattern 5 on-beat bank | A, B | A |
| Pattern 5 on-beat phrase | 1 count to 64 count | 24 count |
| Pattern 5 on-beat velocity | 0% to 100% | 100% |
| Pattern 5 on-beat note length | 0% to 100% | 40% |
| Pattern 5 on-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Square |
| Pattern 5 on-beat variator amount | -100% to 100% | 0% |
| Pattern 5 off-beat bank | A, B | A |
| Pattern 5 off-beat phrase | 1 count to 64 count | 12 count |
| Pattern 5 off-beat velocity | 0% to 100% | 80% |
| Pattern 5 off-beat note length | 0% to 100% | 30% |
| Pattern 5 off-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Pulse |
| Pattern 5 off-beat variator amount | -100% to 100% | 0% |
| Pattern 5 note range | -2 to 2 | 0 |
| Pattern 5 minorness | 0 count to 4 count | 0 count |
| Pattern 6 root note | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 6 steps | 16 count to 64 count | 16 count |
| Pattern 6 shift | -32 to 32 | 0 |
| Pattern 6 rate | 11 choices: 1/1, 1/2, 1/4, 3/16, … | 1/16 |
| Pattern 6 shuffle | 50% to 75% | 50% |
| Pattern 6 on-beat bank | A, B | A |
| Pattern 6 on-beat phrase | 1 count to 64 count | 24 count |
| Pattern 6 on-beat velocity | 0% to 100% | 100% |
| Pattern 6 on-beat note length | 0% to 100% | 40% |
| Pattern 6 on-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Square |
| Pattern 6 on-beat variator amount | -100% to 100% | 0% |
| Pattern 6 off-beat bank | A, B | A |
| Pattern 6 off-beat phrase | 1 count to 64 count | 12 count |
| Pattern 6 off-beat velocity | 0% to 100% | 80% |
| Pattern 6 off-beat note length | 0% to 100% | 30% |
| Pattern 6 off-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Pulse |
| Pattern 6 off-beat variator amount | -100% to 100% | 0% |
| Pattern 6 note range | -2 to 2 | 0 |
| Pattern 6 minorness | 0 count to 4 count | 0 count |
| Pattern 7 root note | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 7 steps | 16 count to 64 count | 16 count |
| Pattern 7 shift | -32 to 32 | 0 |
| Pattern 7 rate | 11 choices: 1/1, 1/2, 1/4, 3/16, … | 1/16 |
| Pattern 7 shuffle | 50% to 75% | 50% |
| Pattern 7 on-beat bank | A, B | A |
| Pattern 7 on-beat phrase | 1 count to 64 count | 24 count |
| Pattern 7 on-beat velocity | 0% to 100% | 100% |
| Pattern 7 on-beat note length | 0% to 100% | 40% |
| Pattern 7 on-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Square |
| Pattern 7 on-beat variator amount | -100% to 100% | 0% |
| Pattern 7 off-beat bank | A, B | A |
| Pattern 7 off-beat phrase | 1 count to 64 count | 12 count |
| Pattern 7 off-beat velocity | 0% to 100% | 80% |
| Pattern 7 off-beat note length | 0% to 100% | 30% |
| Pattern 7 off-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Pulse |
| Pattern 7 off-beat variator amount | -100% to 100% | 0% |
| Pattern 7 note range | -2 to 2 | 0 |
| Pattern 7 minorness | 0 count to 4 count | 0 count |
| Pattern 8 root note | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 8 steps | 16 count to 64 count | 16 count |
| Pattern 8 shift | -32 to 32 | 0 |
| Pattern 8 rate | 11 choices: 1/1, 1/2, 1/4, 3/16, … | 1/16 |
| Pattern 8 shuffle | 50% to 75% | 50% |
| Pattern 8 on-beat bank | A, B | A |
| Pattern 8 on-beat phrase | 1 count to 64 count | 24 count |
| Pattern 8 on-beat velocity | 0% to 100% | 100% |
| Pattern 8 on-beat note length | 0% to 100% | 40% |
| Pattern 8 on-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Square |
| Pattern 8 on-beat variator amount | -100% to 100% | 0% |
| Pattern 8 off-beat bank | A, B | A |
| Pattern 8 off-beat phrase | 1 count to 64 count | 12 count |
| Pattern 8 off-beat velocity | 0% to 100% | 80% |
| Pattern 8 off-beat note length | 0% to 100% | 30% |
| Pattern 8 off-beat variator shape | 18 choices: Square, Pulse, Ramp, Square x2, … | Pulse |
| Pattern 8 off-beat variator amount | -100% to 100% | 0% |
| Pattern 8 note range | -2 to 2 | 0 |
| Pattern 8 minorness | 0 count to 4 count | 0 count |
