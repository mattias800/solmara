Cosine Zone is a phase-distortion synthesizer in the image of the Japanese home keyboards of the mid-1980s that brought digital synthesis to bedrooms at a fraction of the price of the big FM and analogue machines. Their method, **phase distortion**, was their own: instead of filtering a bright wave to make it darker, they start from a pure cosine and bend the way it is read, so it grows brighter. The result sits between analogue and FM: saws and squares that sweep like a filter, resonant squelches without a resonant filter, glassy bells and electric pianos, and basses that became staples of house and techno.

Two lines, each a waveform with three eight-step envelopes: one for the pitch, one for the bend (the brightness), one for the level. Cosine Zone models the phase-distortion engine, the envelopes as the original steps through them, its ring and noise modulation, and even the original's digital-to-analogue converter.

## At a glance

- **Eight voices** with one line, **four** with two.
- **Two lines**, each with a **DCO** (the wave), a **DCW** (the bend: how far the wave is distorted) and a **DCA** (the level).
- **Eight waveforms:** saw, square, pulse, double sine, saw-pulse, and three **resonance** waves; a line can alternate two waves.
- **Three eight-step envelopes a line**, for the pitch, the bend and the level, each with a sustain step and an end step.
- **Line select:** 1, 2, 1+1' (line 1 doubled and detuned) or 1+2' (both lines).
- **Detune** of line 2 by octaves, notes and cents.
- **Ring** and **noise** modulation between the lines.
- **Vibrato** with four waves and a delay; **portamento**; **bend range**; **octave**.
- **DAC**: the original's converter, its steps and its slight dullness at the top, or a clean output.

## Signal flow

<Flow
  caption="One voice of Cosine Zone with both lines (1+2'). Each line is a cosine whose reading is bent by its DCW envelope and shaped in level by its DCA envelope."
  voice={3}
  voices="Each voice"
  columns={[
    [{id: 'dco1', label: 'Line 1 DCO', note: 'wave · pitch'}, {id: 'dco2', label: 'Line 2 DCO', note: 'wave · pitch · detune'}],
    [{id: 'dcw1', label: 'Line 1 DCW', note: 'bend'}, {id: 'dcw2', label: 'Line 2 DCW', note: 'bend'}],
    [{id: 'dca1', label: 'Line 1 DCA', note: 'level'}, {id: 'dca2', label: 'Line 2 DCA', note: 'level'}],
    [{id: 'dac', label: 'DAC', note: 'or clean'}],
  ]}
  links={[['dco1', 'dcw1'], ['dco2', 'dcw2'], ['dcw1', 'dca1'], ['dcw2', 'dca2'], ['dca1', 'dac'], ['dca2', 'dac']]}
  mods={[
    {label: 'DCO envelopes', to: ['dco2']},
    {label: 'DCW envelopes', to: ['dcw2']},
    {label: 'DCA envelopes', to: ['dca2']},
    {label: 'Ring / noise', to: ['dco2']},
  ]}
/>

There is no filter. Each line's brightness comes from the DCW: at its envelope's lowest level, the wave is a pure cosine, as dark as a sound can be; as the DCW envelope rises, the cosine's reading is bent further, and the wave turns into the saw, square or resonance shape you chose, bright and buzzy. Sweeping the DCW is like sweeping a filter, and sounds a little different: cleaner, more vocal, and on the resonance waves like a resonant filter singing.

## The face

### In the device chain

In the chain, Cosine Zone shows a compact face by default. Its full face has **LINE 1** over **LINE 2**, each with its three envelopes drawn as curves you can drag by their corners, with **S** (sustain) and **E** (end) flags and a dot for each voice as it plays.

{{chain}}

### Its window

The window has every step's rate and level as fields, the envelopes drawn, and the wave as it is bent right now. Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Cosine Zone has the focus.

{{window}}

Right-click an envelope to copy, paste, swap, reset or shape it; right-click a step to make it the sustain or the end, insert, delete or reset it; right-click a line to copy, swap or reset it. Each is one undo step.

## Phase distortion and the waves

A cosine read evenly from start to finish is a pure tone. Read it fast for part of its cycle and slowly for the rest, and its shape is bent: it gains harmonics. Each **wave** is a way of bending:

- **Saw**: bent to a sawtooth. All harmonics, the brass and string wave.
- **Square**: a square, hollow, odd harmonics.
- **Pulse**: a narrow pulse, nasal.
- **Double sine**: two humps a cycle, an organ-like tone.
- **Saw-pulse**: half saw, half pulse, a bright and thick combination.
- **Resonance I, II, III**: a sine at a higher frequency inside each cycle, fading toward its end (I a saw-like window, II a triangle, III a trapezoid). The DCW sweeps the inner sine's pitch, which sounds like a resonant filter sweeping: the instrument's famous squelch, without a filter.

