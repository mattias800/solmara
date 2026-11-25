---
title: "Poly Sequencer"
description: "Poly Sequencer"
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

A MIDI device: a polyphonic step sequencer in a scale, whose notes can be boxes that play chords, repeats, arpeggios or strums, with eight patterns of four variations each that switch by themselves, a velocity lane, and transposition from the keys.

[Poly Sequencer on the website](/solmara/write/#poly-sequencer)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Play mode | Seq, Key | Seq |
| MIDI transpose | Off, On, On latch | Off |
| Pattern | 1 count to 8 count | 1 count |
| Variation | I, II, III, IV | I |
| Auto switch | Off, Next, Random, I-II, III-IV, I-I-I-II | Off |
| Shuffle | 50% to 75% | 66% |
| Shuffle source | Local, Global | Local |
