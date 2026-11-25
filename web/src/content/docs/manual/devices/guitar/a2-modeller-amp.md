---
title: "A2 Modeller Amp"
description: "A Neural Amp Modeler capture of an amp, a pedal or a rig, played from its .nam file."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A tone captured with Neural Amp Modeler, an amp, a pedal or a whole rig, played from its .nam file (NAM's A2, Lite and Full, and A1's WaveNets and LSTMs), which is kept with the project; with an input gain, a calibration to the level the tone was captured at, the output levelled by its loudness, and an output gain. It holds the audio back by 64 frames, and 128 where the model's rate is not the project's.

[A2 Modeller Amp on the website](/solmara/guitar/#a2-modeller-amp)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Input | -24 dB to 24 dB | 0 dB |
| Calibrate | Off, On | Off |
| Interface | 0 dBu to 30 dBu | 12 dBu |
| Size | Lite, Full | Full |
| Normalize | Off, On | On |
| Output | -24 dB to 24 dB | 0 dB |
