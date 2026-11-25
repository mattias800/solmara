---
title: "Norrsken"
description: "Virtual-analogue polysynth in the style of the late-1990s Scandinavian keyboards: leads, sync sweeps, and morphing pads."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A modelled twenty-voice virtual-analogue synthesizer from Stockholm, of the turn of the century: its digital engine held to a reference by measurement and blind listening: two oscillators with sync, linear FM and ring modulation, a filter of five types with distortion, three envelopes, two LFOs (the second an arpeggiator or an echo), velocity and wheel morphs on every knob, unison, and the wheel, the stick, aftertouch and a pedal as the hardware takes them. Imports the hardware's documented SysEx programs.

[Norrsken on the website](/solmara/instruments/norrsken/)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Osc 2 pitch | -60 st to 60 st | 0 st |
| Osc 2 fine | -64 to 63 | 0 |
| Oscillator balance | -64 to 63 | -64 |
| Cutoff | 0 to 127 | 100 |
| Resonance | 0 to 127 | 0 |
| Filter envelope amount | 0 to 127 | 0 |
| Pulse width | 0 to 127 | 0 |
| FM / ring tune | 0 to 127 | 0 |
| Filter attack | 0 to 127 | 0 |
| Filter decay | 0 to 127 | 64 |
| Filter sustain | 0 to 127 | 0 |
| Filter release | 0 to 127 | 32 |
| Amp attack | 0 to 127 | 0 |
| Amp decay | 0 to 127 | 64 |
| Amp sustain | 0 to 127 | 127 |
| Amp release | 0 to 127 | 16 |
| Portamento | 0 to 127 | 0 |
| Program gain | 0 to 127 | 100 |
| Mod attack | 0 to 127 | 0 |
| Mod decay | 0 to 127 | 64 |
| Mod envelope amount | -64 to 63 | 0 |
| LFO 1 rate | 0 to 127 | 64 |
| LFO 1 amount | 0 to 127 | 0 |
| LFO 2 rate | 0 to 127 | 64 |
| LFO 2 amount / arp range | 0 to 127 | 0 |
| Pitch morph | -128 to 127 | 0 |
| Fine morph | -128 to 127 | 0 |
| Balance morph | -128 to 127 | 0 |
| Cutoff morph | -128 to 127 | 0 |
| Resonance morph | -128 to 127 | 0 |
| Filter amount morph | -128 to 127 | 0 |
| Width morph | -128 to 127 | 0 |
| FM morph | -128 to 127 | 0 |
| Filter attack morph | -128 to 127 | 0 |
| Filter decay morph | -128 to 127 | 0 |
| Filter sustain morph | -128 to 127 | 0 |
| Filter release morph | -128 to 127 | 0 |
| Amp attack morph | -128 to 127 | 0 |
| Amp decay morph | -128 to 127 | 0 |
| Amp sustain morph | -128 to 127 | 0 |
| Amp release morph | -128 to 127 | 0 |
| Portamento morph | -128 to 127 | 0 |
| Gain morph | -128 to 127 | 0 |
| Mod attack morph | -128 to 127 | 0 |
| Mod decay morph | -128 to 127 | 0 |
| Mod amount morph | -128 to 127 | 0 |
| LFO 1 rate morph | -128 to 127 | 0 |
| LFO 1 amount morph | -128 to 127 | 0 |
| LFO 2 rate morph | -128 to 127 | 0 |
| LFO 2 amount morph | -128 to 127 | 0 |
| Osc 1 waveform | Pulse, Saw, Triangle, Sine | Saw |
| Osc 2 waveform | Pulse, Saw, Triangle, Noise | Saw |
| Oscillator sync | Off, On | Off |
| Ring modulation | Off, On | Off |
| Filter distortion | Off, On | Off |
| Filter type | LP 12, LP 24, HP 24, Band-pass, Notch + LP | LP 12 |
| Osc 2 keyboard tracking | Off, On | On |
| Filter keyboard tracking | Off, One third, Two thirds, Full | Off |
| LFO 1 waveform | Random, Saw, Triangle, Square, Smooth random | Triangle |
| LFO 1 destination | Pulse width, Filter, Pitch 2, Pitch 1+2, FM | Pitch 1+2 |
| Voice mode | Poly, Legato, Mono | Poly |
| Wheel destination | Filter, FM, Pitch 2, LFO 1 amount, Morph | Morph |
| Unison | Off, On | Off |
| Mod envelope destination | Pitch 2, FM, Pulse width, Off | Off |
| Automatic portamento | Off, On | Off |
| Filter envelope velocity | Off, On | Off |
| Octave shift | -2, -1, 0, +1, +2 | 0 |
| LFO 2 / arpeggiator | 9 choices: Arp down, Arp up, Arp up/down, Amp, … | Off |
| Unison detune | 0 to 8 | 2 |
| Output mode | Auto stereo, Mono, Alternate voices | Auto stereo |
| LFO 1 clock sync | Off, 2/1, 1/1, 1/2, 1/4, 1/8, 1/8 triplet, 1/16 | Off |
| LFO 2 clock sync | Off, 2/1, 1/1, 1/2, 1/4, 1/8, 1/8 triplet, 1/16 | Off |
| Modulation wheel | 0 linear to 1 linear | 0 linear |
| Pitch stick | -1 to 1 | 0 |
| Pitch bend range | 0 st to 48 st | 2 st |
| Master tuning | -99 cents to 99 cents | 0 cents |
| Aftertouch | 0 linear to 1 linear | 0 linear |
| Aftertouch amount | Off, 1, 2, 3, 4, 5, 6, 7 | Off |
| Aftertouch destination | LFO 1 amount, LFO 2 amount, Filter, FM, Osc 2 pitch | LFO 1 amount |
| Expression pedal | 0 linear to 1 linear | 0 linear |
| Expression amount | Off, 1, 2, 3, 4, 5, 6, 7 | Off |
| Expression destination | LFO 1 amount, LFO 2 amount, Filter, FM, Osc 2 pitch | LFO 1 amount |
| Arpeggiator hold | Off, On | Off |
