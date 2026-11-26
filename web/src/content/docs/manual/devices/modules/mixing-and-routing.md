---
title: "Modules: Mixing and routing"
description: "Signals mixed, panned, faded, switched, split and sent."
sidebar:
  label: "Mixing and routing"
  order: 8
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

Signals mixed, panned, faded, switched, split and sent.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Modular Mixer

Four inputs, audio or control, each with its own level, which can turn it upside down, mixed for each voice.

- **In:** A (audio), B (audio), C (audio), D (audio)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| A | -2   to 2   | 1   |
| B | -2   to 2   | 1   |
| C | -2   to 2   | 1   |
| D | -2   to 2   | 1   |
| Level | 0 to 2 | 1 |

## Sequential Switch

One of four signals let through, chosen by a knob or the next at each clock.

- **In:** A (control), B (control), C (control), D (control), Clock (clock), Reset (gate)
- **Out:** Output (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Position | A, B, C, D | A |

## Router

One input sent to one of four outputs, chosen by a knob or stepped by a clock, faded across in 5 ms.

- **In:** Input (audio), Clock (clock), Reset (gate)
- **Out:** A (audio), B (audio), C (audio), D (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Position | A, B, C, D | A |

## Mid/Side

Left and right as mid and side and back: the side's width, the mid's level, and mid and side to mix in.

- **In:** Left (audio), Right (audio), Mid in (audio), Side in (audio)
- **Out:** Left (audio), Right (audio), Mid (audio), Side (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Width | 0 to 2 | 1 |
| Mid level | 0 to 2 | 1 |

## Crossover

Three bands, low, mid and high, at two splits (Linkwitz-Riley, 24 dB an octave), adding up to what came in.

- **In:** Input (audio)
- **Out:** Low (audio), Mid (audio), High (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Low split | 20 Hz to 2000 Hz | 200 Hz |
| High split | 200 Hz to 18000 Hz | 2500 Hz |

## Stereo Mixer

Eight inputs, each with a level and a pan, to a stereo pair and a mono sum.

- **In:** In 1 (audio), In 2 (audio), In 3 (audio), In 4 (audio), In 5 (audio), In 6 (audio), In 7 (audio), In 8 (audio)
- **Out:** Left (audio), Right (audio), Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Level 1–8 | 0 to 2 | 1 |
| Pan 1–8 | -1 to 1 | 0 |
| Master | 0 to 2 | 1 |

## Voltage Crossfader

Two signals faded into each other for each voice, in a straight line or at equal power.

- **In:** A (audio), B (audio), CV (control)
- **Out:** Output (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Position | 0 to 1 | 0.5 |
| Law | Linear, Equal power | Linear |

## Voltage Panner

A signal, or each voice, panned into stereo, as loud wherever it is.

- **In:** Input (audio), CV (control)
- **Out:** Left (audio), Right (audio)

| Knob | Range | Starts at |
| --- | --- | --- |
| Pan | -1 to 1 | 0 |

## Buffered Multiple

One signal at four outputs, unchanged, its voices kept.

- **In:** Input (control)
- **Out:** A (control), B (control), C (control), D (control)
