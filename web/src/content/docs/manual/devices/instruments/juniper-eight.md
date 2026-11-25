---
title: "Juniper Eight"
description: "Eight-voice polysynth in the style of the early-1980s Japanese flagships: brass, pads, sync leads and split or layered patches."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A modelled eight-voice polysynth of the early 1980s, built from its circuit and held to a reference by measurement: each voice two oscillators, the first with its triangle, saw, pulse and square and cross-modulation from the second, the second with its sine, saw, pulse and noise, sync either way, a source mix into a high-pass and a four-pole low-pass switchable to two poles that sings at full resonance, and an amplifier, on two envelopes that follow the keys if asked. An LFO with its delay to the oscillators, the pulse width, the filter and the amplifier. An upper and a lower patch, played whole, dual or split; solo, unison and two poly modes; hold, portamento and an arpeggiator.

[Juniper Eight on the website](/solmara/instruments/juniper-eight/)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| LFO rate | 0 to 10 | 5 |
| LFO delay | 0 to 10 | 0 |
| LFO waveform | Sine, Saw, Square, Random | Sine |
| VCO mod LFO | 0 to 10 | 0 |
| VCO mod ENV-1 | 0 to 10 | 0 |
| VCO mod to | VCO-1, VCO-1 & 2, VCO-2 | VCO-1 & 2 |
| Cross mod | 0 to 10 | 0 |
| VCO-1 range | 64', 32', 16', 8', 4', 2' | 8' |
| VCO-1 waveform | Triangle, Saw, Pulse, Square | Saw |
| Sync | Off, VCO-1 to 2, VCO-2 to 1 | Off |
| VCO-2 coarse | -12 semitones to 24 semitones | 0 semitones |
| VCO-2 fine | -100 cents to 100 cents | 6 cents |
| VCO-2 low frequency | Off, On | Off |
| VCO-2 waveform | Sine, Saw, Pulse, Noise | Saw |
| Pulse width | 0 to 10 | 0 |
| Pulse width by | ENV-1, Manual, LFO | Manual |
| Source mix | 0 to 10 | 5 |
| High-pass | 0 to 10 | 0 |
| Cutoff | 0 to 10 | 6 |
| Resonance | 0 to 10 | 0 |
| Slope | 12 dB, 24 dB | 24 dB |
| VCF envelope | 0 to 10 | 3 |
| VCF envelope from | ENV-1, ENV-2 | ENV-1 |
| VCF LFO | 0 to 10 | 0 |
| VCF key follow | 0 to 10 | 3 |
| VCA level | 0 to 10 | 10 |
| VCA LFO | 0 to 10 | 0 |
| ENV-1 attack | 0 to 10 | 0 |
| ENV-1 decay | 0 to 10 | 4 |
| ENV-1 sustain | 0 to 10 | 3 |
| ENV-1 release | 0 to 10 | 3 |
| ENV-1 key follow | Off, On | Off |
| ENV-1 polarity | Normal, Inverted | Normal |
| ENV-2 attack | 0 to 10 | 0 |
| ENV-2 decay | 0 to 10 | 4 |
| ENV-2 sustain | 0 to 10 | 10 |
| ENV-2 release | 0 to 10 | 3 |
| ENV-2 key follow | Off, On | Off |
| Key mode | Whole, Dual, Split | Whole |
| Split point | 24 note to 108 note | 60 note |
| Balance | -5 to 5 | 0 |
| Assign mode | Solo, Unison, Poly 1, Poly 2 | Poly 1 |
| Hold | Off, On | Off |
| Portamento | 0 to 10 | 0 |
| Portamento on | Off, On | Off |
| Unison detune | 0 to 10 | 2 |
| Bender to VCO-1 | Off, On | On |
| Bender to VCO-2 | Off, On | On |
| Bender VCO range | 0 semitones to 24 semitones | 2 semitones |
| Bender to VCF | 0 to 10 | 0 |
| Bender | -1 to 1 | 0 |
| Mod lever to VCO | 0 to 10 | 3 |
| Mod lever to VCF | 0 to 10 | 0 |
| Mod lever | 0 to 1 | 0 |
| Arpeggiator | Off, On | Off |
| Arpeggiator mode | Up, Down, Up & down, Random | Up |
| Arpeggiator range | 1, 2, 3, 4 | 1 |
| Arpeggiator rate | 0 to 10 | 5 |
| Arpeggiator clock | Free, Tempo | Free |
| Master tune | -5 to 5 | 0 |
| Volume | 0 to 10 | 7 |
| Quality | Light, Full | Full |
| Lower LFO rate | 0 to 10 | 5 |
| Lower LFO delay | 0 to 10 | 0 |
| Lower LFO waveform | Sine, Saw, Square, Random | Sine |
| Lower VCO mod LFO | 0 to 10 | 0 |
| Lower VCO mod ENV-1 | 0 to 10 | 0 |
| Lower VCO mod to | VCO-1, VCO-1 & 2, VCO-2 | VCO-1 & 2 |
| Lower Cross mod | 0 to 10 | 0 |
| Lower VCO-1 range | 64', 32', 16', 8', 4', 2' | 8' |
| Lower VCO-1 waveform | Triangle, Saw, Pulse, Square | Saw |
| Lower Sync | Off, VCO-1 to 2, VCO-2 to 1 | Off |
| Lower VCO-2 coarse | -12 semitones to 24 semitones | 0 semitones |
| Lower VCO-2 fine | -100 cents to 100 cents | 6 cents |
| Lower VCO-2 low frequency | Off, On | Off |
| Lower VCO-2 waveform | Sine, Saw, Pulse, Noise | Saw |
| Lower Pulse width | 0 to 10 | 0 |
| Lower Pulse width by | ENV-1, Manual, LFO | Manual |
| Lower Source mix | 0 to 10 | 5 |
| Lower High-pass | 0 to 10 | 0 |
| Lower Cutoff | 0 to 10 | 6 |
| Lower Resonance | 0 to 10 | 0 |
| Lower Slope | 12 dB, 24 dB | 24 dB |
| Lower VCF envelope | 0 to 10 | 3 |
| Lower VCF envelope from | ENV-1, ENV-2 | ENV-1 |
| Lower VCF LFO | 0 to 10 | 0 |
| Lower VCF key follow | 0 to 10 | 3 |
| Lower VCA level | 0 to 10 | 10 |
| Lower VCA LFO | 0 to 10 | 0 |
| Lower ENV-1 attack | 0 to 10 | 0 |
| Lower ENV-1 decay | 0 to 10 | 4 |
| Lower ENV-1 sustain | 0 to 10 | 3 |
| Lower ENV-1 release | 0 to 10 | 3 |
| Lower ENV-1 key follow | Off, On | Off |
| Lower ENV-1 polarity | Normal, Inverted | Normal |
| Lower ENV-2 attack | 0 to 10 | 0 |
| Lower ENV-2 decay | 0 to 10 | 4 |
| Lower ENV-2 sustain | 0 to 10 | 10 |
| Lower ENV-2 release | 0 to 10 | 3 |
| Lower ENV-2 key follow | Off, On | Off |
