---
title: "Desk Glue Bus Compressor"
description: "VCA bus compressor in the style of the 1980s British large-format consoles: glue for the mix and drum buses."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A modelled bus compressor built on a voltage-controlled amplifier, for gluing a mix bus or a drum bus: a threshold, ratios of 2, 4, and 10 to 1, an attack of 0.1 to 30 ms and a release of 0.1 to 1.2 s on switches, with an automatic release that lets a short peak go quickly and a long passage slowly, and a make-up gain. One peak detector serves both channels, so the stereo image holds still. Its timing is the circuit's network of a diode, resistances, and capacitors, solved exactly. With a high-pass in the sidechain, a mix of the compressed with what went in, a switch for where the detector listens, ahead of the gain element or behind it, and a sidechain from another track. Modelled on the stereo compressor in the centre section of a large British mixing console of the 1980s.

[Desk Glue Bus Compressor on the website](/solmara/effects/#desk-glue-bus-compressor)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Threshold | -50 dB to 0 dB | -20 dB |
| Ratio | 2:1, 4:1, 10:1 | 4:1 |
| Attack | 0.1 ms, 0.3 ms, 1 ms, 3 ms, 10 ms, 30 ms | 10 ms |
| Release | 0.1 s, 0.3 s, 0.6 s, 1.2 s, Auto | Auto |
| Make-up | 0 dB to 20 dB | 0 dB |
| Mix | 0 linear to 1 linear | 1 linear |
| SC low cut | 0 Hz to 500 Hz | 0 Hz |
| Detector | Forward, Back | Forward |
