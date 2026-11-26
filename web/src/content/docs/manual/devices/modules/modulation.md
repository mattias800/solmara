---
title: "Modules: Modulation"
description: "What moves things: envelopes, LFOs, random voltages and followers."
sidebar:
  label: "Modulation"
  order: 4
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

What moves things: envelopes, LFOs, random voltages and followers.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Modular LFO

A slow wave for modulation: sine, triangle, ramp and pulse at once, around zero or above it, free or locked to the tempo (eight bars to a thirty-second, triplets and dotted), restarted by a gate or read along a Phase input.

- **In:** Rate (control), Reset (gate), Phase (control)
- **Out:** Sine (control), Triangle (control), Saw (control), Pulse (control), Output (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Rate | 0.001 Hz to 100 Hz | 1 Hz |
| Wave | Sine, Triangle, Saw, Pulse | Saw |
| Unipolar | Bipolar, Unipolar | Bipolar |
| Level | 0 to 2 | 1 |
| Sync | Free, Tempo | Free |
| Division | 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/2T, 1/2., 1/4, 1/4T, 1/4., 1/8, 1/8T, 1/8., 1/16, 1/16T, 1/16., 1/32, 1/32T | 1/4 |
| Phase | 0 to 1 | 0 |

## Modular ADSR

Attack, decay, sustain and release for each voice while its gate is held, started again by a trigger, the same upside down, and a pulse at its end.

- **In:** Gate (gate), Trigger (gate)
- **Out:** Output (control), Inverted (control), End (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Attack | 0.05 ms to 10000 ms | 10 ms |
| Decay | 0.05 ms to 10000 ms | 150 ms |
| Sustain | 0 to 1 | 0.65 |
| Release | 0.05 ms to 20000 ms | 250 ms |
| Curve | -4 to 4 | 0 |

## Slope Function

A rise and a fall at each trigger, or round and round as an LFO, with a curve, and pulses at the end of the rise and of the fall.

- **In:** Trigger (gate), Cycle (gate), Rate (control)
- **Out:** Output (control), Rise End (gate), End (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Rise | 0.05 ms to 20000 ms | 100 ms |
| Fall | 0.05 ms to 20000 ms | 250 ms |
| Cycle | Off, On | Off |
| Curve | -4 to 4 | 0 |

## Stepped Random

A new random voltage at each clock or at its own rate, by a chance, the same each time from its seed, gliding to it or jumping.

- **In:** Clock (clock), Reset (gate)
- **Out:** Output (control), Gate (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Rate | 0.01 Hz to 100 Hz | 2 Hz |
| Probability | 0 to 1 | 0.5 |
| Slew | 0 ms to 5000 ms | 0 ms |
| Seed | 1 to 1000000 | 1 |
| Range | Unipolar, Bipolar | Unipolar |

## Sample and Hold

A voltage taken at each clock and held, or followed while the clock is high and held when it falls.

- **In:** Input (control), Clock (clock)
- **Out:** Output (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Mode | Sample, Track | Sample |

## Envelope Follower

How loud a signal is, as a voltage that follows it with its own attack and release, and a gate while it is above a threshold.

- **In:** Input (audio)
- **Out:** Envelope (control), Gate (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Attack | 0.05 ms to 1000 ms | 5 ms |
| Release | 0.05 ms to 5000 ms | 100 ms |
| Gain | 0 to 8 | 1 |
| Gate threshold | 0 V to 10 V | 1 V |

## Probability Gates

Each trigger sent to one output or the other by a chance, the same each time from its seed.

- **In:** Clock (clock), Probability (control)
- **Out:** A (gate), B (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Probability | 0 to 1 | 0.5 |
| Seed | 1 to 1000000 | 1 |

## Phasor

A ramp from 0 to 10 V, free or locked to the tempo, to drive oscillators, LFOs and sequencers in step.

- **In:** Rate (control), Reset (gate)
- **Out:** Phase (control), Wrap (clock)

| Knob | Range | Starts at |
| --- | --- | --- |
| Rate | 0.001 Hz to 1000 Hz | 1 Hz |
| Sync | Free, Tempo | Tempo |
| Division | 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/2T, 1/2., 1/4, 1/4T, 1/4., 1/8, 1/8T, 1/8., 1/16, 1/16T, 1/16., 1/32, 1/32T | 1 bar |
| Phase | 0 to 1 | 0 |
