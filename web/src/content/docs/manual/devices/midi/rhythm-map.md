---
title: "Rhythm Map"
description: "Rhythm Map"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

A MIDI device: plays drum patterns from a map of rhythms as the song plays. Where on the map it stands sets how plain or syncopated its kick and snare are, a density for each of four drums thins or fills them, and each drum has a mirror that plays between its hits. The track's own notes pass through.

[Rhythm Map on the website](/solmara/write/#rhythm-map)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Map | Straight, Floor, Broken, Half-time, Sparse, Clave | Straight |
| X | 0 count to 15 count | 0 count |
| Y | 0 count to 15 count | 0 count |
| Rate | 1/32, 1/16T, 1/16, 1/8T, 1/8, 1/4T, 1/4 | 1/16 |
| Shuffle | 50% to 75% | 50% |
| Reset | 1 count to 64 count | 64 count |
| Kick density | 0% to 100% | 50% |
| Kick mirror | 0 count to 127 count | 0 count |
| Kick lock | Off, On | Off |
| Kick lock X | 0 count to 15 count | 0 count |
| Kick lock Y | 0 count to 15 count | 0 count |
| Kick note | 0 MIDI note to 127 MIDI note | 36 MIDI note |
| Kick mirror note | 0 MIDI note to 127 MIDI note | 45 MIDI note |
| Snare density | 0% to 100% | 50% |
| Snare mirror | 0 count to 127 count | 0 count |
| Snare lock | Off, On | Off |
| Snare lock X | 0 count to 15 count | 0 count |
| Snare lock Y | 0 count to 15 count | 0 count |
| Snare note | 0 MIDI note to 127 MIDI note | 38 MIDI note |
| Snare mirror note | 0 MIDI note to 127 MIDI note | 37 MIDI note |
| Hat density | 0% to 100% | 50% |
| Hat mirror | 0 count to 127 count | 0 count |
| Hat lock | Off, On | Off |
| Hat lock X | 0 count to 15 count | 0 count |
| Hat lock Y | 0 count to 15 count | 0 count |
| Hat note | 0 MIDI note to 127 MIDI note | 42 MIDI note |
| Hat mirror note | 0 MIDI note to 127 MIDI note | 46 MIDI note |
| Perc density | 0% to 100% | 50% |
| Perc mirror | 0 count to 127 count | 0 count |
| Perc lock | Off, On | Off |
| Perc lock X | 0 count to 15 count | 0 count |
| Perc lock Y | 0 count to 15 count | 0 count |
| Perc note | 0 MIDI note to 127 MIDI note | 39 MIDI note |
| Perc mirror note | 0 MIDI note to 127 MIDI note | 75 MIDI note |
| Shuffle source | Local, Global | Local |
