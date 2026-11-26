---
title: "Modules: Displays"
description: "What a signal is doing, shown as it plays, and notes on the patch."
sidebar:
  label: "Displays"
  order: 10
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

What a signal is doing, shown as it plays, and notes on the patch.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Value Readout

Four signals' values as numbers, a pitch as its note and frequency, passed through unchanged.

- **In:** A (control), B (control), C (control), D (control)
- **Out:** A (control), B (control), C (control), D (control)

## XY Scope

Two signals drawn against each other: a Lissajous figure of two oscillators, a stereo pair's width.

- **In:** X (audio), Y (audio)
- **Out:** None

## Spectrum

The frequencies in a signal as it plays, passed through unchanged.

- **In:** Input (audio)
- **Out:** Output (audio)

## Label

A note on the patch, as large as you write it: no jacks, no sound.

No jacks.

## Signal Monitor

A signal passed through unchanged, its value on the meters and there for agents to read.

- **In:** Input (audio)
- **Out:** Output (audio)
