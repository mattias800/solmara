---
title: "Himlavalv Limiter"
description: "True-peak limiter: loud and clean, for the master and buses."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A limiter for the master and for buses, made to be heard as little as it can: nothing passes its ceiling, between the samples as on them, as the streaming services read a peak. It looks ahead so the gain is down when a peak arrives, and turns down in two parts: a slow one that holds the level that keeps coming back, so a steady tone is not bent and loud music does not pump, and a fast one that takes what is left of each peak and lets go at once, so a lone snare does not duck what follows. Its character goes from Clear to Push; its lookahead is how late it makes the audio.

[Himlavalv Limiter on the website](/solmara/effects/#himlavalv-limiter)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Input | 0 dB to 24 dB | 0 dB |
| Ceiling | -12 dBTP to 0 dBTP | -1 dBTP |
| Lookahead | 0.5 ms to 5 ms | 1.5 ms |
| Attack | 1 ms to 100 ms | 10 ms |
| Release | 10 ms to 2000 ms | 200 ms |
| Link | 0 linear to 1 linear | 1 linear |
| Character | Clear, Balanced, Loud, Push | Balanced |
| Auto release | Off, On | On |
