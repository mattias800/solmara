Norrsken is a virtual-analogue synthesizer in the image of the Scandinavian keyboard of the turn of the century in its bright red case: one of the first instruments to model an analogue synthesizer in software, and one built for playing live. Its sound is clear, fast and punchy: cutting leads, hard sync screams, glassy FM bells, tight basses, and pads that move under the player's hands. Its signature is the **morph**: every knob can have a second setting, and the key's velocity or the modulation wheel slides the whole sound from one to the other.

Two oscillators with sync, FM and ring modulation, a filter with five types and a distortion, three envelopes, two LFOs (the second doubling as an arpeggiator or an echo), and the wheel, the stick, aftertouch and a pedal. Norrsken models the original's digital engine, measured and then held to it by many rounds of blind listening against the original, and it imports the original's own programs.

## At a glance

- **Twenty voices**; poly, legato or mono; **unison** with detune; **portamento**, automatic or always.
- **Oscillator 1:** pulse, saw, triangle or sine. **Oscillator 2:** pulse, saw, triangle or noise, tuned in semitones and cents, with or without keyboard tracking.
- **Sync**, **linear FM** and **ring modulation**, and an **oscillator balance**.
- **A filter** of five types (**LP 12**, **LP 24**, **HP 24**, **Band-pass**, **Notch + LP**) with **distortion**, keyboard tracking and its envelope.
- **Three envelopes:** filter, amplifier and a **mod envelope** (attack and decay) for oscillator 2's pitch, FM or pulse width.
- **LFO 1:** five waves, five destinations, tempo sync. **LFO 2:** an LFO, an **arpeggiator** or an **echo**, tempo-synced.
- **Morph** on every knob, by **velocity** or by the **wheel**.
- **The wheel**, **the pitch stick**, **aftertouch** and **an expression pedal**, each to its own destination.
- **Imports the original's programs** (SysEx).

## Signal flow

<Flow
  caption="One voice of Norrsken. Oscillator 1 can modulate oscillator 2 by FM, reset it by sync, or ring-modulate it; the balance mixes them into the filter."
  voice={4}
  voices="Each of the twenty voices"
  columns={[
    [{id: 'o1', label: 'Osc 1', note: 'pulse · saw · tri · sine'}, {id: 'o2', label: 'Osc 2', note: 'pulse · saw · tri · noise'}],
    [{id: 'bal', label: 'Balance', note: 'sync · FM · ring'}],
    [{id: 'vcf', label: 'Filter', note: '5 types · distortion'}],
    [{id: 'amp', label: 'Amp'}],
    [{id: 'out', label: 'Output', note: 'stereo modes'}],
  ]}
  mods={[
    {label: 'Mod env', to: ['o2']},
    {label: 'LFO 1', to: ['o2', 'vcf']},
    {label: 'LFO 2 / arp', to: ['o2', 'vcf', 'amp']},
    {label: 'Filter env', to: ['vcf']},
    {label: 'Amp env', to: ['amp']},
  ]}
/>

The two oscillators meet at the balance, go through the filter and the amplifier, and out in one of three stereo modes. The mod envelope and LFO 1 work mostly on the oscillators: oscillator 2's pitch (for sync sweeps), the FM amount, the pulse width. LFO 2 can be an ordinary LFO on the pitch, filter or amplifier, or an arpeggiator, or an echo.

## The face

### In the device chain

In the chain, Norrsken shows its panel in two rows, in the original's order from left to right: the readout over the controllers, the two LFOs, the mod envelope over the voice, the oscillators, and the amplifier and performance over the filter. A compact face, for a long chain, keeps the oscillators' tuning and mix, the filter, the amplifier, LFO 1, the mod envelope and the wheel.

{{chain}}

### Its window

The window has everything in four rows. Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Norrsken has the focus.

{{window}}

Where the original has knobs that make a shape, the face draws the shape: the three envelopes are curves you drag by their corners, the filter's response is dragged across for the cutoff and up and down for the resonance, each LFO's wave is drawn at its rate (LFO 2's as the arpeggio's steps when it plays one), and the oscillators' picture shows both oscillators, synced or ring modulated, and their mix. While it plays, each voice is a dot on each envelope and on the filter. The red digits of the **readout** show the value and name of the control under your hand.

## The oscillators

- **Osc 1 waveform:** pulse, saw, triangle or sine.
- **Osc 2 waveform:** pulse, saw, triangle or noise. **Osc 2 pitch** in semitones and **Osc 2 fine** in cents; **Osc 2 keyboard tracking** off makes oscillator 2 a fixed tone whatever the key, for drones and FM with a fixed modulator.
- **Pulse width** for both pulses.
- **Sync** restarts oscillator 2 with each cycle of oscillator 1. Sweep **Osc 2 pitch** with the mod envelope for the classic tearing sync lead.
- **FM / ring tune**: the amount of **linear FM**, oscillator 1 moving oscillator 2's frequency. Linear FM keeps the pitch steady as the amount grows, so bells and electric pianos stay in tune.
- **Ring modulation** multiplies the two: sum and difference tones, metallic.
- **Oscillator balance** mixes oscillator 1 and oscillator 2.

