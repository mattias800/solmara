Vireo is a virtual-analog and wavetable synthesizer in the image of the German synths of the early 2000s that ruled trance, hard dance and electronic pop: a bright red or black box, or a keyboard, with an engine that kept growing through its life. It started as a virtual analog and gained wavetables, a stack of seven saws, a vocoder, three LFOs, four envelopes, a modulation matrix, an arpeggiator with programmable patterns, and a complete effects section: chorus, phaser, delay, reverb, distortion, a filter bank, EQ. Its sound is punchy, clean and very wide, and its basses and plucks are still everywhere in dance music.

Vireo is built from a detailed study of the original's behavior, measured from the original running, and holds a patch exactly as the original does: every byte of it is a control. It loads the original's own patches (SysEx), banks included.

## At a glance

- **Thirty-two voices**, with **unison** of up to eight voices a note, spread in pitch, stereo and LFO phase.
- **Three oscillators** and a **sub-oscillator**, **noise** and a **ring modulator**.
- Oscillators 1 and 2 in several **modes**: **Classic** (saw to pulse, and 64 spectral waves), **HyperSaw** (a stack of saws with its own sub), **Wavetable** and **Wave PWM**.
- **FM** of oscillator 2 by oscillator 1, **sync**, and **saturation**.
- **Two filters**, routed **serial**, **parallel** or **split**, with the first offering analog-style **1- to 4-pole** low-passes.
- **Four envelopes** (filter, amplifier, and two free ones) and **three LFOs**, all syncable to the tempo.
- **A modulation matrix**: six slots, each a source with up to three destinations.
- **Velocity** to many parameters; **three soft knobs** each patch assigns.
- **An arpeggiator** with a 32-step user pattern.
- **Effects:** chorus (several types, including a rotary speaker), phaser, delay (simple, ping-pong, patterns, tape), reverb, distortion, filter bank, character, EQ and bass boost.
- **External input:** an input follower and a vocoder, from another track.

## Signal flow

<Flow
  caption="One voice of Vireo and the effects after the voices. Each voice can be up to eight unison voices; the matrix can route any source to most of what is drawn here."
  voice={4}
  voices="Each voice"
  columns={[
    [{id: 'o1', label: 'Osc 1', note: 'Classic · HyperSaw · WT'}, {id: 'o2', label: 'Osc 2', note: 'FM · sync'}, {id: 'o3', label: 'Osc 3 · sub · noise'}],
    [{id: 'mix', label: 'Mixer', note: 'ring · saturation'}],
    [{id: 'flt', label: 'Filters 1 + 2', note: 'serial · parallel · split'}],
    [{id: 'amp', label: 'Amp', note: 'pan'}],
    [{id: 'fx1', label: 'Effects', note: 'chorus · phaser · more'}],
    [{id: 'fx2', label: 'Delay · reverb'}],
  ]}
  mods={[
    {label: 'LFO 1 · 2 · 3', to: ['o3', 'flt', 'amp']},
    {label: 'Filter env', to: ['flt']},
    {label: 'Amp env', to: ['amp']},
    {label: 'Matrix', to: ['o3', 'flt']},
  ]}
/>

The three oscillators, the sub-oscillator and the noise meet in the mixer, with the ring modulator and the saturation, and go through the two filters (here serial; they can also run in parallel or split the stereo). The amplifier and its envelope shape the voice. The voices go on into the effects: character, chorus, phaser, distortion, filter bank and EQ, then the delay and the reverb.

## The face

### In the device chain

In the chain, Vireo shows a compact face by default: the display and the three soft knobs, the oscillators, the filter and the amplifier's envelope. The full face has the original's fields in two rows: master, modulators, oscillators and mixer over the display, filters, envelopes and effects. As on the original, keys choose which **LFO 1/2/3**, **OSC 1/2/3** and **FILT 1/2** the knobs set, and a lamp list chooses the effect.

{{chain}}

### Its window

The window sets everything side by side, with no select keys: the three LFOs, the three oscillators, both filters with their routing, the input and vocoder, all four envelopes, the matrix's six slots, the effects, the performance settings and the arpeggiator, whose strip shows the user pattern's steps and lights the step it has reached. Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Vireo has the focus.

{{window}}

Across the face: both filters' responses are drawn tall, their corners dragged for the cutoff and the resonance; each envelope is dragged by its corners; while it plays, a dot for each voice sits on its envelopes and at its filter's corner. A **velocity amount** is an amber arc with a handle on its knob (drag it, or Alt-drag the knob); where the **matrix** reaches a knob, a violet arc shows it. Right-click an empty part of a section to copy one oscillator, LFO, filter or envelope onto its twin, swap them, or reset it.

## The oscillators

### Oscillators 1 and 2

Each has a **mode**:

