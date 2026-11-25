---
title: "Note Repeater"
description: "Note Repeater"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

A MIDI device: repeats each note, as a delay repeats sound, up to sixteen times, each repeat a step later, moved in pitch from the one before and louder or softer. With no time between them the repeats stack into chords.

[Note Repeater on the website](/solmara/write/#note-repeater)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Tempo sync | Off, On | On |
| Step | 16 choices: 1/128, 1/64T, 1/64, 1/32T, … | 1/8 |
| Step time | 0 ms to 1000 ms | 250 ms |
| Repeats | 1 count to 16 count | 3 count |
| Velocity | 10% to 200% | 70% |
| Pitch | -12 st to 12 st | 0 st |
