---
title: "Pattern Mutator"
description: "Pattern Mutator"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

A MIDI device: plays a polyphonic pattern of steps, and makes variations of it at a click: notes moved by octaves and fifths or further, swapped, thinned or filled, lengthened, and accented. Eight patterns, transposed from the keys.

[Pattern Mutator on the website](/solmara/write/#pattern-mutator)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Playback mode | SEQ, SEQ+KEY, KEY | SEQ |
| Transpose | Off, On | Off |
| Scale velocity | Off, On | Off |
| Pattern | 1 count to 8 count | 1 count |
| Play mutation | Off, On | Off |
| Local shuffle | 50% to 75% | 66% |
| Octave+Pitch | 0% to 100% | 30% |
| Swap | 0% to 100% | 20% |
| Density | 0% to 100% | 30% |
| Note length | 0% to 100% | 20% |
| Velocity (accent) | 0% to 100% | 30% |
| Shuffle source | Local, Global | Local |
