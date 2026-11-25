---
title: "Hush Gate"
description: "Noise gate pedal: silence between high-gain riffs."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A noise gate pedal for high-gain guitar: it shuts the hiss and hum of a driven amplifier between notes and lets each note through whole. It listens through a band of 80 Hz to 4 kHz, so neither hum nor hiss holds it open, or to another track by sidechain, such as a dry guitar before the amplifier. It opens at the threshold over the attack, smoothly, stays open for the hold once the note falls the hysteresis under the threshold, and closes over the release evenly in decibels, the way a string dies away, to the range. Put it after the drive and before the delay.

[Hush Gate on the website](/solmara/guitar/#hush-gate)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Threshold | -100 dB to 0 dB | -55 dB |
| Hysteresis | 0 dB to 24 dB | 6 dB |
| Attack | 0.1 ms to 100 ms | 1 ms |
| Hold | 0 ms to 2000 ms | 30 ms |
| Release | 1 ms to 5000 ms | 150 ms |
| Range | 0 dB to 120 dB | 90 dB |
| Output | -24 dB to 24 dB | 0 dB |
