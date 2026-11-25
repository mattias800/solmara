---
title: "Solvind EQ"
description: "Listening EQ: what hides is tamed, what is hidden brought up."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

**A design of Solmara's own.**

An equaliser that listens, the mastering family's: many times a second it works out which bands of what passes hide the bands about them, on a model of hearing, and turns those down and the hidden ones up, so a master or a bus is clearer and more even without a fixed curve. Recover and Tame set how far each way, Bias how the spectrum is split between them, Brighten whether the unmasking leans to the highs or the lows, Boost the balance of a louder or quieter playback, and two limits where it acts; the loudness is held, so it is not heard louder. 21 ms late, which the renderer takes out.

[Solvind EQ on the website](/solmara/effects/#solvind-eq)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Recover | 0% to 200% | 50% |
| Tame | 0% to 200% | 50% |
| Bias | -100% to 100% | 0% |
| Brighten | -100% to 100% | 0% |
| Hold loudness | Off, On | On |
| Output | -12 dB to 12 dB | 0 dB |
| Boost | -50 dB to 50 dB | 0 dB |
| Low limit | 20 Hz to 20000 Hz | 20 Hz |
| High limit | 20 Hz to 20000 Hz | 20000 Hz |
