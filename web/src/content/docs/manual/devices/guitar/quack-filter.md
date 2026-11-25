---
title: "Quack Filter"
description: "Envelope filter in the style of the 1970s auto-wahs, through a ladder that each note opens: funk quack."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A modelled envelope filter, the auto-wah, for funk guitar, clav, bass, and synths: the four-pole transistor ladder of the classic monosynth, whose corner an envelope follower moves up by how loud the input is, so that each note opens the filter as it starts and lets it close as it dies away. Cutoff, resonance, and drive are the ladder's; amount sets how far a note opens it; the mode is slow, a swell that lingers, or fast, a snap that falls back; and a mix against the dry signal. Modelled on the low-pass effect boxes built on the synthesizer's filter.

[Quack Filter on the website](/solmara/guitar/#quack-filter)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Cutoff | 0 to 100 | 35 |
| Resonance | 0 to 100 | 50 |
| Drive | 0 to 100 | 6.977 |
| Amount | 0 to 100 | 60 |
| Mode | Slow, Fast | Fast |
| Mix | 0 to 100 | 100 |
| Output | -24 dB to 12 dB | 0 dB |
| Quality | Light, Full | Light |
