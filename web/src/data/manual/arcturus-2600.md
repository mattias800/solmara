Arcturus 2600 is a semi-modular synthesizer in the image of the American studio synth of the early 1970s: a tall panel of modules side by side, every one of them pre-wired to the next, and every connection breakable with a patch cord. It was designed for teaching: the panel prints the signal's routes so a student can read the patch without a single cord in it, and you can play it at once, then start patching and learn how a synthesizer works by changing how it is wired. It is also simply a great instrument: the sound of science-fiction effects, droid voices and lasers, of fat leads and percussion, of experimental albums and film sound design.

Three oscillators, noise, a ring modulator, a four-pole filter, two envelopes, a sample and hold, an envelope follower, a lag, a mixer with spring reverb, and a keyboard with its own vibrato and a second voice. In Arcturus 2600 every slider on the panel is an input's level, as on the original; the normal connections are its sound as it starts, and seven inputs can be re-patched from a strip of sources across the top.

## At a glance

- **Monophonic**, or **two voices**: the lowest key on VCO-1 and the filter, the highest on VCO-2 and VCO-3.
- **VCO-1:** saw and square. **VCO-2:** triangle, saw, sine and pulse with width and PWM. **VCO-3:** saw and pulse with width. Five ranges each, from **LO** (an LFO) to an octave up; sync.
- Each oscillator's pitch takes the **keyboard**, the **sample and hold** (or noise), the **ADSR** and a fourth, re-patchable **FM** input, each by its own slider.
- **Noise** from low rumble through pink to white.
- **A ring modulator** with AC or DC coupling.
- **A four-pole resonant low-pass filter** with five audio inputs and three frequency inputs, including the keyboard.
- **An ADSR** and **an AR** envelope, triggered by the keyboard or by the sample-and-hold's clock.
- **A VCA** with a linear (AR) and an exponential (ADSR) control input.
- **A sample and hold** with its own clock, an **envelope follower** and a **lag**.
- **A mixer** with pan and a **spring reverb**.
- **Keyboard controls:** portamento, a delayed vibrato, tune and the voices.

## Signal flow

<Flow
  caption="Arcturus 2600's normalled patch, the sound it makes with no cords: the five audio inputs of the filter, the amplifier and the mixer with its reverb. Each oscillator also feeds the others' pitch and the filter's frequency through sliders."
  wrap={3}
  columns={[
    [{id: 'v1', label: 'VCO-1', note: 'saw · square'}, {id: 'v2', label: 'VCO-2', note: 'tri · saw · sine · pulse'}, {id: 'v3', label: 'VCO-3', note: 'saw · pulse'}, {id: 'noise', label: 'Noise', note: 'colour'}],
    [{id: 'ring', label: 'Ring mod', note: 'saw 1 × sine 2'}],
    [{id: 'vcf', label: 'VCF', note: '4-pole low-pass'}],
    [{id: 'vca', label: 'VCA', note: 'AR lin · ADSR exp'}],
    [{id: 'mix', label: 'Mixer', note: 'pan'}],
    [{id: 'rev', label: 'Spring reverb'}],
  ]}
  links={[['v1', 'ring'], ['v2', 'ring'], ['v1', 'vcf'], ['v2', 'vcf'], ['v3', 'vcf'], ['noise', 'vcf'], ['ring', 'vcf'], ['vcf', 'vca'], ['vca', 'mix'], ['mix', 'rev']]}
  mods={[
    {label: 'S&H', to: ['v1', 'v2']},
    {label: 'ADSR', to: ['v1', 'vcf', 'vca']},
    {label: 'Keyboard', to: ['v3', 'vcf']},
    {label: 'AR', to: ['vca']},
  ]}
/>

On the original, the panel prints these lines, and on Arcturus 2600's face each slider's jack is labeled with what it takes. Every slider in a module is an input level: the filter's **SQR 1** slider is how much of VCO-1's square goes into the filter, its **ADSR** slider how far the ADSR moves its frequency. A new Arcturus 2600 plays VCO-1's square through the filter and the amplifier, shaped by the ADSR.

## The face

### In the device chain

