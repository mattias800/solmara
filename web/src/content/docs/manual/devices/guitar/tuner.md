---
title: "Tuner"
description: "Chromatic tuner: the note and cents of a held string."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A chromatic tuner for guitar, bass, and anything that holds a note: it shows the note it hears and how many cents sharp or flat, against a reference for A4, and passes the audio as it came or mutes it while tuning, as a tuner pedal does. It reads a steady string to within half a cent from a dropped low D up. Agents read it with the tuner command.

[Tuner on the website](/solmara/guitar/#tuner)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Reference | 430 Hz to 450 Hz | 440 Hz |
| Mute | Pass, Mute | Pass |
