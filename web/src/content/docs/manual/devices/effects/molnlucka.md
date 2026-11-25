---
title: "Molnlucka"
description: "Room maker: its track's bands cut where another track plays."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

Makes room in its track for another, band by band: it listens to the other track by sidechain and turns its own track down in each of 32 bands by as much as the other is loud there, so a vocal comes through the guitars without the guitars ducked as a whole. Amount, attack and release, the range it cuts in, only where the two clash, and each side cut by where the other sits. No latency.

[Molnlucka on the website](/solmara/effects/#molnlucka)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Amount | 0% to 100% | 50% |
| Attack | 0.1 ms to 500 ms | 10 ms |
| Release | 1 ms to 5000 ms | 150 ms |
| Depth | 0 dB to 30 dB | 18 dB |
| Low cut | 20 Hz to 2000 Hz | 20 Hz |
| High cut | 500 Hz to 20000 Hz | 20000 Hz |
| Stereo | Follow it, Stereo, L / R, M / S | Follow it |
| Balance | -1 linear to 1 linear | 0 linear |
| Only where they clash | Off, On | On |
| Freeze | Off, On | Off |
