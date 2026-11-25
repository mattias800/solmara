---
title: "Mid-Century Vari-Mu"
description: "Variable-mu valve compressor in the style of the late-1950s American broadcast limiters: slow, gentle glue for masters and buses."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A modelled variable-mu valve compressor, for masters and drum buses: a push-pull pair of remote-cutoff valves between an input and an output transformer, whose gain falls smoothly as the sidechain takes their grids further under their cathodes. The ratio is no switch's: it grows with the reduction, from a gentle slope at the knee to a limiter's well over it. An input knob in dB that drives the valves and sets the threshold with the threshold knob, a time constant switch of six places, four fixed and two automatic that let a short peak go quickly and a long passage slowly, the sidechain's bias trimmer, an output knob, a mix, a balance trimmer for the pair, a high-pass in the sidechain, a link between the two channels, a matrix that compresses their middle and side, and a sidechain from another track. The gain cell is a circuit solved part by part; the timing network is the circuit's, solved exactly. Modelled on the large American valve limiter of the late 1950s, two channels of it in one unit.

[Mid-Century Vari-Mu on the website](/solmara/effects/#mid-century-vari-mu)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Input | -20 dB to 0 dB | -10 dB |
| Threshold | 0 to 10 | 5 |
| Time Constant | 1, 2, 3, 4, 5, 6 | 2 |
| DC Threshold | 0 to 10 | 8.6 |
| Output | -20 dB to 20 dB | 0 dB |
| Mix | 0 linear to 1 linear | 1 linear |
| Balance | -10 to 10 | 0 |
| SC Filter | Off, On | Off |
| Link | Off, On | On |
| Matrix | Left-Right, Mid-Side | Left-Right |