The full panel is very wide, so in the chain Arcturus 2600 shows a compact face: the filter's response, the ADSR and the controls you play.

{{chain}}

### Its window

The window has the whole panel, in three rows of modules on orange-tabbed plates, with pictures on black glass beside them: each oscillator's waves, the noise, both envelopes (dragged by their corners) and the filter's response (its corner dragged for the frequency and the resonance). Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Arcturus 2600 has the focus.

{{window}}

Across the top runs the **patch** strip: a jack for every source the instrument has, from **SAW 1** to **KBD**. Under each module's sliders are its input jacks, labeled with what is normalled into them; a jack with a double ring can be re-patched.

## The oscillators

All three oscillators share their layout:

- **RANGE:** **LO** (sub-audio, an LFO), **-2** and **-1** octaves, **N** (normal) and **+1**.
- **INIT** (initial frequency, in semitones) and **FINE**.
- **KBD:** how much the keyboard moves the pitch. At the top it tracks normally; lower, the keys move it less, for microtonal scales or a fixed drone; at 0 the oscillator ignores the keys.
- **S/H** (VCO-3: **NOISE**), **ADSR** and **FM**: how much each input moves the pitch. The S/H slider gives random stepped pitches; the ADSR, a pitch sweep with each note; FM, audio-rate modulation from its source.

Then each its own:

- **VCO-1** gives a **saw** and a **square**. Its FM input is normalled from **SINE 2**. **SYNC** resets VCO-1 by VCO-2: tune VCO-1 up and sweep it for the hard-sync sound.
- **VCO-2** gives a **triangle**, **saw**, **sine** and **pulse**. **WIDTH** sets the pulse from 10 % to 90 %, and **PWM** sweeps it from its input, normalled from the noise. Its FM is normalled from **SQR 1**. **SYNC** locks it to VCO-1.
- **VCO-3** gives a **saw** and a **pulse** with **WIDTH**. Its second input is the **NOISE** (a random wander of pitch), its FM is normalled from **SINE 2**. **SYNC** locks it to VCO-1. On LO, VCO-3 is the classic modulation oscillator.

The oscillators run freely; no key restarts them.

## Noise and the ring modulator

**noise:** **COLOR** moves from a low rumble through pink to bright white noise; **LEVEL** sets its output, which feeds VCO-2's PWM, VCO-3's pitch, the sample and hold and the filter.

**ring mod** multiplies **IN 1** (VCO-1's saw) by **IN 2** (VCO-2's sine), each by its slider. Instead of two pitches you hear their sum and difference: metallic, bell-like and inharmonic tones that shift strangely as you play, the voice of every robot. **COUPLE** chooses **AC** (audio only, the usual) or **DC**, which also passes slow changes: with an LFO in one input, DC turns the ring modulator into a tremolo.

## The filter: VCF

A four-pole low-pass, 24 dB an octave, built from four transconductance stages with a resonance loop. At high **RES** it sings: a pure sine that stays clean while everything under it passes.

- **FREQ** and **FINE** set the cutoff, **RES** the resonance.
- Five audio inputs: **RING**, **SQR 1**, **PLS 2**, **SAW 3** and **NOISE**, each a level. This is the instrument's mixer: blend any oscillators and noise into the filter.
- Three frequency inputs: **KBD** (how much the keys move the cutoff; at the top a singing filter plays in tune), **ADSR** (the envelope's sweep) and **FM** (normalled from **SINE 2**: VCO-2's sine sweeping the cutoff, at audio rate a vocal growl).

## Envelopes, the amplifier and the mixer

- **adsr:** **A**, **D**, **S**, **R**, for the filter, the oscillators' pitch and the amplifier's exponential input.
- **ar:** **A** and **R**, a second envelope, for the amplifier's linear input. Both envelopes rise toward a point past full, so their attacks are quick and bend over.
- **s/h · clock** **GATE**: **KEY** starts both envelopes from the keyboard; **CLK** starts them from the sample-and-hold's clock, so they repeat by themselves while a key is held: an automatic rhythm.
- **vca:** **VCF** and **RING** are its audio inputs (the filter and the ring modulator); **LIN** (the AR, linear) and **EXP** (the ADSR, exponential) its controls. The exponential input gives a natural fade, the linear one a punchier, more abrupt shape.
- **mixer · reverb:** **VCF** and **VCA** set the levels of the filter's output and the amplifier's into the mixer, **PAN** places the sum, and **REV L** and **REV R** add the spring reverb on each side. The spring is the original's kind of reverb: a metallic splash and boing, wonderful on percussion and effects.

