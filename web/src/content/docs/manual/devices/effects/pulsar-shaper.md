---
title: "Pulsar Shaper"
description: "Volume shaper: a drawn duck in time with the song, as a sidechain pumps."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

A volume curve drawn over a stretch of the song, from a sixteenth to two bars, that turns a track down and up again in time: the pumping of a sidechained compressor under a kick, with no sidechain, or gates and swells. A second curve can move a filter's cutoff in the same time. Each cycle starts on the song's grid or with each note; ready shapes start it, and its curves are drawn.

[Pulsar Shaper on the website](/solmara/effects/#pulsar-shaper)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Depth | 0 linear to 1 linear | 1 linear |
| Length | 1/16, 1/8, 1/4, 1/2, 1 bar, 2 bars | 1/4 |
| Swing | 0 linear to 1 linear | 0 linear |
| Smooth | 0 ms to 20 ms | 2 ms |
| Offset | 0 linear to 1 linear | 0 linear |
| Restart on | Beat, Note | Beat |
| Moves | Volume, Filter, Both | Volume |
| Filter | Low pass, High pass | Low pass |
| Cutoff low | 20 Hz to 20000 Hz | 300 Hz |
| Cutoff high | 20 Hz to 20000 Hz | 8000 Hz |
| Resonance | 0 linear to 1 linear | 0.3 linear |
