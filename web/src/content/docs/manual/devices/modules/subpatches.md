---
title: "Modules: Subpatches"
description: "Modules of your own, made of other modules."
sidebar:
  label: "Subpatches"
  order: 11
---

<!-- Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page. -->

Modules of your own, made of other modules.

Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.

## Subpatch

Modules and cables of its own, as one module: its jacks are the Subpatch Inputs and Outputs inside it. Cmd/Ctrl+G makes one of the modules selected; double-click it to open it.

No jacks.

## Subpatch Input

A jack of the subpatch it is in: what is patched into that jack from outside comes out of it here.

- **In:** None
- **Out:** Output (control)

| Knob | Range | Starts at |
| --- | --- | --- |
| Kind | Audio, CV, Gate, Pitch | CV |

## Subpatch Output

A jack of the subpatch it is in: what is patched into it here goes out of that jack.

- **In:** Input (control)
- **Out:** None

| Knob | Range | Starts at |
| --- | --- | --- |
| Kind | Audio, CV, Gate, Pitch | CV |
