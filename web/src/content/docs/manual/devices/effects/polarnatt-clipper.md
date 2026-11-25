---
title: "Polarnatt Clipper"
description: "Mastering clipper: peaks off before the limiter, in six curves."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A clipper for the master and for buses, the mastering family's: it drives the audio into a ceiling it never passes, to take the fastest peaks off before a limiter, more cleanly than a limiter can. Its algorithm is how it bends into the ceiling, from hard through soft, sine, a diode pair's and tape's to a valve's lopsided curve, its softness how far under the ceiling it starts, and it runs at once, four, or sixteen times the rate so what it makes does not fold back.

[Polarnatt Clipper on the website](/solmara/effects/#polarnatt-clipper)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Drive | 0 dB to 36 dB | 0 dB |
| Ceiling | -24 dB to 0 dB | 0 dB |
| Softness | 0 linear to 1 linear | 0.3 linear |
| Mix | 0 linear to 1 linear | 1 linear |
| Output | -24 dB to 24 dB | 0 dB |
| Algorithm | Hard, Soft, Sine, Diode, Tape, Valve | Soft |
| Oversampling | 1x, 4x, 16x | 4x |
