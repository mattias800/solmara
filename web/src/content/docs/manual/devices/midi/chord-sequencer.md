---
title: "Chord Sequencer"
description: "Chord Sequencer"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A MIDI device: sixteen chords on pads, from sets in many styles or written by hand, each lit by how well it would follow the last, played from the keys or by a progression of up to sixteen bars, with velocity, humanizing, a bass taken away or a root added, and eight patterns.

[Chord Sequencer on the website](/solmara/write/#chord-sequencer)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Pattern | 1 count to 8 count | 1 count |
| MIDI | Off, On | On |
| External trigger | Off, On | Off |
| Octave | -2 count to 2 count | 0 count |
| Flats | Off, On | On |
| Snap | Bar, 1/2, 1/4, 1/8, 1/16 | Bar |
| Shuffle source | Local, Global | Local |
| Pattern 1 set root | 12 choices: C, C#, D, D#, … | C |
| Pattern 1 velocity | Original, Fixed | Original |
| Pattern 1 velocity trim | -100% to 100% | 0% |
| Pattern 1 MIDI to velocity | Off, On | On |
| Pattern 1 humanize velocity | 0% to 100% | 0% |
| Pattern 1 humanize timing | 0% to 100% | 0% |
| Pattern 1 remove bass | Off, Auto, Below | Off |
| Pattern 1 remove below | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 1 add root bottom | Off, On | Off |
| Pattern 1 add root top | Off, On | Off |
| Pattern 1 bars | 1 count to 16 count | 4 count |
| Pattern 1 shuffle | 50% to 75% | 50% |
| Pattern 2 set root | 12 choices: C, C#, D, D#, … | C |
| Pattern 2 velocity | Original, Fixed | Original |
| Pattern 2 velocity trim | -100% to 100% | 0% |
| Pattern 2 MIDI to velocity | Off, On | On |
| Pattern 2 humanize velocity | 0% to 100% | 0% |
| Pattern 2 humanize timing | 0% to 100% | 0% |
| Pattern 2 remove bass | Off, Auto, Below | Off |
| Pattern 2 remove below | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 2 add root bottom | Off, On | Off |
| Pattern 2 add root top | Off, On | Off |
| Pattern 2 bars | 1 count to 16 count | 4 count |
| Pattern 2 shuffle | 50% to 75% | 50% |
| Pattern 3 set root | 12 choices: C, C#, D, D#, … | C |
| Pattern 3 velocity | Original, Fixed | Original |
| Pattern 3 velocity trim | -100% to 100% | 0% |
| Pattern 3 MIDI to velocity | Off, On | On |
| Pattern 3 humanize velocity | 0% to 100% | 0% |
| Pattern 3 humanize timing | 0% to 100% | 0% |
| Pattern 3 remove bass | Off, Auto, Below | Off |
| Pattern 3 remove below | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 3 add root bottom | Off, On | Off |
| Pattern 3 add root top | Off, On | Off |
| Pattern 3 bars | 1 count to 16 count | 4 count |
| Pattern 3 shuffle | 50% to 75% | 50% |
| Pattern 4 set root | 12 choices: C, C#, D, D#, … | C |
| Pattern 4 velocity | Original, Fixed | Original |
| Pattern 4 velocity trim | -100% to 100% | 0% |
| Pattern 4 MIDI to velocity | Off, On | On |
| Pattern 4 humanize velocity | 0% to 100% | 0% |
| Pattern 4 humanize timing | 0% to 100% | 0% |
| Pattern 4 remove bass | Off, Auto, Below | Off |
| Pattern 4 remove below | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 4 add root bottom | Off, On | Off |
| Pattern 4 add root top | Off, On | Off |
| Pattern 4 bars | 1 count to 16 count | 4 count |
| Pattern 4 shuffle | 50% to 75% | 50% |
| Pattern 5 set root | 12 choices: C, C#, D, D#, … | C |
| Pattern 5 velocity | Original, Fixed | Original |
| Pattern 5 velocity trim | -100% to 100% | 0% |
| Pattern 5 MIDI to velocity | Off, On | On |
| Pattern 5 humanize velocity | 0% to 100% | 0% |
| Pattern 5 humanize timing | 0% to 100% | 0% |
| Pattern 5 remove bass | Off, Auto, Below | Off |
| Pattern 5 remove below | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 5 add root bottom | Off, On | Off |
| Pattern 5 add root top | Off, On | Off |
| Pattern 5 bars | 1 count to 16 count | 4 count |
| Pattern 5 shuffle | 50% to 75% | 50% |
| Pattern 6 set root | 12 choices: C, C#, D, D#, … | C |
| Pattern 6 velocity | Original, Fixed | Original |
| Pattern 6 velocity trim | -100% to 100% | 0% |
| Pattern 6 MIDI to velocity | Off, On | On |
| Pattern 6 humanize velocity | 0% to 100% | 0% |
| Pattern 6 humanize timing | 0% to 100% | 0% |
| Pattern 6 remove bass | Off, Auto, Below | Off |
| Pattern 6 remove below | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 6 add root bottom | Off, On | Off |
| Pattern 6 add root top | Off, On | Off |
| Pattern 6 bars | 1 count to 16 count | 4 count |
| Pattern 6 shuffle | 50% to 75% | 50% |
| Pattern 7 set root | 12 choices: C, C#, D, D#, … | C |
| Pattern 7 velocity | Original, Fixed | Original |
| Pattern 7 velocity trim | -100% to 100% | 0% |
| Pattern 7 MIDI to velocity | Off, On | On |
| Pattern 7 humanize velocity | 0% to 100% | 0% |
| Pattern 7 humanize timing | 0% to 100% | 0% |
| Pattern 7 remove bass | Off, Auto, Below | Off |
| Pattern 7 remove below | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 7 add root bottom | Off, On | Off |
| Pattern 7 add root top | Off, On | Off |
| Pattern 7 bars | 1 count to 16 count | 4 count |
| Pattern 7 shuffle | 50% to 75% | 50% |
| Pattern 8 set root | 12 choices: C, C#, D, D#, … | C |
| Pattern 8 velocity | Original, Fixed | Original |
| Pattern 8 velocity trim | -100% to 100% | 0% |
| Pattern 8 MIDI to velocity | Off, On | On |
| Pattern 8 humanize velocity | 0% to 100% | 0% |
| Pattern 8 humanize timing | 0% to 100% | 0% |
| Pattern 8 remove bass | Off, Auto, Below | Off |
| Pattern 8 remove below | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Pattern 8 add root bottom | Off, On | Off |
| Pattern 8 add root top | Off, On | Off |
| Pattern 8 bars | 1 count to 16 count | 4 count |
| Pattern 8 shuffle | 50% to 75% | 50% |
