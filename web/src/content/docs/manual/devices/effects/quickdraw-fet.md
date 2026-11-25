---
title: "Quickdraw FET"
description: "FET limiting amp in the style of the late-1960s American studio limiters: fast, aggressive peaks for drums and vocals."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A modelled peak limiter built on a field-effect transistor: the transistor is the lower leg of a divider at the input and turns the audio down as the sidechain, which listens after it, lifts its gate. It has no threshold knob: the input knob drives the audio into a fixed threshold and the output knob makes up the level. Attack and release, both fastest at the top of their travel, with an attack from a few milliseconds down to a tenth of one, and a button for each ratio, 4, 8, 12, or 20 to 1, none of them, or all four at once, which pumps and distorts. It can listen to another track by sidechain. Modelled on the black-faced American transistor limiting amplifier of the late 1960s, the usual fast, aggressive compressor for drums, vocals, and bass.

[Quickdraw FET on the website](/solmara/effects/#quickdraw-fet)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Input | 0 to 100 | 30 |
| Output | 0 to 100 | 55 |
| Attack | 0 to 100 | 50 |
| Release | 0 to 100 | 50 |
| Ratio | Off, 4:1, 8:1, 12:1, 20:1, All | 4:1 |
| Quality | Standard, Ultra | Standard |
