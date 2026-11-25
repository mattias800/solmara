---
title: "Kick"
description: "Kick"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A kick drum of five layers, each a body (a sine blended with a waveform and a wavetable), a click, noise, or a sample or factory click, shaped over the hit by curves of pitch, level, and place in the table, with points that follow the key and lock the phase; velocity, random, and LFO, drive, tone, and a limiter. Its layers go to bus A, bus B, or straight on, and its chains busA, busB, and master hold effects for each, the master's for what they come to.

[Kick on the website](/solmara/instruments/kick/)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Level | 0 linear to 2 linear | 0.8 linear |
| Length | 10 ms to 3000 ms | 600 ms |
| Gate | Off, On | Off |
| Root key | 0 note to 127 note | 36 note |
| Velocity | 0 linear to 1 linear | 0.5 linear |
| Velocity to pitch | 0 semitones to 12 semitones | 0 semitones |
| Velocity to drive | 0 dB to 24 dB | 0 dB |
| Random pitch | 0 cents to 100 cents | 0 cents |
| Random decay | 0 linear to 0.5 linear | 0 linear |
| LFO rate | 0.1 Hz to 40 Hz | 6 Hz |
| LFO to pitch | 0 semitones to 12 semitones | 0 semitones |
| Drive | 0 dB to 36 dB | 0 dB |
| Drive type | Soft, Hard, Valve | Soft |
| Tone | 200 Hz to 20000 Hz | 20000 Hz |
| Limiter | Off, On | On |
| Limiter release | Fast, Medium, Slow | Medium |
| Lookahead | Off, 1 ms, 3 ms | 1 ms |
| Pitch snap | Off, Notes, Scale | Off |
| Morph | 0 linear to 1 linear | 0 linear |
| Layer 1 | Off, Body, Click, Noise, Sample | Body |
| L1 level | -60 dB to 12 dB | 0 dB |
| L1 mute | Off, On | Off |
| L1 solo | Off, On | Off |
| L1 invert | Off, On | Off |
| L1 phase | 0 degrees to 360 degrees | 0 degrees |
| L1 wave | Triangle, Saw, Square | Triangle |
| L1 wave mix | 0 linear to 1 linear | 0 linear |
| L1 click noise | 0 linear to 1 linear | 0.6 linear |
| L1 filter | Low, Band, High | Band |
| L1 cutoff | 20 Hz to 20000 Hz | 6000 Hz |
| L1 resonance | 0 linear to 1 linear | 0.2 linear |
| L1 tune | -24 semitones to 24 semitones | 0 semitones |
| L1 start | 0 ms to 500 ms | 0 ms |
| L1 pan | -1 linear to 1 linear | 0 linear |
| L1 sample filter | Off, On | Off |
| L1 bus | Master, Bus A, Bus B | Master |
| L1 table | 16 choices: Basic Shapes, Pulse Width, Harmonic Build, Odd Build, … | Basic Shapes |
| L1 table mix | 0 linear to 1 linear | 0 linear |
| L1 table position | 0 linear to 1 linear | 0 linear |
| L1 decay shape | 0 linear to 1 linear | 1 linear |
| L1 factory click | 11 choices: Its sample, Felt Beater, Plastic Beater, Wood Beater, … | Its sample |
| L1 H1 ratio | 0.5 to 16 | 2 |
| L1 H1 level | -60 dB to 0 dB | -60 dB |
| L1 H1 decay | 1 ms to 3000 ms | 150 ms |
| L1 H2 ratio | 0.5 to 16 | 3 |
| L1 H2 level | -60 dB to 0 dB | -60 dB |
| L1 H2 decay | 1 ms to 3000 ms | 150 ms |
| L1 H3 ratio | 0.5 to 16 | 4 |
| L1 H3 level | -60 dB to 0 dB | -60 dB |
| L1 H3 decay | 1 ms to 3000 ms | 150 ms |
| L1 H4 ratio | 0.5 to 16 | 5 |
| L1 H4 level | -60 dB to 0 dB | -60 dB |
| L1 H4 decay | 1 ms to 3000 ms | 150 ms |
| L1 H5 ratio | 0.5 to 16 | 6 |
| L1 H5 level | -60 dB to 0 dB | -60 dB |
| L1 H5 decay | 1 ms to 3000 ms | 150 ms |
| L1 H6 ratio | 0.5 to 16 | 7 |
| L1 H6 level | -60 dB to 0 dB | -60 dB |
| L1 H6 decay | 1 ms to 3000 ms | 150 ms |
| L1 H7 ratio | 0.5 to 16 | 8 |
| L1 H7 level | -60 dB to 0 dB | -60 dB |
| L1 H7 decay | 1 ms to 3000 ms | 150 ms |
| L1 H8 ratio | 0.5 to 16 | 9 |
| L1 H8 level | -60 dB to 0 dB | -60 dB |
| L1 H8 decay | 1 ms to 3000 ms | 150 ms |
| L1 H9 ratio | 0.5 to 16 | 10 |
| L1 H9 level | -60 dB to 0 dB | -60 dB |
| L1 H9 decay | 1 ms to 3000 ms | 150 ms |
| Layer 2 | Off, Body, Click, Noise, Sample | Click |
| L2 level | -60 dB to 12 dB | 0 dB |
| L2 mute | Off, On | Off |
| L2 solo | Off, On | Off |
| L2 invert | Off, On | Off |
| L2 phase | 0 degrees to 360 degrees | 0 degrees |
| L2 wave | Triangle, Saw, Square | Triangle |
| L2 wave mix | 0 linear to 1 linear | 0 linear |
| L2 click noise | 0 linear to 1 linear | 0.6 linear |
| L2 filter | Low, Band, High | Band |
| L2 cutoff | 20 Hz to 20000 Hz | 6000 Hz |
| L2 resonance | 0 linear to 1 linear | 0.2 linear |
| L2 tune | -24 semitones to 24 semitones | 0 semitones |
| L2 start | 0 ms to 500 ms | 0 ms |
| L2 pan | -1 linear to 1 linear | 0 linear |
| L2 sample filter | Off, On | Off |
| L2 bus | Master, Bus A, Bus B | Master |
| L2 table | 16 choices: Basic Shapes, Pulse Width, Harmonic Build, Odd Build, … | Basic Shapes |
| L2 table mix | 0 linear to 1 linear | 0 linear |
| L2 table position | 0 linear to 1 linear | 0 linear |
| L2 decay shape | 0 linear to 1 linear | 1 linear |
| L2 factory click | 11 choices: Its sample, Felt Beater, Plastic Beater, Wood Beater, … | Its sample |
| L2 H1 ratio | 0.5 to 16 | 2 |
| L2 H1 level | -60 dB to 0 dB | -60 dB |
| L2 H1 decay | 1 ms to 3000 ms | 150 ms |
| L2 H2 ratio | 0.5 to 16 | 3 |
| L2 H2 level | -60 dB to 0 dB | -60 dB |
| L2 H2 decay | 1 ms to 3000 ms | 150 ms |
| L2 H3 ratio | 0.5 to 16 | 4 |
| L2 H3 level | -60 dB to 0 dB | -60 dB |
| L2 H3 decay | 1 ms to 3000 ms | 150 ms |
| L2 H4 ratio | 0.5 to 16 | 5 |
| L2 H4 level | -60 dB to 0 dB | -60 dB |
| L2 H4 decay | 1 ms to 3000 ms | 150 ms |
| L2 H5 ratio | 0.5 to 16 | 6 |
| L2 H5 level | -60 dB to 0 dB | -60 dB |
| L2 H5 decay | 1 ms to 3000 ms | 150 ms |
| L2 H6 ratio | 0.5 to 16 | 7 |
| L2 H6 level | -60 dB to 0 dB | -60 dB |
| L2 H6 decay | 1 ms to 3000 ms | 150 ms |
| L2 H7 ratio | 0.5 to 16 | 8 |
| L2 H7 level | -60 dB to 0 dB | -60 dB |
| L2 H7 decay | 1 ms to 3000 ms | 150 ms |
| L2 H8 ratio | 0.5 to 16 | 9 |
| L2 H8 level | -60 dB to 0 dB | -60 dB |
| L2 H8 decay | 1 ms to 3000 ms | 150 ms |
| L2 H9 ratio | 0.5 to 16 | 10 |
| L2 H9 level | -60 dB to 0 dB | -60 dB |
| L2 H9 decay | 1 ms to 3000 ms | 150 ms |
| Layer 3 | Off, Body, Click, Noise, Sample | Off |
| L3 level | -60 dB to 12 dB | 0 dB |
| L3 mute | Off, On | Off |
| L3 solo | Off, On | Off |
| L3 invert | Off, On | Off |
| L3 phase | 0 degrees to 360 degrees | 0 degrees |
| L3 wave | Triangle, Saw, Square | Triangle |
| L3 wave mix | 0 linear to 1 linear | 0 linear |
| L3 click noise | 0 linear to 1 linear | 0.6 linear |
| L3 filter | Low, Band, High | Band |
| L3 cutoff | 20 Hz to 20000 Hz | 6000 Hz |
| L3 resonance | 0 linear to 1 linear | 0.2 linear |
| L3 tune | -24 semitones to 24 semitones | 0 semitones |
| L3 start | 0 ms to 500 ms | 0 ms |
| L3 pan | -1 linear to 1 linear | 0 linear |
| L3 sample filter | Off, On | Off |
| L3 bus | Master, Bus A, Bus B | Master |
| L3 table | 16 choices: Basic Shapes, Pulse Width, Harmonic Build, Odd Build, … | Basic Shapes |
| L3 table mix | 0 linear to 1 linear | 0 linear |
| L3 table position | 0 linear to 1 linear | 0 linear |
| L3 decay shape | 0 linear to 1 linear | 1 linear |
| L3 factory click | 11 choices: Its sample, Felt Beater, Plastic Beater, Wood Beater, … | Its sample |
| L3 H1 ratio | 0.5 to 16 | 2 |
| L3 H1 level | -60 dB to 0 dB | -60 dB |
| L3 H1 decay | 1 ms to 3000 ms | 150 ms |
| L3 H2 ratio | 0.5 to 16 | 3 |
| L3 H2 level | -60 dB to 0 dB | -60 dB |
| L3 H2 decay | 1 ms to 3000 ms | 150 ms |
| L3 H3 ratio | 0.5 to 16 | 4 |
| L3 H3 level | -60 dB to 0 dB | -60 dB |
| L3 H3 decay | 1 ms to 3000 ms | 150 ms |
| L3 H4 ratio | 0.5 to 16 | 5 |
| L3 H4 level | -60 dB to 0 dB | -60 dB |
| L3 H4 decay | 1 ms to 3000 ms | 150 ms |
| L3 H5 ratio | 0.5 to 16 | 6 |
| L3 H5 level | -60 dB to 0 dB | -60 dB |
| L3 H5 decay | 1 ms to 3000 ms | 150 ms |
| L3 H6 ratio | 0.5 to 16 | 7 |
| L3 H6 level | -60 dB to 0 dB | -60 dB |
| L3 H6 decay | 1 ms to 3000 ms | 150 ms |
| L3 H7 ratio | 0.5 to 16 | 8 |
| L3 H7 level | -60 dB to 0 dB | -60 dB |
| L3 H7 decay | 1 ms to 3000 ms | 150 ms |
| L3 H8 ratio | 0.5 to 16 | 9 |
| L3 H8 level | -60 dB to 0 dB | -60 dB |
| L3 H8 decay | 1 ms to 3000 ms | 150 ms |
| L3 H9 ratio | 0.5 to 16 | 10 |
| L3 H9 level | -60 dB to 0 dB | -60 dB |
| L3 H9 decay | 1 ms to 3000 ms | 150 ms |
| Layer 4 | Off, Body, Click, Noise, Sample | Off |
| L4 level | -60 dB to 12 dB | 0 dB |
| L4 mute | Off, On | Off |
| L4 solo | Off, On | Off |
| L4 invert | Off, On | Off |
| L4 phase | 0 degrees to 360 degrees | 0 degrees |
| L4 wave | Triangle, Saw, Square | Triangle |
| L4 wave mix | 0 linear to 1 linear | 0 linear |
| L4 click noise | 0 linear to 1 linear | 0.6 linear |
| L4 filter | Low, Band, High | Band |
| L4 cutoff | 20 Hz to 20000 Hz | 6000 Hz |
| L4 resonance | 0 linear to 1 linear | 0.2 linear |
| L4 tune | -24 semitones to 24 semitones | 0 semitones |
| L4 start | 0 ms to 500 ms | 0 ms |
| L4 pan | -1 linear to 1 linear | 0 linear |
| L4 sample filter | Off, On | Off |
| L4 bus | Master, Bus A, Bus B | Master |
| L4 table | 16 choices: Basic Shapes, Pulse Width, Harmonic Build, Odd Build, … | Basic Shapes |
| L4 table mix | 0 linear to 1 linear | 0 linear |
| L4 table position | 0 linear to 1 linear | 0 linear |
| L4 decay shape | 0 linear to 1 linear | 1 linear |
| L4 factory click | 11 choices: Its sample, Felt Beater, Plastic Beater, Wood Beater, … | Its sample |
| L4 H1 ratio | 0.5 to 16 | 2 |
| L4 H1 level | -60 dB to 0 dB | -60 dB |
| L4 H1 decay | 1 ms to 3000 ms | 150 ms |
| L4 H2 ratio | 0.5 to 16 | 3 |
| L4 H2 level | -60 dB to 0 dB | -60 dB |
| L4 H2 decay | 1 ms to 3000 ms | 150 ms |
| L4 H3 ratio | 0.5 to 16 | 4 |
| L4 H3 level | -60 dB to 0 dB | -60 dB |
| L4 H3 decay | 1 ms to 3000 ms | 150 ms |
| L4 H4 ratio | 0.5 to 16 | 5 |
| L4 H4 level | -60 dB to 0 dB | -60 dB |
| L4 H4 decay | 1 ms to 3000 ms | 150 ms |
| L4 H5 ratio | 0.5 to 16 | 6 |
| L4 H5 level | -60 dB to 0 dB | -60 dB |
| L4 H5 decay | 1 ms to 3000 ms | 150 ms |
| L4 H6 ratio | 0.5 to 16 | 7 |
| L4 H6 level | -60 dB to 0 dB | -60 dB |
| L4 H6 decay | 1 ms to 3000 ms | 150 ms |
| L4 H7 ratio | 0.5 to 16 | 8 |
| L4 H7 level | -60 dB to 0 dB | -60 dB |
| L4 H7 decay | 1 ms to 3000 ms | 150 ms |
| L4 H8 ratio | 0.5 to 16 | 9 |
| L4 H8 level | -60 dB to 0 dB | -60 dB |
| L4 H8 decay | 1 ms to 3000 ms | 150 ms |
| L4 H9 ratio | 0.5 to 16 | 10 |
| L4 H9 level | -60 dB to 0 dB | -60 dB |
| L4 H9 decay | 1 ms to 3000 ms | 150 ms |
| Layer 5 | Off, Body, Click, Noise, Sample | Off |
| L5 level | -60 dB to 12 dB | 0 dB |
| L5 mute | Off, On | Off |
| L5 solo | Off, On | Off |
| L5 invert | Off, On | Off |
| L5 phase | 0 degrees to 360 degrees | 0 degrees |
| L5 wave | Triangle, Saw, Square | Triangle |
| L5 wave mix | 0 linear to 1 linear | 0 linear |
| L5 click noise | 0 linear to 1 linear | 0.6 linear |
| L5 filter | Low, Band, High | Band |
| L5 cutoff | 20 Hz to 20000 Hz | 6000 Hz |
| L5 resonance | 0 linear to 1 linear | 0.2 linear |
| L5 tune | -24 semitones to 24 semitones | 0 semitones |
| L5 start | 0 ms to 500 ms | 0 ms |
| L5 pan | -1 linear to 1 linear | 0 linear |
| L5 sample filter | Off, On | Off |
| L5 bus | Master, Bus A, Bus B | Master |
| L5 table | 16 choices: Basic Shapes, Pulse Width, Harmonic Build, Odd Build, … | Basic Shapes |
| L5 table mix | 0 linear to 1 linear | 0 linear |
| L5 table position | 0 linear to 1 linear | 0 linear |
| L5 decay shape | 0 linear to 1 linear | 1 linear |
| L5 factory click | 11 choices: Its sample, Felt Beater, Plastic Beater, Wood Beater, … | Its sample |
| L5 H1 ratio | 0.5 to 16 | 2 |
| L5 H1 level | -60 dB to 0 dB | -60 dB |
| L5 H1 decay | 1 ms to 3000 ms | 150 ms |
| L5 H2 ratio | 0.5 to 16 | 3 |
| L5 H2 level | -60 dB to 0 dB | -60 dB |
| L5 H2 decay | 1 ms to 3000 ms | 150 ms |
| L5 H3 ratio | 0.5 to 16 | 4 |
| L5 H3 level | -60 dB to 0 dB | -60 dB |
| L5 H3 decay | 1 ms to 3000 ms | 150 ms |
| L5 H4 ratio | 0.5 to 16 | 5 |
| L5 H4 level | -60 dB to 0 dB | -60 dB |
| L5 H4 decay | 1 ms to 3000 ms | 150 ms |
| L5 H5 ratio | 0.5 to 16 | 6 |
| L5 H5 level | -60 dB to 0 dB | -60 dB |
| L5 H5 decay | 1 ms to 3000 ms | 150 ms |
| L5 H6 ratio | 0.5 to 16 | 7 |
| L5 H6 level | -60 dB to 0 dB | -60 dB |
| L5 H6 decay | 1 ms to 3000 ms | 150 ms |
| L5 H7 ratio | 0.5 to 16 | 8 |
| L5 H7 level | -60 dB to 0 dB | -60 dB |
| L5 H7 decay | 1 ms to 3000 ms | 150 ms |
| L5 H8 ratio | 0.5 to 16 | 9 |
| L5 H8 level | -60 dB to 0 dB | -60 dB |
| L5 H8 decay | 1 ms to 3000 ms | 150 ms |
| L5 H9 ratio | 0.5 to 16 | 10 |
| L5 H9 level | -60 dB to 0 dB | -60 dB |
| L5 H9 decay | 1 ms to 3000 ms | 150 ms |
