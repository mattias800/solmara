Promise Bloom is a five-voice polyphonic synthesizer in the image of the American polysynth of the late 1970s that changed what a synthesizer was: the first that remembered every knob. Before it, a polyphonic synth was a huge, fragile machine and a sound was something you set up by hand; after it, a player could call up a brass patch, a string patch and a lead in one song. Its sound became the sound of the late seventies and early eighties: warm, slightly unruly brass, thick pads, round basses, and the strange, vocal sweeps of its Poly-Mod section.

Each voice is a small monosynth: two oscillators, a mixer with noise, a resonant four-pole filter with its own envelope, and an amplifier with another. On top of that sit two modulation sections that give it its character: **Poly-Mod**, where each voice's filter envelope and second oscillator modulate the first oscillator and the filter at audio rate, and **Wheel-Mod**, where the LFO and noise reach the oscillators and the filter by the mod wheel. Promise Bloom models each stage from its circuit, the oscillator chips' ramps and pulses, the filter's four stages, the envelopes' segments, down to each voice's own slight tuning error.

## At a glance

- **Five voices**, each with two VCOs, a mixer, a 24 dB/octave resonant low-pass and two ADSR envelopes.
- **Oscillator A:** saw and pulse together or apart, pulse width, sync to B.
- **Oscillator B:** saw, triangle and pulse, fine tuning, a low-frequency mode and a keyboard switch, so it can be a modulator.
- **A mixer** for A, B and noise.
- **Poly-Mod:** the filter envelope and oscillator B modulating A's pitch, A's pulse width and the filter, in every voice.
- **One LFO** with saw, triangle and square, mixable, and **Wheel-Mod** sending the LFO and noise by the mod wheel.
- **Glide**, **unison** with detune, a release switch, a pitch wheel with a range up to an octave.

## Signal flow

<Flow
  caption="One voice of Promise Bloom; the whole frame is built five times. Poly-Mod works inside each voice, at audio rate: the voice's own filter envelope and oscillator B move oscillator A and the filter."
  voice={4}
  voices="Each of the five voices"
  wrap={2}
  columns={[
    [{id: 'a', label: 'Oscillator A', note: 'saw · pulse · sync'}, {id: 'b', label: 'Oscillator B', note: 'saw · tri · pulse'}, {id: 'noise', label: 'Noise'}],
    [{id: 'mix', label: 'Mixer'}],
    [{id: 'vcf', label: 'Filter', note: '24 dB low-pass'}],
    [{id: 'vca', label: 'Amplifier'}],
    [{id: 'vol', label: 'Volume'}],
  ]}
  mods={[
    {label: 'Poly-Mod', to: ['a', 'vcf']},
    {label: 'Wheel-Mod', to: ['a', 'b', 'vcf']},
    {label: 'Filter env', to: ['vcf']},
    {label: 'Amp env', to: ['vca']},
  ]}
/>

The two oscillators and the noise meet in the mixer, go through the filter, which its own envelope opens and closes, and the amplifier, which its envelope shapes. The modulation is where Promise Bloom becomes more than a monosynth five times over: Poly-Mod brings the filter envelope and oscillator B into oscillator A and the filter, and Wheel-Mod brings the LFO or noise into both oscillators and the filter, as far as the mod wheel lets it.

## The face

### In the device chain

In the chain Promise Bloom shows its whole panel in the original's three rows: Poly-Mod, oscillator A, the mixer, the filter and its envelope on top; the LFO, oscillator B and the amplifier in the middle; Wheel-Mod, glide and unison, the five voices' lamps and the wheels at the bottom. A compact face, for a long chain, keeps the filter, both envelopes drawn, the mixer, glide, unison and the volume.

{{chain}}

### Its window

The window lays the panel out in three columns in the order the sound travels: the modulation, the oscillators and the mixer, then the filter and the amplifier. Each oscillator draws the wave it makes, the LFO draws its mix of shapes, the filter draws its response (drag the corner for the cutoff and the resonance), and both envelopes are drawn to be dragged at their corners. Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Promise Bloom has the focus.

