---
title: "Modules: Utilities"
description: "Voltages set and scaled, pitches quantized and moved, and the notes as signals."
sidebar:
  label: "Utilities"
  order: 9
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

Voltages set and scaled, pitches quantized and moved, and the notes as signals.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Attenuverter

A signal made larger, smaller or upside down, and moved up or down: for audio or modulation.

- **In:** Input (control)
- **Out:** Output (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Gain | -4 to 4 | 1 |
| Offset | -10 V to 10 V | 0 V |

## Constant Voltage

A steady voltage, set exactly: to tune, to bias, or to control.

- **In:** None
- **Out:** Output (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Voltage | -10 V to 10 V | 0 V |

## Slew Limiter

How fast a voltage may rise and fall, each set apart: for glide, and to smooth modulation.

- **In:** Input (control)
- **Out:** Output (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Rise | 0.01 ms to 20000 ms | 50 ms |
| Fall | 0.01 ms to 20000 ms | 50 ms |

## Pitch Quantizer

A pitch moved to the nearest note of a scale: one of fourteen, the song's, notes of your own, or the notes held, from a root, transposed; and a pulse each time the note changes.

- **In:** Pitch (pitch), Transpose (pitch)
- **Out:** Pitch (pitch), Changed (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Root | 0 semitones to 11 semitones | 0 semitones |
| Scale | Chromatic, Major, Minor, Major pentatonic, Minor pentatonic, Dorian, Phrygian, Lydian, Mixolydian, Locrian, Harmonic minor, Melodic minor, Blues, Whole tone, Song's scale, Custom, Notes held | Chromatic |
| Transpose | -48 semitones to 48 semitones | 0 semitones |
| Octave | -4 to 4 | 0 |
| C | Off, On | On |
| C# | Off, On | Off |
| D | Off, On | On |
| D# | Off, On | Off |
| E | Off, On | On |
| F | Off, On | On |
| F# | Off, On | Off |
| G | Off, On | On |
| G# | Off, On | Off |
| A | Off, On | On |
| A# | Off, On | Off |
| B | Off, On | On |

## Pitch Utility

A pitch moved by semitones, octaves, a ratio of whole numbers and cents.

- **In:** Pitch (pitch)
- **Out:** Pitch (pitch)

| Knob | Range | Starts at |
| --- | --- | --- |
| Transpose | -48 semitones to 48 semitones | 0 semitones |
| Octave | -4 to 4 | 0 |
| Ratio over | 1 to 16 | 1 |
| Ratio under | 1 to 16 | 1 |
| Fine | -100 cents to 100 cents | 0 cents |

## Note to CV

The rack's notes as signals for each voice: pitch at 1 V an octave, gate, velocity, pressure, bend and slide.

- **In:** None
- **Out:** Pitch (pitch), Gate (gate), Velocity (control), Pressure (control), Bend (control), Slide (control)

## Voice Info

Each voice's number and its place across the voices (to spread a unison's tuning or pan), the keys held, the lowest and highest of them, and a gate while any is.

- **In:** None
- **Out:** Voice (control), Spread (control), Keys held (control), Lowest key (pitch), Highest key (pitch), Any key (gate)
