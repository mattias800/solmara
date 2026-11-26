---
title: "Modules: Filters and amps"
description: "What shapes a sound's colour and loudness: filters, resonators and amplifiers."
sidebar:
  label: "Filters and amps"
  order: 2
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

What shapes a sound's colour and loudness: filters, resonators and amplifiers.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Modular VCA

How loud each voice is, set by a control voltage, on a straight or an exponential curve.

- **In:** Input (audio), CV (control)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Gain | 0 to 2 | 1 |
| Bias | 0 to 1 | 0 |
| Response | Linear, Exponential | Linear |

## Modular Multimode Filter

A state-variable filter that stays stable at any setting, its low-pass, band-pass, high-pass and notch at once, with drive.

- **In:** Input (audio), Cutoff (control), Resonance (control)
- **Out:** Low (audio), Band (audio), High (audio), Notch (audio), Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Cutoff | 10 Hz to 20000 Hz | 1000 Hz |
| Resonance | 0 to 0.999 | 0.1 |
| Mode | Low-pass, Band-pass, High-pass, Notch | Low-pass |
| Drive | 1 to 8 | 1 |

## Dual Multimode Filter

Two state-variable filters, the second tuned apart from the first, one after the other or side by side.

- **In:** Input (audio), Cutoff (control), Cutoff B (control)
- **Out:** A (audio), B (audio), Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Cutoff | 10 Hz to 20000 Hz | 1000 Hz |
| Resonance | 0 to 0.999 | 0.1 |
| Mode | Low-pass, Band-pass, High-pass, Notch | Low-pass |
| Drive | 1 to 8 | 1 |
| B tuning | -4 octaves to 4 octaves | 1 octave |
| Routing | Serial, Parallel | Serial |

## Modal Resonator

Four ringing modes at a pitch, struck by a gate or set ringing by audio, with structure, decay and brightness.

- **In:** Input (audio), Pitch (pitch), Strike (gate)
- **Out:** Output (audio), Odd (audio), Even (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Frequency | 0.01 Hz to 20000 Hz | 261.626 Hz |
| Decay | 0.01 s to 20 s | 1.5 s |
| Structure | 0 to 1 | 0.2 |
| Brightness | 0 to 1 | 0.5 |
| Mix | 0 to 1 | 1 |

## Spectral Bank

Eight resonant bands side by side, each with its own level, all moved together in frequency.

- **In:** Input (audio), Shift (control)
- **Out:** Output (audio), Odd (audio), Even (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Shift | -4 octaves to 4 octaves | 0 octaves |
| Resonance | 0.01 to 0.99 | 0.6 |
| Band 1–8 | 0 to 2 | 1 |

## Coupled Low-pass Gate

Loudness and a low-pass filter opened and closed together, with an attack and a decay of their own, struck by a gate or played by a control; or the amplifier alone, or the filter alone.

- **In:** Audio (audio), Control (control), Strike (gate)
- **Out:** Audio (audio), Response (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Response attack | 0.05 ms to 100 ms | 1 ms |
| Response decay | 1 ms to 4000 ms | 100 ms |
| Open cutoff | 20 Hz to 20000 Hz | 12000 Hz |
| Mode | Coupled, VCA, Low-pass | Coupled |
| Bias | 0 to 1 | 0 |

## Character Filter

Every filter the app has, as Vintergatan plays them: the transistor and diode ladders, Sallen-Key, OTA, state variable, the pure filter, the hardware models' own filters, and comb, phaser, formant, ring and reverb.

- **In:** Input (audio), Cutoff (control), Resonance (control)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Circuit | Transistor ladder, Diode ladder, Sallen-Key, OTA cascade, State variable, Pure, Scream ladder, June OTA, Promise OTA, Shy OTA, Two-Filter pair, Comb, Phaser, Formant, Ring, Reverb | Transistor ladder |
| Type | Low 24, Low 12, Band 24, Band 12, High 24, High 12, Notch 24, Notch 12, Peak 24, Peak 12, All-pass 24, All-pass 12, Morph 24, Morph 12 | Low 24 |
| Cutoff | 20 Hz to 20000 Hz | 1000 Hz |
| Resonance | 0 to 1 | 0.2 |
| Drive | 0 dB to 36 dB | 0 dB |
| Morph | 0 to 2 | 0 |
| Mix | 0 to 1 | 1 |