{{window}}

While it plays, each voice's lamp lights, the filter's response shows a dot at each voice's cutoff, each envelope shows a dot for each voice, and the LFO a dot where it is. Right-click an envelope's knobs to copy it to the other envelope or reset it.

## The oscillators

The original's oscillators drift and differ slightly from voice to voice, and so do Promise Bloom's: each voice has its own small tuning error and wander. That is a large part of why five voices playing the same chord sound like an ensemble.

### Oscillator A

- **FREQUENCY** tunes A in semitones over two octaves either way; the middle is in tune with the keys.
- **SHAPE:** **saw** and **pulse** keys, each on or off. Both on adds them together, a brighter, thicker sound than either.
- **PULSE WIDTH** from thin to square (5) to thin again.
- **SYNC** locks A to B: every time B starts its cycle, A restarts. A's harmonics stay at A's pitch while the note's pitch is B's. Tune A above B and sweep A's pitch (with Poly-Mod's filter envelope, for example) for the classic tearing sync lead.

### Oscillator B

- **FREQUENCY** and **FINE** (up to a semitone, for detuning against A).
- **SHAPE:** **saw**, **triangle** and **pulse** keys, any of them together.
- **PULSE WIDTH**, as on A.
- **LO FREQ** takes B down seven and a half octaves, to a slow wave: a second LFO, for Poly-Mod.
- **KEYBOARD**: off, B no longer follows the keys and holds the pitch its knob sets, a drone under the melody or a fixed modulator for Poly-Mod.

### Mixer

**OSC A**, **OSC B** and **NOISE**, each a level. Noise is a single white-noise source shared by the voices, for breath, wind and percussion.

## The filter

A four-pole low-pass, 24 dB an octave, built like the original's from four transconductance stages with a resonance loop, the loop itself bending gently when pushed.

- **CUTOFF** covers about ten octaves, up to 7.3 kHz.
- **RESONANCE** emphasises the cutoff; from about 6.5 the filter sings on its own, and higher up it is a sine-wave oscillator. As resonance rises, the bass thins.
- **ENV AMOUNT** is how far the filter envelope opens the filter, up to 8 octaves.
- **KEYBOARD** on makes the filter follow the keys an octave an octave, so the tone is even across the keyboard and a singing filter plays in tune.

The filter has its own **ATTACK**, **DECAY**, **SUSTAIN** and **RELEASE** under it.

## The amplifier and envelopes

The amplifier has its own ADSR envelope. Both envelopes work like the original's: the attack charges toward a point past full and turns as it reaches it, so it rises quickly and bends over; the decay and the release fall exponentially. The filter envelope's times are a little faster than the amplifier's at the same settings.

**RELEASE** (by the volume) is the original's release switch: off, both envelopes let go at once when you lift a key, whatever their release; on, each takes its release time. Switch it off for tight, organ-like playing without resetting the envelopes.

## Poly-Mod

Poly-Mod is the section that makes this instrument distinctive. In every voice, two sources can modulate oscillator A and the filter:

- **FILT ENV**: the filter envelope, by its amount.
- **OSC B**: oscillator B, by its amount, at audio rate.

and three keys choose where they go (**DESTINATION**):

- **FREQ A**: A's pitch. The filter envelope on FREQ A, with SYNC on, is the sync sweep. Oscillator B on FREQ A is frequency modulation: metallic, bell-like and clangorous tones, growls with B low.
- **PW A**: A's pulse width, swept by the envelope or buzzed by B.
- **FILTER**: the cutoff. Oscillator B on the filter at audio rate makes the filter itself a source of new partials: vowel sounds, hollow tones, aggressive basses.

Because each voice has its own envelope and its own oscillator B, the modulation is polyphonic: every note of a chord moves on its own.

## LFO and Wheel-Mod

