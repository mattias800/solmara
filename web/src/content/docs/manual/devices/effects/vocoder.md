---
title: "Vocoder"
description: "Vocoder"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

Makes a carrier speak through 4 to 40 bands of an input's envelopes. Noise, external audio, the input itself, or a pitch-following oscillator; with formants, freeze, and a band patchbay.

[Vocoder on the website](/solmara/effects/#vocoder)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Carrier | Noise, External, Modulator, Pitch Tracking | Noise |
| Bands | 10 choices: 4, 8, 12, 16, … | 16 |
| Range low | 20 Hz to 18000 Hz | 80 Hz |
| Range high | 20 Hz to 18000 Hz | 12000 Hz |
| BW | 10% to 200% | 100% |
| Bank | Precise, Retro | Precise |
| Formant | -12 st to 12 st | 0 st |
| Depth | 0% to 200% | 100% |
| Attack | 0.1 ms to 1000 ms | 5 ms |
| Release | 1 ms to 30000 ms | 100 ms |
| Freeze | Off, On | Off |
| Freeze Sync | Off, 1 bar, 1/2, 1/4, 1/8, 1/16 | Off |
| Enhance | Off, On | Off |
| Unvoiced | 0% to 100% | 0% |
| Sens. | 0% to 100% | 50% |
| Detection | Slow, Fast | Fast |
| Balance | Hiss, Buzz, Blend | Hiss |
| Highs | Switched, Direct | Switched |
| Gate | -96 dB to 0 dB | -80 dB |
| Tilt | -12 dB to 12 dB | 0 dB |
| Routing | Bypass, On | Bypass |
| Channels | Mono, Stereo, L/R | Stereo |
| Width | 0% to 100% | 0% |
| Listen | Output, Modulator, Carrier | Output |
| Level | -24 dB to 24 dB | 0 dB |
| Dry/Wet | 0% to 100% | 100% |
| Downsampling | 0% to 100% | 0% |
| Density | 0% to 100% | 100% |
| Pitch low | 20 Hz to 2000 Hz | 50 Hz |
| Pitch high | 20 Hz to 2000 Hz | 1200 Hz |
| Pitch | -24 st to 24 st | 0 st |
| Waveform | Saw, Pulse 50%, Pulse 25%, Pulse 12.5% | Saw |
| Quantize | Off, Semitones, Project scale | Off |
