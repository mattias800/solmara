---
title: "Modules: Sources"
description: "What makes a sound: oscillators, samples, grains and noise."
sidebar:
  label: "Sources"
  order: 1
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

What makes a sound: oscillators, samples, grains and noise.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Modular Oscillator

Sine, triangle, saw and pulse at once, free of aliasing, with the pulse's width, exponential and linear FM, and hard sync.

- **In:** Pitch (pitch), FM (control), Sync (gate)
- **Out:** Sine (audio), Triangle (audio), Saw (audio), Pulse (audio), Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Frequency | 0.01 Hz to 20000 Hz | 261.626 Hz |
| Wave | Sine, Triangle, Saw, Pulse | Saw |
| Pulse width | 0.02 to 0.98 | 0.5 |
| FM depth | -10 to 10 | 0 |
| Linear FM | -2000 Hz/V to 2000 Hz/V | 0 Hz/V |
| Level | 0 to 2 | 1 |

## Complex Oscillator

Two oscillators, one modulating the other's frequency through zero and its phase, then folded; the modulator has an output of its own.

- **In:** Pitch (pitch), FM (control), Timbre (control), Sync (gate)
- **Out:** Output (audio), Modulator (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Frequency | 0.01 Hz to 20000 Hz | 261.626 Hz |
| Ratio | 0.125 to 16 | 2 |
| FM index | 0 to 20 | 0 |
| Fold | 1 to 8 | 1 |
| Phase index | 0 to 8 | 0 |
| Level | 0 to 2 | 1 |

## Morph Oscillator

One wave that morphs smoothly from sine to triangle to saw to square, the morph moved as fast as audio.

- **In:** Pitch (pitch), Morph (control), FM (control)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Frequency | 0.01 Hz to 20000 Hz | 261.626 Hz |
| Morph | 0 to 3 | 0 |
| FM depth | -10 to 10 | 0 |
| Level | 0 to 2 | 1 |

## Noise and Random

White and pink noise, and a random voltage that wanders smoothly, the same each time from its seed.

- **In:** Reset (gate)
- **Out:** White (audio), Pink (audio), Random (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Random rate | 0.01 Hz to 100 Hz | 1 Hz |
| Seed | 1 to 1000000 | 1 |
| Level | 0 to 2 | 1 |

## Grain Texture

What comes in, cut into grains, four overlapping for each voice, with their size, density, position and pitch, and a freeze.

- **In:** Input (audio), Pitch (pitch), Position (control), Freeze (gate)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Grain size | 5 ms to 500 ms | 100 ms |
| Density | 0.1 Hz to 100 Hz | 20 Hz |
| Position | 0 to 1 | 0.4 |
| Pitch | -24 semitones to 24 semitones | 0 semitones |
| Texture | 0 to 1 | 0.3 |
| Freeze | Off, On | Off |
| Mix | 0 to 1 | 1 |

## Character Oscillator

Every analog oscillator the app has, as Vintergatan plays them: the pure one, and Titan 303's, Shy One's, June Bloom's, Promise Bloom's, Mini Moonbeam's and the Two-Filter Mono's own cores.

- **In:** Pitch (pitch), FM (control), Sync (gate)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Character | Pure, Scream, Shy, June, Promise, Moonbeam, Two-Filter | Pure |
| Wave | Saw, Pulse, Triangle, Sine | Saw |
| Frequency | 0.01 Hz to 20000 Hz | 261.626 Hz |
| Pulse width | 0.05 to 0.95 | 0.5 |
| FM depth | -10 to 10 | 0 |
| Level | 0 to 2 | 1 |

## Wavetable Oscillator

Vintergatan's wavetable oscillator: the factory tables, or one made of the audio in its slot, read by position, band-limited, through its twenty warps, a second warp and a spectral morph; the FM, AM and ring warps take the Other input.

- **In:** Pitch (pitch), FM (control), Position (control), Other (audio)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Table | Basic Shapes, Pulse Width, Harmonic Build, Odd Build, Harmonic Sweep, Drawbars, Sync Saw, Sync Sine, FM Index, FM Unison, Wavefold, Phase Resonance, Vowels, Noise Spectra, Bit Steps, From audio | Basic Shapes |
| Position | 0 to 1 | 0 |
| Warp | None, FM, Classic, Modern, Sync, Bend +, Bend -, Bend +/-, Pulse width, Mirror, Quantize, Remap, FM from another, AM from another, Ring from another, Squeeze, Formant, Low pass, High pass, Saturate | None |
| Warp amount | 0 to 1 | 0 |
| Warp second | 0 to 1 | 0 |
| Second warp | None, Sync, Bend +, Bend -, Bend +/-, Pulse width, Mirror, Quantize, Remap, FM from another, AM from another, Ring from another, Squeeze, Formant, Low pass, High pass, Saturate | None |
| Second amount | 0 to 1 | 0 |
| Frequency | 0.01 Hz to 20000 Hz | 261.626 Hz |
| FM depth | -10 to 10 | 0 |
| Level | 0 to 2 | 1 |
| Table from audio | Cycles, Pitch splice, Vocode | Cycles |
| Spectral morph | None, Vocode, Formant scale, Harmonic stretch, Inharmonic scale, Smear, Random amplitudes, Low pass, High pass, Phase disperse, Shepard tone, Time skew, Even/odd, Comb, Gate | None |
| Morph amount | 0 to 1 | 0 |

## Sample Oscillator

Vintergatan's sample, granular and spectral oscillators on the audio in its slot: played from its start at each gate, once, looped, back and forth, reversed or held; as grains scattered about a position; or taken apart into its partials and put together again, its speed apart from its pitch, through a spectral morph.

- **In:** Pitch (pitch), Gate (gate), Position (control)
- **Out:** Left (audio), Right (audio), Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Mode | Sample, Granular, Spectral | Sample |
| Play | Once, Loop, Back and forth, Reverse, Hold | Once |
| Start | 0 to 1 | 0 |
| End | 0 to 1 | 1 |
| Loop start | 0 to 1 | 0 |
| Loop end | 0 to 1 | 1 |
| Loop fade | 0 to 0.5 | 0 |
| Position | 0 to 1 | 0.5 |
| Scan | 0 to 4 | 0 |
| Grain size | 5 ms to 500 ms | 80 ms |
| Density | 1 per second to 200 per second | 20 per second |
| Spray | 0 to 1 | 0.05 |
| Pitch spray | 0 semitones to 12 semitones | 0 semitones |
| Window | Smooth, Triangle, Sharp | Smooth |
| Window amount | 0 to 1 | 1 |
| Level | 0 to 2 | 1 |
| Speed | 0 to 4 | 1 |
| Timbre | -24 semitones to 24 semitones | 0 semitones |
| Lowest frequency | 20 Hz to 20000 Hz | 20 Hz |
| Highest frequency | 20 Hz to 20000 Hz | 20000 Hz |
| Spectral morph | None, Vocode, Formant scale, Harmonic stretch, Inharmonic scale, Smear, Random amplitudes, Low pass, High pass, Phase disperse, Shepard tone, Time skew, Even/odd, Comb, Gate | None |
| Morph amount | 0 to 1 | 0 |
| Root key | 0 to 127 | 60 |

## Multisample Oscillator

Vintergatan's multisample oscillator: a sample library (SFZ, DecentSampler, SoundFont or Sampler instrument) across the keys, each gate playing the zone its pitch and velocity fall in from that zone's own root.

- **In:** Pitch (pitch), Gate (gate), Velocity (control)
- **Out:** Left (audio), Right (audio), Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Transpose | -48 semitones to 48 semitones | 0 semitones |
| Level | 0 to 2 | 1 |