## Sample and hold, follower and lag

- **s/h · clock:** **IN** is the level of the source (normalled from the noise), **CLOCK** the internal clock's rate, from 0.2 to 24 Hz. At each tick, the sample and hold takes its input's value and holds it until the next: from noise, a staircase of random voltages. On an oscillator's pitch, that is the computer bubbling of countless films; on the filter, a rhythmic random wah.
- **follow · lag:** the **envelope follower** turns a signal's loudness into a control voltage (its input normalled from the preamplifier, re-patchable to any source), and the **LAG** smooths whatever passes it, from the follower by default. Patch them for a filter that opens as a sound grows louder, or for slow, smooth random movement.

## The keyboard

- **PORT** (portamento) glides between notes.
- **SPEED**, **DEPTH** and **DELAY** are the keyboard's own vibrato: a sine that arrives after the delay.
- **TUNE** is the master tuning.
- **VOICES:** **1**, the lowest key held plays everything; **2**, the lowest key plays VCO-1 and the filter and the highest plays VCO-2 and VCO-3. Hold two keys and the oscillators split into a duophonic instrument.

A key played over a lower one held does not restart the envelopes. **VOLUME** sets the output; **QUALITY** Full runs the oscillators and filter at twice the sample rate, Light at the rate.

## Patching

Seven inputs can be re-patched, each from any of the 16 sources on the patch strip: VCO-1's, VCO-2's and VCO-3's **FM** inputs, the filter's first audio input (**RING**) and its **FM** input, the sample-and-hold's **IN** and the envelope follower's **IN**. Drag from a source jack on the strip to one of these inputs; the cable hangs between them, faint at rest and bright while you handle it, in front of the panel. Drag a plug off its input to put it back to its normal, or onto another input to move it.

The sources: **SAW 1**, **SQR 1**, **SAW 2**, **TRI 2**, **SINE 2**, **PULSE 2**, **SAW 3**, **PULSE 3**, **NOISE**, **S/H**, **ADSR**, **AR**, **FOLLOW**, **LAG**, **RING** and **KBD**.

### Patches to try

- **Random notes.** VCO-1 S/H slider up, CLOCK at 5: every tick a new random pitch.
- **Self-playing rhythm.** GATE on CLK, ADSR A 0, D 3, S 0; hold a key.
- **Laser zap.** VCO-1 ADSR slider high, ADSR A 0, D 2, S 0: each note sweeps down.
- **Filter FM.** Patch **SAW 3** into the filter's FM, VCO-3 at audio range, FM slider up: vowel growls.
- **Slow random sweep.** Patch **S/H** into the follower's input; the lag smooths it; patch **LAG** into the filter's FM.
- **Ring bells.** RING into the filter at full, the other filter inputs down, VCO-2 detuned from VCO-1, ADSR on the VCA with a long decay, a little reverb.

## Your first patch: the duophonic lead

1. **Two oscillators.** Filter inputs: SQR 1 at 6, PLS 2 at 6. VCO-2 INIT up a fifth.
2. **Two voices.** VOICES **2**. Hold one key and play another above it: the bottom key plays VCO-1, the top VCO-2.
3. **Shape.** FREQ 4, RES 3, filter ADSR 5; ADSR A 0, D 5, S 6, R 3.
4. **Expression.** PORT 2, vibrato DEPTH 3 with DELAY 4.
5. **Space.** REV L and REV R at 3.

## Tips

- **Read the jacks.** Under every slider, its jack says what it is listening to. That is the instrument explaining itself.
- **Turn a module's input sliders down before you patch**, then bring them up while you listen.
- **The KBD sliders are not just on and off.** Partial keyboard tracking makes strange, stretched scales.
- **The spring loves percussion.** A short noise burst through the filter with REV up is the instrument's signature drum.
