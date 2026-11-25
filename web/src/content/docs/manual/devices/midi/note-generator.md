---
title: "Note Generator"
description: "Note Generator"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

A MIDI device: four lines that each play a Euclidean rhythm at a rate of their own, with pitches, velocities and lengths varied by chance about a base key, kept to a scale, frozen in a zone, and joined as chords or as one line. It plays with the song, or while a key is held, about that key.

[Note Generator on the website](/solmara/write/#note-generator)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Base key | 0 MIDI note to 127 MIDI note | 60 MIDI note |
| Global steps | 1 count to 32 count | 16 count |
| Play mode | Seq, Key | Seq |
| Master vary | 0% to 200% | 100% |
| Freeze start | 1 count to 32 count | 1 count |
| Freeze length | 0 count to 32 count | 0 count |
| Freeze cycle | 0 count to 9999 count | 0 count |
| Output mode | Poly, Mono High, Mono Low, Mono Last, Mono Line | Poly |
| To scale | Off, On | On |
| Scale key | 13 choices: C, C#, D, D#, … | Base |
| Scale | 16 choices: Major, Minor, Lydian, Mixolydian, … | Major |
| Octave | -2 oct to 2 oct | 0 oct |
| Line 1 on | Off, On | On |
| Line 1 steps | 1 count to 32 count | 16 count |
| Line 1 rate | 14 choices: 1/2, 3/8, 1/4, 3/16, … | 1/16 |
| Line 1 shift | -4 to 4 | 0 |
| Line 1 pattern | 1 count to 32 count | 8 count |
| Line 1 pattern vary | 0% to 100% | 0% |
| Line 1 bias | -100% to 100% | 0% |
| Line 1 length | 10% to 200% | 80% |
| Line 1 length vary | 0% to 100% | 0% |
| Line 1 velocity | 1 count to 127 count | 100 count |
| Line 1 velocity vary | 0% to 100% | 0% |
| Line 1 pitch vary | 0% to 100% | 50% |
| Line 1 pitch spread | -100% to 100% | 0% |
| Line 1 range high | 0 st to 24 st | 12 st |
| Line 1 range low | -24 st to 0 st | -12 st |
| Line 2 on | Off, On | Off |
| Line 2 steps | 1 count to 32 count | 16 count |
| Line 2 rate | 14 choices: 1/2, 3/8, 1/4, 3/16, … | 1/16 |
| Line 2 shift | -4 to 4 | 0 |
| Line 2 pattern | 1 count to 32 count | 6 count |
| Line 2 pattern vary | 0% to 100% | 0% |
| Line 2 bias | -100% to 100% | 0% |
| Line 2 length | 10% to 200% | 80% |
| Line 2 length vary | 0% to 100% | 0% |
| Line 2 velocity | 1 count to 127 count | 100 count |
| Line 2 velocity vary | 0% to 100% | 0% |
| Line 2 pitch vary | 0% to 100% | 50% |
| Line 2 pitch spread | -100% to 100% | 0% |
| Line 2 range high | 0 st to 24 st | 12 st |
| Line 2 range low | -24 st to 0 st | -12 st |
| Line 2 offset | -24 st to 24 st | 12 st |
| Line 3 on | Off, On | Off |
| Line 3 steps | 1 count to 32 count | 16 count |
| Line 3 rate | 14 choices: 1/2, 3/8, 1/4, 3/16, … | 1/16 |
| Line 3 shift | -4 to 4 | 0 |
| Line 3 pattern | 1 count to 32 count | 5 count |
| Line 3 pattern vary | 0% to 100% | 0% |
| Line 3 bias | -100% to 100% | 0% |
| Line 3 length | 10% to 200% | 80% |
| Line 3 length vary | 0% to 100% | 0% |
| Line 3 velocity | 1 count to 127 count | 100 count |
| Line 3 velocity vary | 0% to 100% | 0% |
| Line 3 pitch vary | 0% to 100% | 50% |
| Line 3 pitch spread | -100% to 100% | 0% |
| Line 3 range high | 0 st to 24 st | 12 st |
| Line 3 range low | -24 st to 0 st | -12 st |
| Line 3 offset | -24 st to 24 st | 7 st |
| Line 4 on | Off, On | Off |
| Line 4 steps | 1 count to 32 count | 16 count |
| Line 4 rate | 14 choices: 1/2, 3/8, 1/4, 3/16, … | 1/16 |
| Line 4 shift | -4 to 4 | 0 |
| Line 4 pattern | 1 count to 32 count | 3 count |
| Line 4 pattern vary | 0% to 100% | 0% |
| Line 4 bias | -100% to 100% | 0% |
| Line 4 length | 10% to 200% | 80% |
| Line 4 length vary | 0% to 100% | 0% |
| Line 4 velocity | 1 count to 127 count | 100 count |
| Line 4 velocity vary | 0% to 100% | 0% |
| Line 4 pitch vary | 0% to 100% | 50% |
| Line 4 pitch spread | -100% to 100% | 0% |
| Line 4 range high | 0 st to 24 st | 12 st |
| Line 4 range low | -24 st to 0 st | -12 st |
| Line 4 offset | -24 st to 24 st | -12 st |
| Shuffle | 50% to 75% | 66.667% |
| Shuffle source | Local, Global | Local |
