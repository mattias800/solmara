---
title: "Guitar Auto-EQ"
description: "Guitar auto-EQ: learns your guitar and turns it toward a pickup's DI or a saved tone profile."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

An equaliser that turns the guitar it is given toward a target guitar. Listen learns the guitar's tone from five seconds of playing; the equaliser is the difference between that and the target, a passive pickup's DI of our own or a tone profile, a guitar learned and saved. Amount sets how far it goes (100 % an even match), smooth how smooth the equaliser is, from a twelfth of an octave to more than half of one, and an output. It does nothing until it has learned a guitar, and holds nothing back.

[Guitar Auto-EQ on the website](/solmara/effects/#guitar-auto-eq)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Amount | 0% to 100% | 50% |
| Smooth | 0% to 100% | 50% |
| Output | -24 dB to 24 dB | 0 dB |
