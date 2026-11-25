---
title: "Granular Sampler"
description: "Granular Sampler"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

A sample played as windowed grains: position and scan, size and density, spray, pitch, freeze, stereo scatter, an amplitude envelope and LFO modulation; 16 voices and 128 grains.

[Granular Sampler on the website](/solmara/instruments/granular-sampler/)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Root note | 0 MIDI note to 127 MIDI note | 60 MIDI note |
| Level | 0 linear to 1 linear | 0.8 linear |
| Position | 0% to 100% | 50% |
| Scan speed | -2 to 2 | 1 |
| Grain size | 5 ms to 500 ms | 80 ms |
| Density | 0 grains/s to 120 grains/s | 20 grains/s |
| Position spray | 0% to 100% | 10% |
| Pitch | -24 semitones to 24 semitones | 0 semitones |
| Pitch spray | 0 semitones to 12 semitones | 0 semitones |
| Stereo scatter | 0 linear to 1 linear | 0.5 linear |
| Freeze scan | Off, On | Off |
| Attack | 0 ms to 20000 ms | 10 ms |
| Decay | 0 ms to 20000 ms | 200 ms |
| Sustain | 0 linear to 1 linear | 0.8 linear |
| Release | 0 ms to 20000 ms | 300 ms |
| LFO rate | 0.05 Hz to 20 Hz | 0.5 Hz |
| LFO to position | 0% to 100% | 0% |
| LFO to pitch | 0 semitones to 12 semitones | 0 semitones |
| LFO to density | 0 linear to 1 linear | 0 linear |
| LFO to size | 0 linear to 1 linear | 0 linear |
| Seed | 0 integer to 65535 integer | 0 integer |
| Interpolation | Linear, Cubic, Sinc | Cubic |
