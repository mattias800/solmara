---
title: "Modules: Logic and math"
description: "Gates combined and compared, signals added and multiplied, counted and latched."
sidebar:
  label: "Logic and math"
  order: 7
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

Gates combined and compared, signals added and multiplied, counted and latched.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Gate Logic

Two gates or clocks compared: AND, OR, XOR, NOT, NAND, NOR and XNOR at once.

- **In:** A (gate), B (gate)
- **Out:** And (gate), Or (gate), Xor (gate), Not (gate), Nand (gate), Nor (gate), Xnor (gate)

## Voltage Comparator

A gate while a voltage is above a threshold, a margin keeping it from chattering, and a pulse as it rises past and as it falls.

- **In:** Input (control), Threshold (control)
- **Out:** Gate (gate), Rise (gate), Fall (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Threshold | -10 V to 10 V | 0 V |
| Hysteresis | 0 V to 5 V | 0.1 V |

## Math

Two signals added, subtracted, multiplied, divided, compared, clipped or averaged, and gates for which is above.

- **In:** A (control), B (control)
- **Out:** Output (control), A above B (gate), A below B (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Operation | A + B, A - B, A x B, A / B, Minimum, Maximum, Difference, Clip A to B, Average | A + B |
| B | -10 V to 10 V | 0 V |
| Gain | -2 to 2 | 1 |

## Latch

A flip-flop: set, reset or toggled by gates, or taking its data input at each clock.

- **In:** Set (gate), Reset (gate), Toggle (gate), Data (gate), Clock (clock)
- **Out:** Output (gate), Inverted (gate)

## Counter

Counts clocks up and down to a length, as a voltage and a pitch, with a carry pulse each time it wraps.

- **In:** Up (clock), Down (clock), Reset (gate)
- **Out:** Value (control), Pitch (pitch), Carry (clock)

| Knob | Range | Starts at |
| --- | --- | --- |
| Length | 1 to 64 | 8 |
