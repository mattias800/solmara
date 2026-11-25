---
title: "1978 Digital Hall"
description: "1970s digital hall reverb: lush, dark halls and plates for vocals and snares."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**An emulation of a digital original,** modelled on the late-1970s American digital reverb whose halls and plates were on every record of the 1980s.

A digital hall reverb of the late 1970s, modelled as its algorithm: a network of delays and diffusers that recirculate at a low sample rate between steep converter filters, so the tail is dark above 8 kHz and grainy far down, with its delays wandering slowly so it never rings. Nine programs: two small halls, a large hall, a chamber, a room, three plates, and a chorus. Bass and mid decay times split at a crossover, a treble decay, depth (how far back the sound sits), pre-delay, diffusion, wander and chorus for the delays' motion, the converters' hiss, mix, and output. Edits never stop the tail.

[1978 Digital Hall on the website](/solmara/effects/#1978-digital-hall)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Program | 9 choices: Small Hall A, Small Hall B, Large Hall, Chamber, … | Small Hall A |
| Bass | 0.6 s to 70 s | 3 s |
| Mid | 0.6 s to 70 s | 2 s |
| Crossover | 100 Hz to 10900 Hz | 540 Hz |
| Treble | 100 Hz to 10900 Hz | 6600 Hz |
| Depth | 0 count to 71 count | 23 count |
| Pre-delay | 0 ms to 300 ms | 24 ms |
| Diffusion | 0 count to 63 count | 28 count |
| Wander | 0 count to 15 count | 2 count |
| Chorus | 0 count to 15 count | 1 count |
| Noise | Off, On | Off |
| Mix | 0 linear to 1 linear | 0.3 linear |
| Output | -24 dB to 24 dB | 0 dB |
