Oberon Eight is an eight-voice polyphonic synthesizer in the image of the American polysynth of the early 1980s that could play two complete sounds at once, layered or split across the keyboard. Its sound is big, bright and brassy: the synth that blasted the most famous riffs of eighties rock and pop, the stabs of arena anthems and the lush, wide pads of the same records. Where some of its rivals were warm and round, this one is bold: open filters, punchy envelopes and a two-pole filter mode that keeps the edge of its oscillators.

Each voice is a complete analogue synth on its own card: two oscillators with sync and cross-modulation, a mixer with noise, a resonant filter switchable between four and two poles, and two envelopes. A processor held the programs and played two of them at once. Oberon Eight models each voice from its circuit, and keeps two full patches, **Upper** and **Lower**, each with every control.

## At a glance

- **Eight voices**, each with two oscillators, a mixer, a resonant low-pass and two ADSR envelopes.
- **Oscillator 1:** saw and pulse together or apart, 16' to 2'. **Oscillator 2:** saw and pulse, over five octaves, with detune.
- **One pulse width** for both, **sync** of oscillator 2 to oscillator 1, and **cross-modulation** (oscillator 2 on oscillator 1's frequency).
- **A low-pass filter** of **4 poles** (24 dB an octave) or **2 poles** (12 dB), resonant, with key tracking.
- **A filter envelope** and **a loudness envelope**.
- **An LFO** (sine, square, sample and hold) with two depths: one for the frequencies, one for the pulse widths and the level.
- **Two patches, Upper and Lower:** played **whole**, **double** (layered) or **split**.
- **Unison**, **portamento**, **hold**, a **bender** (to both oscillators or oscillator 2 alone) and a **modulation lever** for vibrato with its own rate and wave.

## Signal flow

<Flow
  caption="One voice of Oberon Eight; the frame is built eight times. In double and split, four voices play the upper patch and four the lower."
  voice={4}
  voices="Each of the eight voices"
  columns={[
    [{id: 'o1', label: 'Oscillator 1', note: 'saw · pulse'}, {id: 'o2', label: 'Oscillator 2', note: 'saw · pulse · sync'}, {id: 'noise', label: 'Noise'}],
    [{id: 'mix', label: 'Mixer'}],
    [{id: 'vcf', label: 'Filter', note: '4 or 2 poles'}],
    [{id: 'vca', label: 'Amplifier'}],
    [{id: 'vol', label: 'Volume'}],
  ]}
  mods={[
    {label: 'Osc 2 (X-mod)', to: ['o1']},
    {label: 'LFO', to: ['o2', 'vcf', 'vca']},
    {label: 'Vibrato lever', to: ['o2']},
    {label: 'Filter env', to: ['vcf']},
    {label: 'Loudness env', to: ['vca']},
  ]}
/>

Two oscillators and noise meet in the mixer, go through the filter, which its envelope sweeps, and the amplifier, shaped by the loudness envelope. The LFO reaches the oscillators' pitch, the filter, the pulse widths and the level, each by a switch; the lever's vibrato has an LFO of its own. Oscillator 1 can reset oscillator 2 (sync), and oscillator 2 can modulate oscillator 1's pitch at audio rate (cross mod).

## The face

### In the device chain

{{chain}}

### Its window

The window has both patches, **UPPER** over **LOWER**, each a full panel with pictures at the right: the LFO's wave, the two oscillators' waves, the filter's response and both envelopes, each dragged by its points. Under them are the levers, the manual controls, the keyboard modes and a keyboard on which you drag the split point. Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Oberon Eight has the focus.

{{window}}

Beside each patch, its name, the voices it plays (**VOICES 1-8**, or 1-4 and 5-8 in double and split) and lamps for its voices; a patch that is not played says **NOT HEARD**.

## The oscillators

- **OSC 1** sets oscillator 1's footage: 16', 8', 4' or 2'. **SAW** and **PULSE** switch its waves on, either or both.
- **OSC 2** tunes oscillator 2 in semitones over five octaves (0 to 60), and **DETUNE** a semitone either way of that. Oscillator 2 a few cents from oscillator 1 is the classic thick sound; a fifth or an octave above, a fuller chord-like tone.
- **PW** sets the pulse width of both oscillators' pulses.
- **SYNC** resets oscillator 2 every time oscillator 1 starts its cycle. Tune oscillator 2 above oscillator 1 and sweep it for the hard-sync lead.
- **X-MOD** (cross mod) lets oscillator 2 modulate oscillator 1's frequency at audio rate: metallic, clanging, bell-like tones, or a growl at low amounts.

## The filter

- **OSC 1**, **OSC 2** and **NOISE** are the mixer's levels into the filter.
- **FREQ** is the cutoff, **RES** the resonance, **ENV** how far the filter envelope moves it.
- **4 POLE** lit: 24 dB an octave, deep and round. Unlit: **2 poles**, 12 dB an octave, brighter and more open. The two-pole mode is a big part of this instrument's sound: it keeps the brassy rasp of the saws.
- **TRACK** makes the cutoff follow the keys.

## The envelopes

The **FILTER ENVELOPE** and the **LOUDNESS ENVELOPE** each have **A**, **D**, **S** and **R**. The filter envelope sweeps the cutoff by **ENV**; the loudness envelope shapes the level. Both are drawn at the right of the patch, to be dragged by their corners.

## Modulation: the LFO

- **RATE**, and its wave: **SINE**, **SQR** (square) or **S/H** (sample and hold, a random step every cycle).
- **FREQ** is the depth on the frequencies, sent by **OSC 1**, **OSC 2** and **FILT** (the filter's cutoff).
- **PW** is the depth on the pulse widths and the level, sent by **PW 1**, **PW 2** and **VOL**.

So one LFO can give vibrato (FREQ to OSC 1 and OSC 2), a wah (FREQ to FILT), pulse-width movement (PW to PW 1 and PW 2) and tremolo (PW to VOL) at once, at two different depths.

## Levers and manual control

- **BEND** is the pitch-bend lever (the track's pitch bend), its range from 1 to 24 semitones (**RANGE**). **BEND 2** bends oscillator 2 alone, so a bend opens an interval between the two oscillators.
- The **modulation lever** (your keyboard's mod wheel) brings in a vibrato of its own, with its **RATE**, **DEPTH** and wave (**SAW**, **SINE**, **SQR**), sent to **MOD 1** and **MOD 2** (the oscillators).
- **VOLUME** and **TUNE** are the output level and the master tune. **HOLD** keeps notes sounding after you let go.
- **PORTA** (portamento) glides between notes; **UNISON** stacks all the voices on one note for a huge monophonic sound.

## The keyboard: whole, double, split

- **WHOLE:** the upper patch on all eight voices.
- **DOUBLE:** every key plays both patches, four voices each, layered. Brass over strings is the classic.
- **SPLIT:** the lower patch below the split point, the upper above it, four voices each. Drag along the keyboard in the window to move the split, or step it with the arrows beside **AT**.

Each patch has every control of its own; the window shows both at once.

**LIGHT** and **FULL** are the quality: Full runs the oscillators and filters at twice the sample rate, Light at the rate.

## Your first patch: the anthem brass

From a new Oberon Eight:

1. **Two saws.** OSC 1 8', saw; OSC 2 saw at the same pitch, DETUNE a little sharp. Mixer OSC 1 and OSC 2 at 7.
2. **Two poles.** 4 POLE off. FREQ 4, RES 1, ENV 6.
3. **The bite.** Filter envelope A 1, D 4, S 4, R 2. Loudness envelope A 0, D 3, S 9, R 2.
4. **Play stabs.** Short chords punch; held chords bloom and settle.

## Starting points

- **Bright pad.** Both saws, DETUNE a little more, 4 POLE off, FREQ 6, loudness A 5, S 9, R 6; LFO SINE at RATE 3, PW to PW 1 and PW 2 with the pulses on as well.
- **Sync lead.** SYNC on, oscillator 2's saw only, OSC 2 up an octave; BEND 2 on with RANGE 12, so the bender sweeps the synced oscillator; PORTA 2.
- **Unison bass.** UNISON on, OSC 1 16', saw and pulse, 4 POLE on, FREQ 3, RES 3, ENV 6, filter D 3, S 1.
- **Cross-mod bell.** X-MOD 5, OSC 2 up 19 semitones, filter open, loudness A 0, D 7, S 0, R 7.
- **Split.** SPLIT at C3: LOWER a bass, UPPER a brass; play both hands.
- **Random filter.** LFO S/H, RATE 6, FREQ depth 5 to FILT, RES 5.

## Tips

- **Try two poles first.** For brass and bright pads, the 12 dB mode is the instrument's character.
- **Two LFO depths, one LFO.** FREQ and PW let a single LFO do vibrato and pulse movement at different depths.
- **BEND 2** turns a bend into an opening interval: the rock-keyboard trick.
- **Double halves the voices.** With two patches layered, each has four.
