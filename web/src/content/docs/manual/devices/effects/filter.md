---
title: "Filter"
description: "Filter"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A modelled analogue filter: a transistor ladder, a squelchy diode ladder, a screaming Sallen-Key, a polished OTA cascade, or a smooth state variable, driven into saturation and ringing at high resonance, as low-, band-, or high-pass, with an LFO and an envelope follower to move its cutoff. The follower listens to the filter's input or another track by sidechain.

[Filter on the website](/solmara/effects/#filter)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Model | Transistor ladder, Diode ladder, Sallen-Key, OTA cascade, State variable, Comb, Phaser, Formant | Transistor ladder |
| Type | Low 24, Low 12, Band 24, Band 12, High 24, High 12 | Low 24 |
| Cutoff | 20 Hz to 20000 Hz | 2000 Hz |
| Resonance | 0 linear to 1 linear | 0.3 linear |
| Drive | 0 dB to 36 dB | 0 dB |
| LFO depth | 0 octaves to 4 octaves | 0 octaves |
| LFO rate | 0.05 Hz to 20 Hz | 1 Hz |
| LFO sync | Off, On | Off |
| LFO division | 13 choices: 1/32, 1/16T, 1/16, 1/8T, … | 1/4 |
| LFO shape | Sine, Triangle, Saw up, Saw down, Square, Random | Sine |
| LFO spread | 0 linear to 1 linear | 0 linear |
| Follow | -4 octaves to 4 octaves | 0 octaves |
| Follow attack | 0.1 ms to 500 ms | 10 ms |
| Follow release | 5 ms to 2000 ms | 200 ms |
| Mix | 0 linear to 1 linear | 1 linear |
| Output | -24 dB to 24 dB | 0 dB |
| Morph | 0 linear to 2 linear | 0 linear |
