---
title: "Gate"
description: "Gate"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

Turns down audio below a threshold, with smooth attack and release, hold, and hysteresis. Its filtered detector can listen to another track before or after that track's fader.

[Gate on the website](/solmara/effects/#gate)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Threshold | -80 dB to 0 dB | -40 dB |
| Range | 0 dB to 80 dB | 60 dB |
| Attack | 0.1 ms to 100 ms | 5 ms |
| Hold | 0 ms to 1000 ms | 50 ms |
| Release | 1 ms to 2000 ms | 100 ms |
| Hysteresis | 0 dB to 24 dB | 3 dB |
| SC low cut | 20 Hz to 2000 Hz | 20 Hz |
| SC high cut | 100 Hz to 20000 Hz | 20000 Hz |
| SC listen | Off, On | Off |
