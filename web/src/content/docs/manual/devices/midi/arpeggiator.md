---
title: "Arpeggiator"
description: "Arpeggiator"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A MIDI device: plays the notes held in a shape (up, down, played, chord, random...) or a drawn pattern whose rows are the held notes, so it follows any chord, with chance, ratchets, conditions, scale steps, swing and a range of shifted passes; twelve pattern slots. Vintergatan's arp is the same.

[Arpeggiator on the website](/solmara/write/#arpeggiator)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Shape | 16 choices: Pattern, Up, Down, Up/Down, … | Up |
| Rate | 13 choices: 1/1, 1/2, 1/4, 1/8, … | 1/16 |
| Gate | 1% to 200% | 100% |
| Range | 1 count to 8 count | 1 count |
| Shift | -48 semitones to 48 semitones | 12 semitones |
| Latch | Off, On | Off |
| Swing | 0 linear to 1 linear | 0 linear |
| Seed | 0 count to 999 count | 1 count |
| Restart | After silence, Each note, Never | After silence |
| Scale | 15 choices: Project, Major, Minor, Dorian, … | Project |
| Root | 12 choices: C, C#, D, D#, … | C |
| Pattern slot | 1 count to 12 count | 1 count |
