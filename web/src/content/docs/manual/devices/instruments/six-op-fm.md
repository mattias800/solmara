---
title: "Six-Op FM"
description: "Six-operator FM synth in the style of the 1980s Japanese digital keyboards: bells, electric pianos, basses and brass."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**An emulation of a digital original,** modelled on the early-1980s Japanese six-operator FM keyboard that brought digital synthesis to every studio.

A modelled six-operator FM synthesizer of 1983, its digital engine's behaviour held to a reference by measurement: six sine operators in one of 32 algorithms, each at a ratio of the key's pitch or a fixed frequency, with its output level and an envelope of four rates and four levels; one operator feeds itself back. Sixteen voices.

[Six-Op FM on the website](/solmara/instruments/six-op-fm/)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Algorithm | 1 to 32 | 32 |
| Feedback | 0 to 7 | 0 |
| Oscillator key sync | Off, On | On |
| Volume | -60 dB to 24 dB | 0 dB |
| Transpose | -24 semitones to 24 semitones | 0 semitones |
| Pitch EG rate 1 | 0 to 99 | 99 |
| Pitch EG rate 2 | 0 to 99 | 99 |
| Pitch EG rate 3 | 0 to 99 | 99 |
| Pitch EG rate 4 | 0 to 99 | 99 |
| Pitch EG level 1 | 0 to 99 | 50 |
| Pitch EG level 2 | 0 to 99 | 50 |
| Pitch EG level 3 | 0 to 99 | 50 |
| Pitch EG level 4 | 0 to 99 | 50 |
| LFO speed | 0 to 99 | 35 |
| LFO delay | 0 to 99 | 0 |
| LFO pitch depth | 0 to 99 | 0 |
| LFO amplitude depth | 0 to 99 | 0 |
| LFO key sync | Off, On | On |
| LFO wave | Triangle, Saw down, Saw up, Square, Sine, Sample and hold | Triangle |
| Pitch sensitivity | 0 to 7 | 3 |
| Mono | Poly, Mono | Poly |
| Portamento time | 0 to 99 | 0 |
| Portamento mode | Fingered, Full time | Fingered |
| DAC | Vintage, Clean | Vintage |
| Feedback steps | Six-op, Four-op | Six-op |
| Reverb rate | 0 to 99 | 0 |
| Wheel to pitch | 0 to 99 | 0 |
| Wheel to amplitude | 0 to 99 | 0 |
| Breath to pitch | 0 to 99 | 0 |
| Breath to amplitude | 0 to 99 | 0 |
| Foot to pitch | 0 to 99 | 0 |
| Foot to amplitude | 0 to 99 | 0 |
| Operator 1 | Off, On | On |
| Operator 1 output level | 0 to 99 | 99 |
| Operator 1 frequency mode | Ratio, Fixed | Ratio |
| Operator 1 coarse | 0 to 31 | 1 |
| Operator 1 fine | 0 to 99 | 0 |
| Operator 1 detune | -7 to 7 | 0 |
| Operator 1 rate 1 | 0 to 99 | 99 |
| Operator 1 rate 2 | 0 to 99 | 99 |
| Operator 1 rate 3 | 0 to 99 | 99 |
| Operator 1 rate 4 | 0 to 99 | 70 |
| Operator 1 level 1 | 0 to 99 | 99 |
| Operator 1 level 2 | 0 to 99 | 99 |
| Operator 1 level 3 | 0 to 99 | 99 |
| Operator 1 level 4 | 0 to 99 | 0 |
| Operator 1 break point | 0 to 99 | 39 |
| Operator 1 left depth | 0 to 99 | 0 |
| Operator 1 right depth | 0 to 99 | 0 |
| Operator 1 left curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 1 right curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 1 rate scaling | 0 to 7 | 0 |
| Operator 1 amplitude sensitivity | 0 to 3 | 0 |
| Operator 1 velocity sensitivity | 0 to 7 | 0 |
| Operator 1 wave | Sine, Squared, Half, Half squared, Double, Double squared, Humps, Humps squared | Sine |
| Operator 2 | Off, On | On |
| Operator 2 output level | 0 to 99 | 0 |
| Operator 2 frequency mode | Ratio, Fixed | Ratio |
| Operator 2 coarse | 0 to 31 | 1 |
| Operator 2 fine | 0 to 99 | 0 |
| Operator 2 detune | -7 to 7 | 0 |
| Operator 2 rate 1 | 0 to 99 | 99 |
| Operator 2 rate 2 | 0 to 99 | 99 |
| Operator 2 rate 3 | 0 to 99 | 99 |
| Operator 2 rate 4 | 0 to 99 | 70 |
| Operator 2 level 1 | 0 to 99 | 99 |
| Operator 2 level 2 | 0 to 99 | 99 |
| Operator 2 level 3 | 0 to 99 | 99 |
| Operator 2 level 4 | 0 to 99 | 0 |
| Operator 2 break point | 0 to 99 | 39 |
| Operator 2 left depth | 0 to 99 | 0 |
| Operator 2 right depth | 0 to 99 | 0 |
| Operator 2 left curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 2 right curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 2 rate scaling | 0 to 7 | 0 |
| Operator 2 amplitude sensitivity | 0 to 3 | 0 |
| Operator 2 velocity sensitivity | 0 to 7 | 0 |
| Operator 2 wave | Sine, Squared, Half, Half squared, Double, Double squared, Humps, Humps squared | Sine |
| Operator 3 | Off, On | On |
| Operator 3 output level | 0 to 99 | 0 |
| Operator 3 frequency mode | Ratio, Fixed | Ratio |
| Operator 3 coarse | 0 to 31 | 1 |
| Operator 3 fine | 0 to 99 | 0 |
| Operator 3 detune | -7 to 7 | 0 |
| Operator 3 rate 1 | 0 to 99 | 99 |
| Operator 3 rate 2 | 0 to 99 | 99 |
| Operator 3 rate 3 | 0 to 99 | 99 |
| Operator 3 rate 4 | 0 to 99 | 70 |
| Operator 3 level 1 | 0 to 99 | 99 |
| Operator 3 level 2 | 0 to 99 | 99 |
| Operator 3 level 3 | 0 to 99 | 99 |
| Operator 3 level 4 | 0 to 99 | 0 |
| Operator 3 break point | 0 to 99 | 39 |
| Operator 3 left depth | 0 to 99 | 0 |
| Operator 3 right depth | 0 to 99 | 0 |
| Operator 3 left curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 3 right curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 3 rate scaling | 0 to 7 | 0 |
| Operator 3 amplitude sensitivity | 0 to 3 | 0 |
| Operator 3 velocity sensitivity | 0 to 7 | 0 |
| Operator 3 wave | Sine, Squared, Half, Half squared, Double, Double squared, Humps, Humps squared | Sine |
| Operator 4 | Off, On | On |
| Operator 4 output level | 0 to 99 | 0 |
| Operator 4 frequency mode | Ratio, Fixed | Ratio |
| Operator 4 coarse | 0 to 31 | 1 |
| Operator 4 fine | 0 to 99 | 0 |
| Operator 4 detune | -7 to 7 | 0 |
| Operator 4 rate 1 | 0 to 99 | 99 |
| Operator 4 rate 2 | 0 to 99 | 99 |
| Operator 4 rate 3 | 0 to 99 | 99 |
| Operator 4 rate 4 | 0 to 99 | 70 |
| Operator 4 level 1 | 0 to 99 | 99 |
| Operator 4 level 2 | 0 to 99 | 99 |
| Operator 4 level 3 | 0 to 99 | 99 |
| Operator 4 level 4 | 0 to 99 | 0 |
| Operator 4 break point | 0 to 99 | 39 |
| Operator 4 left depth | 0 to 99 | 0 |
| Operator 4 right depth | 0 to 99 | 0 |
| Operator 4 left curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 4 right curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 4 rate scaling | 0 to 7 | 0 |
| Operator 4 amplitude sensitivity | 0 to 3 | 0 |
| Operator 4 velocity sensitivity | 0 to 7 | 0 |
| Operator 4 wave | Sine, Squared, Half, Half squared, Double, Double squared, Humps, Humps squared | Sine |
| Operator 5 | Off, On | On |
| Operator 5 output level | 0 to 99 | 0 |
| Operator 5 frequency mode | Ratio, Fixed | Ratio |
| Operator 5 coarse | 0 to 31 | 1 |
| Operator 5 fine | 0 to 99 | 0 |
| Operator 5 detune | -7 to 7 | 0 |
| Operator 5 rate 1 | 0 to 99 | 99 |
| Operator 5 rate 2 | 0 to 99 | 99 |
| Operator 5 rate 3 | 0 to 99 | 99 |
| Operator 5 rate 4 | 0 to 99 | 70 |
| Operator 5 level 1 | 0 to 99 | 99 |
| Operator 5 level 2 | 0 to 99 | 99 |
| Operator 5 level 3 | 0 to 99 | 99 |
| Operator 5 level 4 | 0 to 99 | 0 |
| Operator 5 break point | 0 to 99 | 39 |
| Operator 5 left depth | 0 to 99 | 0 |
| Operator 5 right depth | 0 to 99 | 0 |
| Operator 5 left curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 5 right curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 5 rate scaling | 0 to 7 | 0 |
| Operator 5 amplitude sensitivity | 0 to 3 | 0 |
| Operator 5 velocity sensitivity | 0 to 7 | 0 |
| Operator 5 wave | Sine, Squared, Half, Half squared, Double, Double squared, Humps, Humps squared | Sine |
| Operator 6 | Off, On | On |
| Operator 6 output level | 0 to 99 | 0 |
| Operator 6 frequency mode | Ratio, Fixed | Ratio |
| Operator 6 coarse | 0 to 31 | 1 |
| Operator 6 fine | 0 to 99 | 0 |
| Operator 6 detune | -7 to 7 | 0 |
| Operator 6 rate 1 | 0 to 99 | 99 |
| Operator 6 rate 2 | 0 to 99 | 99 |
| Operator 6 rate 3 | 0 to 99 | 99 |
| Operator 6 rate 4 | 0 to 99 | 70 |
| Operator 6 level 1 | 0 to 99 | 99 |
| Operator 6 level 2 | 0 to 99 | 99 |
| Operator 6 level 3 | 0 to 99 | 99 |
| Operator 6 level 4 | 0 to 99 | 0 |
| Operator 6 break point | 0 to 99 | 39 |
| Operator 6 left depth | 0 to 99 | 0 |
| Operator 6 right depth | 0 to 99 | 0 |
| Operator 6 left curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 6 right curve | -Lin, -Exp, +Exp, +Lin | -Lin |
| Operator 6 rate scaling | 0 to 7 | 0 |
| Operator 6 amplitude sensitivity | 0 to 3 | 0 |
| Operator 6 velocity sensitivity | 0 to 7 | 0 |
| Operator 6 wave | Sine, Squared, Half, Half squared, Double, Double squared, Humps, Humps squared | Sine |