With the DCW at nothing, every wave is the same pure cosine. The DCW's level is how far toward the wave it goes.

A line can have a **second wave**: then it plays the two in alternate cycles, an octave under the key, for richer, hollow or organ-like timbres.

## The envelopes

Each line has three envelopes, and each envelope has **eight steps**. A step has a **rate** (how fast it moves, 0 to 99) and a **level** (where it goes, 0 to 99). When you strike a key, the envelope starts from nothing and moves to step 1's level at step 1's rate, then on to step 2, and so on.

- **Sustain** (S): the step where it holds while you keep the key down.
- **End** (E): the last step; its level is always nothing.

On release, the envelope goes on from the step after the sustain to the end. A rate is a speed: half the way takes half the time.

- **DCO envelope**: the pitch. Small levels are fine pitch movements (about 12 cents a level), large ones whole semitones. A fast drop from a high level is a drum's thump; steps of different pitches make arpeggios and trills inside one note.
- **DCW envelope**: the bend. This is the filter envelope of the instrument: a quick rise and a fall to a lower sustain is a pluck; a slow rise a swell.
- **DCA envelope**: the level.

Eight steps make shapes no ADSR can: double attacks, bends that pluck the resonance four times in one key, levels that gate a held chord into a rhythm, pitch steps that climb an arpeggio as you let go.

**Key follow** for the DCW makes it smaller and its envelope faster higher up the keyboard, as a real instrument's high notes are duller and shorter; for the DCA, it makes the level envelope faster higher up.

## Lines, detune and modulation

**Line select**:

- **1**: line 1 alone, eight voices.
- **2**: line 2 alone.
- **1+1'**: line 1 doubled, the copy detuned by the detune controls. Thick, chorused, four voices.
- **1+2'**: both lines, each with its own settings, line 2 detuned. Two sounds layered, four voices.

**Detune** moves line 2 (or the copy) by **octave**, **note** and **fine** (up to a semitone).

**Modulation**, in 1+2':

- **Ring**: line 2 multiplied by line 1. Metallic, bell-like, inharmonic: the instrument's bells and chimes.
- **Noise**: line 2's speed switched at random, a breathy or cymbal-like noise.

## Performance

- **Vibrato**: a **wave** (triangle, saw up, saw down, square), a **delay** before it starts, a **rate** and a **depth**.
- **Octave** moves the whole instrument an octave down or up.
- **Portamento** on or off, with its **time**.
- **Bend range** up to 12 semitones for the track's pitch bend.
- **DAC** on gives the original's converter, its small steps and its softened top: a slightly grainy, warmer sound. Off, the output is clean.
- **Volume** in dB.

A key takes a silent voice, or else the oldest one; a key struck again takes a new voice while the old one's release still sounds.

## Your first patch: the saw bass that sweeps like a filter

From a new Cosine Zone (line 1's saw, a DCW that opens and settles):

1. **Line 1, saw.** Octave -1.
2. **DCW envelope:** step 1 rate 99, level 80; step 2 rate 60, level 10, sustain on step 2; step 3 rate 70, end.
3. **DCA envelope:** step 1 rate 99, level 99, sustain; step 2 rate 75, end.
4. **Play it.** Each note snaps bright and falls dark, like a filter envelope. Change step 2's rate to make the decay longer.
5. **Now switch the wave to Resonance II** and hear the same envelope squelch.

## Starting points

- **Squelch bass.** Resonance I, DCW step 1 rate 95 level 99, step 2 rate 55 level 0, DCA a short organ gate.
- **Digital bell.** 1+2', Modulation Ring, both lines saw, line 2 detuned up an octave and a fifth, DCA long decays.
- **Electric piano.** 1+1', square with a short DCW pluck, detune fine 8.
- **Brass.** Saw, DCW step 1 rate 60 level 70 (a slow opening), sustain level 50, vibrato with delay.
- **Gated chord.** DCA levels alternating 99 and 0 across steps 1 to 7 at the same rate, sustain on 7: a held chord stutters.

## Tips

- **Think of the DCW as the filter.** Bright means more DCW, dark means less.
- **The resonance waves need DCW movement** to sound resonant; held still they are a fixed tone.
- **Two lines halve the voices.** Use 1+1' for thickness only when you don't need eight notes.
- **Steps are cheap.** If an ADSR doesn't do it, use more steps.
