---
title: "Anchor Arpeggiator"
description: "Anchor Arpeggiator"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**An emulation of a digital original,** modelled on the player devices of another DAW.

A MIDI device: an arpeggio of two parts, an anchor that plays one to three of the chord's notes in a sparse, repeating rhythm, and a movement that runs through the others between them in one of forty shapes, as thick as its density says, with rhythm and octave modifiers chosen by a seed.

[Anchor Arpeggiator on the website](/solmara/write/#anchor-arpeggiator)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Hold | Off, On | Off |
| Hold mode | Hold All, Latch, Chord, Toggle | Latch |
| Clear | 0 count to 9999 count | 0 count |
| Play mode | Retrig, Sync to Song | Retrig |
| Shuffle | 50% to 75% | 50% |
| Rate | 11 choices: 1/64, 1/32, 1/16T, 1/16, … | 1/16 |
| Steps | 4 count to 64 count | 16 count |
| Anchor | Off, On | On |
| Anchor pattern | 0 count to 64 count | 1 count |
| Anchor length | 10% to 410% | 100% |
| Anchor velocity mode | Offset, Fixed | Offset |
| Anchor velocity offset | -127 velocity to 127 velocity | 0 velocity |
| Anchor fixed velocity | 1 velocity to 127 velocity | 100 velocity |
| Anchor octave | -2 oct to 2 oct | 0 oct |
| Movement | Off, On | On |
| Shape | 1 count to 40 count | 1 count |
| Density | 0% to 100% | 100% |
| Shift rhythm | -16 to 16 | 0 |
| Movement length | 10% to 410% | 75% |
| Movement velocity mode | Offset, Fixed | Offset |
| Movement velocity offset | -127 velocity to 127 velocity | 0 velocity |
| Movement fixed velocity | 1 velocity to 127 velocity | 100 velocity |
| Movement octave | -2 oct to 2 oct | 0 oct |
| Humanize | 0% to 100% | 0% |
| Rhythm modifier | Off, On | Off |
| Rhythm function | Mute, Mute or Double, Double, Double or Triple, Triple, Triple or Quad, Quad | Double |
| Doubled steps | Repeat, Arpeggiate | Repeat |
| Rhythm amount | 0% to 100% | 25% |
| Rhythm movement only | Off, On | Off |
| Rhythm seed | 0 count to 9999 count | 1 count |
| Octave modifier | Off, On | Off |
| Octave function | -2, -2 or -1, -1, -1 or +1, +1, +1 or +2, +2 | +1 |
| Octave amount | 0% to 100% | 25% |
| Octave movement only | Off, On | Off |
| Octave seed | 0 count to 9999 count | 1 count |
| Shuffle source | Local, Global | Local |
