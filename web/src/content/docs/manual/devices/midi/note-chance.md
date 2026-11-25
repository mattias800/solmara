---
title: "Note Chance"
description: "Note Chance"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A MIDI device: lets notes through by a sequence of yes and no, or by chance, and by chance sets or moves their pitch, velocity and length within ranges, each with a chance of its own or one for all.

[Note Chance on the website](/solmara/write/#note-chance)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Conditional | Off, On | Off |
| Steps | 2 count to 8 count | 4 count |
| Reset | Reset on Play, Reset 1 sec, Reset 5 sec, No Reset | Reset on Play |
| Chord | Off, On | Off |
| Probability | Off, On | Off |
| Pass chance | 0% to 100% | 50% |
| Random pitch | Off, On | Off |
| Pitch mode | Set To, Octaves +/-, Octaves +, Semitones +/-, Between | Between |
| Set key | 0 MIDI note to 127 MIDI note | 60 MIDI note |
| Octaves | 1 count to 8 count | 1 count |
| Semitones | 1 count to 127 count | 7 count |
| Lowest key | 0 MIDI note to 127 MIDI note | 48 MIDI note |
| Highest key | 0 MIDI note to 127 MIDI note | 72 MIDI note |
| Pitch chance | 0% to 100% | 50% |
| Random velocity | Off, On | Off |
| Velocity mode | Set To, Offset +/-, Between | Offset +/- |
| Set velocity | 1 count to 127 count | 100 count |
| Velocity offset | 1 count to 127 count | 20 count |
| Lowest velocity | 1 count to 127 count | 40 count |
| Highest velocity | 1 count to 127 count | 110 count |
| Velocity chance | 0% to 100% | 50% |
| Random length | Off, On | Off |
| Length mode | Set To, Between | Set To |
| Set length | 13 choices: Pulse, 1/128, 1/64, 1/32, … | 1/16 |
| Shortest | 13 choices: Pulse, 1/128, 1/64, 1/32, … | 1/32 |
| Longest | 13 choices: Pulse, 1/128, 1/64, 1/32, … | 1/4 |
| Length chance | 0% to 100% | 50% |
| Sync chance | Off, On | Off |
| Shared chance | 0% to 100% | 50% |
