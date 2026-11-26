---
title: "Modules: Sequencing"
description: "What keeps time and plays in it: clocks, dividers, sequencers and the song's place."
sidebar:
  label: "Sequencing"
  order: 5
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

What keeps time and plays in it: clocks, dividers, sequencers and the song's place.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Modular Clock

A clock with swing, at its own tempo or the song's, with its place in each pulse and a gate while it runs.

- **In:** Reset (gate), Rate (control)
- **Out:** Clock (clock), Phase (control), Run (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Tempo | 1 BPM to 999 BPM | 120 BPM |
| Pulses per beat | 0.125 to 32 | 4 |
| Sync | Free, Transport | Transport |
| Swing | 0 to 0.75 | 0 |

## Clock Divider

A clock divided by two, three, four and eight at once, and by any number up to 64 at its main output.

- **In:** Clock (clock), Reset (gate)
- **Out:** Div 2 (clock), Div 3 (clock), Div 4 (clock), Div 8 (clock), Output (clock)

| Knob | Range | Starts at |
| --- | --- | --- |
| Division | 1 to 64 | 2 |

## Voltage Sequencer

Eight steps of pitch, a clock stepping them and a gate at each, played to a length of steps you set.

- **In:** Clock (clock), Reset (gate), Transpose (pitch)
- **Out:** Pitch (pitch), Gate (gate), Step (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Steps | 1 to 8 | 8 |
| Gate length | 0.01 to 1 | 0.5 |
| Step 1–8 | -24 semitones to 24 semitones | 0 semitones, 3 semitones, 7 semitones, 10 semitones, 12 semitones, 10 semitones, 7 semitones, 3 semitones |

## Euclidean Gates

A number of hits spread as evenly as they go over a number of steps, turned round to start elsewhere, and an accent on the hits that fall every so many steps.

- **In:** Clock (clock), Reset (gate)
- **Out:** Gate (gate), Accent (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Steps | 1 to 32 | 16 |
| Hits | 0 to 32 | 5 |
| Rotate | 0 to 31 | 0 |
| Accent every | 1 to 16 | 4 |

## Trigger Delay

A trigger, a while later, as a pulse as long as you set.

- **In:** Trigger (gate), Time (control)
- **Out:** Output (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Delay | 0 ms to 10000 ms | 100 ms |
| Width | 0.02 ms to 10000 ms | 10 ms |

## Transport

The song's place as signals: running, ramps over each beat, each bar and a length of bars, a pulse at each beat and bar, and the tempo.

- **In:** None
- **Out:** Running (gate), Beat phase (control), Bar phase (control), Ramp (control), Beat (clock), Bar (clock), Tempo (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Beats a bar | 1 to 16 | 4 |
| Ramp length | 1 bar to 64 bars | 4 bars |

## Step Sequencer

Sixteen steps of pitch, each resting, playing or tied on, with accent and chance; forward, backward, ping-pong or random, clocked or read along a Phase input.

- **In:** Clock (clock), Reset (gate), Transpose (pitch), Phase (control)
- **Out:** Pitch (pitch), Gate (gate), Accent (gate), Velocity (control), Step (control), End (clock)

| Knob | Range | Starts at |
| --- | --- | --- |
| Steps | 1 to 16 | 16 |
| Direction | Forward, Backward, Ping-pong, Random | Forward |
| Gate length | 0.01 to 1 | 0.5 |
| Step 1–16 pitch | -24 semitones to 24 semitones | 0 semitones |
| Step 1–16 gate | Rest, Play, Tie | Play |
| Step 1–16 accent | Off, On | Off |
| Step 1–16 chance | 0 to 1 | 1 |

## Trigger Sequencer

Four tracks of sixteen steps, each off, on or accented, with a chance for each track.

- **In:** Clock (clock), Reset (gate)
- **Out:** Gate A (gate), Gate B (gate), Gate C (gate), Gate D (gate), Accent A (gate), Accent B (gate), Accent C (gate), Accent D (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Steps | 1 to 16 | 16 |
| Gate length | 0.01 to 1 | 0.25 |
| Track A chance | 0 to 1 | 1 |
| Track B chance | 0 to 1 | 1 |
| Track C chance | 0 to 1 | 1 |
| Track D chance | 0 to 1 | 1 |
| Track A step 1–16 | Off, On, Accent | Off |
| Track B step 1–16 | Off, On, Accent | Off |
| Track C step 1–16 | Off, On, Accent | Off |
| Track D step 1–16 | Off, On, Accent | Off |

## Clock Ratio

An incoming clock multiplied and divided by whole numbers, its pulses spread evenly.

- **In:** Clock (clock), Reset (gate)
- **Out:** Output (clock)

| Knob | Range | Starts at |
| --- | --- | --- |
| Multiply | 1 to 16 | 2 |
| Divide | 1 to 16 | 1 |
| Pulse width | 0.05 to 0.95 | 0.5 |

## Clock Quantizer

Holds each gate until the next clock, then lets it through: as a pulse, or for as long as it is held.

- **In:** Gate (gate), Clock (clock)
- **Out:** Output (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Gate | Pulse, Follow | Follow |

## Ratchet

Repeats a gate: a number of pulses at an interval, or for as long as it is held.

- **In:** Gate (gate)
- **Out:** Output (gate)

| Knob | Range | Starts at |
| --- | --- | --- |
| Repeats | 1 to 16 | 4 |
| Interval | 5 ms to 2000 ms | 100 ms |
| Pulse width | 0.05 to 0.95 | 0.5 |
| Mode | Count, While held | Count |

## Shift Register

Eight stages a clock moves a value along: its data input's, or its own last stage, changed by chance (a looping random sequence), with a weighted sum.

- **In:** Clock (clock), Data (control)
- **Out:** Out 1 (control), Out 2 (control), Out 3 (control), Out 4 (control), Out 5 (control), Out 6 (control), Out 7 (control), Out 8 (control), Sum (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Change | 0 to 1 | 0.5 |
| Loop length | 1 to 8 | 8 |
