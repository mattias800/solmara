---
title: "Clementine Phaser"
description: "Four-stage phaser in the style of the 1970s one-knob phaser pedals: a swirling sweep."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A modelled four-stage phaser of the one-knob pedal kind, for guitars, electric pianos, and synths: four all-pass stages, each an operational amplifier whose corner a junction field-effect transistor sets, the four gates swept together by a relaxation oscillator through the bias network, and the input summed with the fourth stage, which puts two notches in the sound that sweep up and down. The transistors' resistance goes as their gate's volts, so the sweep is not even in octaves: it passes quickly through the lows and lingers in the upper middle, and their square law adds a little even distortion on loud notes. A rate knob, as the pedal has, a depth and a mix beside it, and a switch between the earlier version and the later one, whose feedback resistor raises peaks beside the notches. Modelled on the orange phaser pedal of the mid-1970s.

[Clementine Phaser on the website](/solmara/effects/#clementine-phaser)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Rate | 0 to 100 | 40 |
| Depth | 0 to 100 | 100 |
| Mix | 0 to 100 | 50 |
| Version | Script, Block | Script |
| Output | -24 dB to 12 dB | 0 dB |
| Bias | 0 to 100 | 50 |