## The filter

- **Filter type:**
  - **LP 12**: a two-pole low-pass, bright and open.
  - **LP 24**: a four-pole low-pass, round and deep.
  - **HP 24**: a four-pole high-pass, thin.
  - **Band-pass**: a band of the sound, nasal and vocal.
  - **Notch + LP**: a notch with a low-pass, a hollow, phasey tone.
- **Cutoff** and **Resonance**.
- **Filter distortion**: a distortion in the filter section, for gritty leads and basses.
- **Filter keyboard tracking**: off, a third, two thirds or full.
- **Filter envelope amount**, and the filter envelope's **attack**, **decay**, **sustain** and **release**. **Filter envelope velocity** lets the key's strike scale the envelope.

## The amplifier

**Amp attack**, **decay**, **sustain** and **release**, and **Program gain**, the patch's level.

## The mod envelope

**Mod attack** and **Mod decay**, and its **amount**, sent by **Mod envelope destination** to **Pitch 2** (oscillator 2's pitch, for sync sweeps), **FM** (the FM amount, for bell attacks), or **Pulse width**.

## The LFOs

- **LFO 1:** **rate**, **amount**, **waveform** (random, saw, triangle, square, smooth random) and **destination**: pulse width, filter, pitch 2, pitch 1+2 (vibrato) or FM. **LFO 1 clock sync** locks it to the song's tempo.
- **LFO 2 / arpeggiator:** one control chooses what LFO 2 is:
  - an LFO to **Amp** (tremolo), **Pitch 1+2** or **Filter**;
  - an **arpeggiator**: **Arp up**, **Arp down**, **Arp up/down** or **Arp random**, its range set by **LFO 2 amount / arp range** and its speed by the rate or the clock sync; **Arpeggiator hold** keeps it going;
  - an **Echo**: each note repeats, fading.

## Morph

Every knob can have a second setting, its **morph**: where it goes at full velocity, or with the wheel up when the wheel's destination is **Morph**. On the face, a knob's morph is an amber arc beyond its collar, ending in a handle; drag the handle, or **Alt-drag** (**Option-drag** on a Mac) the knob, to set it. Pictures show the morph as an amber ghost, its handles Alt-dragged.

So a single knob turn can be set up to happen by playing: strike harder and the cutoff opens, the attack shortens and the FM rises, all at once and each by its own amount. Right-click a control to clear its morph, swap it with its setting, or set it to its morph; or clear a section's morphs, or all of them.

## Playing it

- **Voice mode:** **Poly**, **Legato** (mono, envelopes not restarted when you play legato) or **Mono**.
- **Unison** with **Unison detune**: voices stacked on each note.
- **Portamento**, and **Automatic portamento**, which glides only when you play legato.
- **Modulation wheel** to its **Wheel destination**: filter, FM, pitch 2, LFO 1 amount or Morph.
- **Pitch stick** (the track's pitch bend), its range by **Pitch bend range**.
- **Aftertouch** and **Expression pedal**, each with its **amount** and **destination** (LFO 1 amount, LFO 2 amount, filter, FM or oscillator 2's pitch).
- **Octave shift** two octaves either way, **Master tuning**.
- **Output mode:** **Auto stereo**, **Mono**, or **Alternate voices** (each new voice to the other side).

The knobs move in whole steps, 128 places, as the original's.

## Importing programs

Norrsken imports the original's documented SysEx programs, from banks of single programs, four-program performances or percussion kits, also from Standard MIDI Files. Each import is one undo step.

## Your first patch: the sync lead

1. **Sync.** Osc 1 saw, Osc 2 saw, **Sync** on, **Oscillator balance** toward oscillator 2. Osc 2 pitch +12.
2. **The sweep.** Mod envelope destination **Pitch 2**, mod attack 0, mod decay 60, amount 70.
3. **Filter.** LP 24, cutoff high, resonance low, a little **Filter distortion**.
4. **Voice.** Voice mode **Legato**, Automatic portamento on, portamento 30.
5. **Morph.** Alt-drag the mod envelope amount's morph higher: strike harder for a wilder sweep.

## Starting points

- **FM electric piano.** Osc 1 sine, Osc 2 sine an octave up, FM / ring tune 40 with the mod envelope to FM (decay 40), amp decay and release long, velocity morph on the FM.
- **Arpeggio.** LFO 2 Arp up/down, clock sync 1/16, arp range 2 octaves, a short pluck, Arpeggiator hold on.
- **Band-pass voice.** Filter Band-pass, resonance high, LFO 1 smooth random to the filter, slow.
- **Wide pad.** Two saws, Osc 2 fine a few cents, LP 12, slow amp envelope, Unison on, Output mode Auto stereo.
- **Distorted bass.** Osc 1 pulse, Osc 2 saw an octave down, LP 24 with distortion, mono.

## Tips

- **Set up morphs as you design.** A sound with a few velocity morphs comes alive under your fingers.
- **Wheel to Morph** turns the wheel into a sound-design control: one movement between two complete sounds.
- **Linear FM stays in tune**, so try it on pads and keys, not only bells.
- **LFO 2 as an echo** saves an effect for quick, rhythmic repeats.
