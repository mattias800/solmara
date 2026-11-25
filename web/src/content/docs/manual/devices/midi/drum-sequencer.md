---
title: "Drum Sequencer"
description: "Drum Sequencer"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A MIDI device: plays eight channels of sixteen steps as the song plays, each a key of the instrument such as a drum rack's pad, with eight patterns to choose between. Each channel has its own length, speed, direction and slide, and each step a velocity, repeats, triplets or a flam, and a probability. The track's own notes pass through.

[Drum Sequencer on the website](/solmara/write/#drum-sequencer)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Pattern | 1 count to 8 count | 1 count |
| Shuffle source | Local, Global | Local |
