---
title: "Note Filter"
description: "Note Filter"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A MIDI device: lets through the notes within a range of keys and of velocities, or outside it, and moves, fixes or scales their pitch, octave, velocity on a curve, and length, limits how many sound at once, and holds them.

[Note Filter on the website](/solmara/write/#note-filter)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Mode | Filter > Adjust, Adjust > Filter, Filter > Adjust (split) | Filter > Adjust |
| Pitch range | Off, On | Off |
| Lowest key | 0 MIDI note to 127 MIDI note | 0 MIDI note |
| Highest key | 0 MIDI note to 127 MIDI note | 127 MIDI note |
| Flip key range | Off, On | Off |
| Velocity range | Off, On | Off |
| Lowest velocity | 1 count to 127 count | 1 count |
| Highest velocity | 1 count to 127 count | 127 count |
| Flip velocity range | Off, On | Off |
| Pitch | Off, On | Off |
| Pitch mode | Offset, Fixed | Offset |
| Pitch offset | -24 st to 24 st | 0 st |
| Fixed key | 0 MIDI note to 127 MIDI note | 60 MIDI note |
| Octave | Off, On | Off |
| Octaves | -3 oct to 3 oct | 0 oct |
| Velocity | Off, On | Off |
| Velocity mode | Offset, Fixed, Scale | Offset |
| Velocity offset | -127 count to 127 count | 0 count |
| Fixed velocity | 1 count to 127 count | 100 count |
| Velocity scale | 1% to 800% | 100% |
| Note length | Off, On | Off |
| Length mode | Min, Max, Fixed | Min |
| Length | 13 choices: Pulse, 1/128, 1/64, 1/32, … | 1/16 |
| Restrict poly | Off, On | Off |
| Voices | 1 count to 16 count | 1 count |
| Restrict mode | First Note, Low Note, High Note, Last Note | Last Note |
| Hold | Off, On | Off |
| Hold mode | Hold All, Latch, Chord | Hold All |