- **Classic**: **Shape** blends from a spectral wave (at the left) through a **saw** (in the middle) to a **pulse** (at the right), whose width is **Pulsewidth**. **Wave Select** chooses the spectral wave, from a sine through 63 others. Turning Shape is a smooth sweep through very different tones.
- **HyperSaw**: a stack of saws in one oscillator, with **Density** (how many) and **Detune spread** (how far apart), and its own sub. The supersaw sound, one oscillator thick.
- **Wavetable**: a table of waves, **Wave Select** choosing the table and **Index** the position in it; moving the index (by an LFO or envelope) sweeps through the table's waves.
- **Wave PWM**: two copies of the wavetable read against each other, a pulse-width-modulation-like thickening.

Then **Semitone**, **Keyfollow**, and for oscillator 2 **Detune**, **FM Amount** (oscillator 1 modulating oscillator 2's frequency; **Osc FM Mode** chooses how), **Sync** (oscillator 2 reset by oscillator 1), and **Filt Env Amt**, which lets the filter envelope sweep oscillator 2's pitch (and **FM Filt Env Amt** the FM amount): the sync sweep and the FM pluck.

### Oscillator 3, sub-oscillator and noise

**Osc 3** adds a third oscillator with its own mode, semitone and detune. The **sub-oscillator** is a square or triangle an octave down. **Noise** has a volume and a color, from dark to bright. The **ring modulator** multiplies oscillators 1 and 2, its own volume in the mix.

### The mixer

**Osc Balance** blends oscillators 1 and 2; **Osc Mainvolume** sets the level into the filters. The **saturation** stage, chosen by **Saturation Curve** (light, soft, middle, hard, digital, wave shaper, rectifier, bit and rate reducers, and filtered variants), gives drive and grit before or between the filters.

**Init Phase** sets whether the oscillators start at a fixed point of their wave with every note (punchy, consistent) or run free (alive).

## The filters

- **Filter 1** modes: **Low Pass**, **High Pass**, **Band Pass** and **Band Stop**, plus **Analog 1 Pole** to **Analog 4 Pole**: a model of an analog ladder-style low-pass, from gentle to steep, warmer and more resonant.
- **Filter 2** modes: Low Pass, High Pass, Band Pass and Band Stop.
- **Cutoff**, **Cutoff2** (filter 2's, or its offset from filter 1 when **Filter2 Cutoff Link** is on), **Resonance** for each, **Env Amt** and **Env Polarity** for each, **Keyfollow** for each.
- **Filter Routing**:
  - **Serial 4**: filter 1 into filter 2, together 4 poles.
  - **Serial 6**: filter 1 into filter 2, 6 poles: the steepest.
  - **Parallel 4**: the two side by side; **Filter Balance** mixes them. Two different filters at once, a low-pass and a high-pass for example.
  - **Split Mode**: filter 1 on the left, filter 2 on the right: stereo filtering.
- **Filter Balance** sets how much of each filter is heard.

## Envelopes

- **Filter envelope** and **amp envelope**: **Attack**, **Decay**, **Sustain**, **Sustain Time** and **Release**. **Sustain Time** is the original's extra stage: after the decay, the level keeps moving up or down from the sustain level over this time, so a held note can keep falling or swell. In the middle it holds still.
- **Envelope 3** and **Envelope 4**: two more, the same shape, for the matrix.

## LFOs

**LFO 1** and **LFO 2** each have a **rate**, a **shape**, **symmetry**, **keyfollow**, **keytrigger** (restart at each note), a **mode** (poly, one per voice, or mono, one for all), an **envelope mode** (it runs once like an envelope), and **clock** sync to the tempo. Each has its own fixed destinations with amounts (LFO 1: the oscillators' pitch, pulse width, resonance, filter gain; LFO 2: shape, FM, both cutoffs, pan) and one free **assign** destination. **LFO 3** is simpler: rate, shape, clock, a **fade-in**, and one destination among the oscillators' pitch, pulse width or sync phase: vibrato or pulse-width movement with its own speed.

## The modulation matrix

Six **Assign** slots, each with a **source** (pitch bend, channel pressure, mod wheel, breath, foot pedal, expression, other controllers, the LFOs, envelopes and more) and up to three **destinations**, each with its own **amount**. Use it for everything the fixed routings don't cover: the mod wheel opening both filters and adding vibrato, aftertouch to the delay send, envelope 3 to the wavetable index.

## Velocity and soft knobs

Velocity can reach: both oscillators' shape, the pulse width, the FM amount, both filters' envelope amounts and resonances, the amplifier and the pan, each by its own amount.

The **three soft knobs** are set up per patch to the controls that matter most for that sound; their names show on the display. Right-click one to choose what it turns.

## Playing

- **Key Mode**: **Poly**, **Mono 1** to **Mono 4** (with and without retrigger and legato glide), and **Hold**.
- **Unison Mode** from **Twin** to eight voices a note, with **Unison Detune**, **Unison Pan Spread** and **Unison Lfo Phase** (each unison voice's LFOs offset, for movement).
- **Portamento Time**, **Bender Range Up** and **Down**, **Bender Scale**.
- **Transpose**, **Patch Volume**, **Panorama**, **Punch Intensity** (a little extra snap at the attack).
- **Control Smooth Mode** smooths stepped controller changes, or quantizes them to the beat.

## The arpeggiator

**Arp Mode**: **Up**, **Down**, **Up&Down**, **As Played**, **Random**, **Chord**, or **Arp>Matrix** (it plays into the matrix as a source). **Octave Range** 1 to 4, **Hold**, **Note Length**, **Swing**, and the **Clock** in note values. The **User** pattern has up to 32 steps, each with its own length and velocity, drawn in the window. The original's factory patterns play as plain steps.

## Effects

- **Character**: a finishing stage: **Analog Boost**, **Vintage 1-3**, **Pad Opener**, **Lead Enhancer**, **Bass Enhancer**, **Stereo Widener**, **Speaker Cabinet**.
- **Chorus**: **Classic**, **Vintage**, **Air Chorus**, **Vibrato** and **Rotary Speaker**, with mix, rate, depth, delay, feedback and LFO shape.
- **Phaser**: 1 to 6 stages, with mix, rate, depth, frequency, feedback and stereo spread.
- **Distortion**: a curve (light to hard, digital, wave shaper, rectifier, reducers, filters, and more) and its intensity.
- **Filter Bank**: a ring modulator, frequency shifter, **vowel filter**, **comb filter**, or crossfading and variable-slope filters, with mix, frequency, resonance and stereo phase.
- **EQ**: low, mid and high bands, and **Bass Intensity** and **Bass Tune**, a low-end boost.
- **Delay**: **Simple**, **Ping Pong** with several ratios, and rhythmic **Pattern** modes; **Delay Type** Classic or **Tape** (clocked, free or with doppler), with send, time or clock, feedback, modulation and color.
- **Reverb**: **Ambience**, **Small Room**, **Large Room** or **Hall**, with send, time, damping, color, predelay and feedback.

## External input: follower and vocoder

Choose another track as Vireo's sidechain and its audio is the **external input**.

- **Input Follower**: the input's loudness drives the filter envelope, so the filters follow another track: a pad that pumps with the drums.
- **Vocoder**: the input (a voice, say) shapes the sound of Vireo's oscillators, or noise, through the filter bands. The filters' controls turn into the vocoder's (carrier and modulator frequencies, Q, spread, bands, attack and release), as their alternative names say.
- **Input Ringmodulator** and FM from the input bring it into the oscillators.

## Loading patches

Vireo reads the original's SysEx: single patches and whole banks of 128, from `.syx` files or Standard MIDI Files. **File > Import SysEx voices as presets** (or right-click the library's **PRESETS** title) saves each patch of a file as a preset, named after it. Older patches are brought up to date as the original does. Some of the original's advanced wave content is not yet heard; a patch that uses it loads and plays the rest.

## Your first patch: the trance pluck

1. **Oscillators.** Osc 1 **HyperSaw**, Density high, Detune spread medium. Osc 2 Classic, Shape at the saw, Detune a little.
2. **Filter.** Filter 1 **Analog 4 Pole**, Cutoff low, Resonance a little, Filter1 Env Amt high.
3. **Envelopes.** Filter envelope: Attack 0, Decay short, Sustain 0. Amp envelope: Attack 0, Decay medium, Sustain 0, Release short.
4. **Velocity.** Flt1 EnvAmt Velocity up a little: harder notes open more.
5. **Effects.** Delay Ping Pong, clocked to dotted eighths; Reverb Hall, a little send.

## Starting points

- **Hoover-ish lead.** HyperSaw, Mono 2 with portamento, Osc2 Filt Env Amt negative for a pitch dive, Chorus Classic.
- **Wavetable pad.** Osc 1 Wavetable, LFO 2 slowly to Shape (the index), filters Parallel 4 with a low-pass and a band-pass, long amp envelope, Reverb Hall.
- **FM bass.** Osc 1 Classic sine, Osc 2 Classic, FM Amount medium with FM Filt Env Amt sweeping it, Mono 1, Bass Intensity up.
- **Vocoder.** Choose a vocal track as the sidechain, Vocoder Mode **In L+R**, both oscillators HyperSaw, hold chords.
- **Stereo split.** Filter Routing Split Mode, filter 1 and filter 2 cutoffs apart, LFO 2 to Cutoff2 for a moving stereo image.

## Tips

- **Shape is a sweep.** On a Classic oscillator, the Shape knob alone goes from a sine through a saw to a thin pulse.
- **Sustain Time keeps a note moving.** Turn it below the middle for notes that keep dying while held, above for swells.
- **Use the matrix** for the mod wheel: one wheel, three destinations.
- **Unison LFO phase** makes unison move instead of just thickening.
