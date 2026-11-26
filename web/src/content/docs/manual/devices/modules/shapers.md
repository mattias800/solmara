---
title: "Modules: Shapers"
description: "What bends a wave into another: folding, saturation, multiplying and rectifying."
sidebar:
  label: "Shapers"
  order: 3
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

What bends a wave into another: folding, saturation, multiplying and rectifying.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Wavefolder

A wave folded back on itself again and again, for bright overtones, off centre by its symmetry, the fold moved as fast as audio.

- **In:** Input (audio), Fold (control)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Fold | 1 to 16 | 2 |
| Symmetry | -5 V to 5 V | 0 V |
| Mix | 0 to 1 | 1 |

## Ring Modulator

Two signals multiplied: a ring modulator's sound, and amplitude modulation.

- **In:** A (audio), B (audio)
- **Out:** Ring (audio), AM (audio), Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Level | 0 to 2 | 1 |

## Voltage Saturator

Smooth saturation, driven harder or softer, lopsided by its bias, mixed with what came in.

- **In:** Input (audio), Drive (control)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Drive | 1 to 32 | 2 |
| Bias | -5 V to 5 V | 0 V |
| Mix | 0 to 1 | 1 |

## Shaper

Chebyshev harmonics of an order, a diode's lopsided curve, a hard clip, fewer bits, or steps of a voltage.

- **In:** Input (audio), Drive (control), Amount (control)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Type | Chebyshev, Diode, Hard clip, Bit crush, Level steps | Chebyshev |
| Drive | 0 dB to 36 dB | 0 dB |
| Amount | 0 to 1 | 0.5 |
| Mix | 0 to 1 | 1 |
| Level | 0 to 2 | 1 |

## Voltage Rectifier

A signal's negative half turned up or cut off, the signal upside down, and the lower and the higher of it and a second.

- **In:** A (control), B (control)
- **Out:** Full (control), Half (control), Inverted (control), Minimum (control), Maximum (control)