The **LFO** has a **FREQUENCY** from a slow sweep to over 20 Hz (about 0.2 Hz at 2.5, 1 Hz at 5, 5 Hz at 7.5) and three **SHAPE** keys: **saw**, **triangle** and **square**. Any of them can be on together; their sum is the LFO's wave.

**Wheel-Mod** sends a mix of the LFO and noise (**SOURCE MIX**, from the LFO alone to noise alone) to **FREQ A**, **FREQ B**, **PW A**, **PW B** and **FILTER**, by as much as the **mod wheel** is pushed. The LFO to both frequencies is vibrato; to the pulse widths it is the slow, chorus-like movement of the era's pads; noise to the filter is a rough growl.

A new Promise Bloom has the triangle LFO on the wheel to both oscillators' pitch: push the mod wheel for vibrato.

## Performance

- **GLIDE RATE** slides each voice from its last note to the next, slowing as it arrives.
- **UNISON** puts all five voices on the lowest key held, spread by **DETUNE**, which the original did not have. A thick monophonic bass or lead.
- **PITCH** and **MOD** are the wheels: the track's pitch bend and your keyboard's mod wheel. **BEND** sets the pitch wheel's range, 1 to 12 semitones.
- **MASTER TUNE** moves everything a semitone either way, and **VOLUME** is the output.
- **QUALITY**: **Full** runs the oscillators and filters at twice the sample rate (the default), **Light** at the rate, for half the processing and almost the same sound.

A key takes the free voice that last played it, or else the next free voice in turn; with five held, a sixth takes over the voice after the last one taken. The oscillators run freely, so no two notes start quite alike. Promise Bloom does not answer velocity, as the original did not.

## Your first patch: the sync sweep

From a new Promise Bloom:

1. **Sync.** Oscillator A **SYNC** on, A's saw only, B's saw only. Mixer: OSC A 10, OSC B 0.
2. **Tune it up.** A's FREQUENCY up an octave.
3. **Sweep it.** Poly-Mod **FILT ENV** 5, destination **FREQ A**. Filter envelope: ATTACK 0, DECAY 5, SUSTAIN 2.
4. **Hear it.** Each note now sweeps down through its harmonics. Change Poly-Mod's FILT ENV to make the sweep wider or narrower.
5. **Shape the filter.** CUTOFF 7, RESONANCE 2, ENV AMOUNT 3.

## Starting points

- **Brass.** Both saws, B's FINE a little up, CUTOFF 3, ENV AMOUNT 6, RESONANCE 1. Filter envelope A 2, D 4, S 5, R 2. Amplifier A 1, S 10, R 2.
- **Poly-Mod bell.** A's pulse at width 5, B's triangle with KEYBOARD on, B tuned up an octave and a fifth, OSC B level 0, Poly-Mod **OSC B** 4 to **FREQ A**. Amplifier A 0, D 7, S 0, R 7; CUTOFF 8.
- **Vocal sweep.** B LO FREQ on, B's triangle; Poly-Mod OSC B 3 to **FILTER**; RESONANCE 6.
- **Fat unison bass.** UNISON on, DETUNE 3, both saws, A down an octave, CUTOFF 2.5, RESONANCE 3, ENV AMOUNT 6, filter D 3, S 1.
- **Pad with movement.** Both pulses, Wheel-Mod LFO to PW A and PW B, triangle LFO at 3, mod wheel up a third, filter and amplifier attacks at 5, releases at 6.

## Tips

- **Poly-Mod on the filter at audio rate** is the instrument's secret weapon for basses: oscillator B at the same pitch as A, a little OSC B to FILTER.
- **Keep the release switch in mind.** If a sound will not ring out, check that RELEASE is lit.
- **Five voices** run out sooner than you think with long releases: shorten them on fast chord parts.
- **For vibrato only on the wheel**, leave Wheel-Mod's destinations on the frequencies and the source on the triangle LFO, as a new one has.
