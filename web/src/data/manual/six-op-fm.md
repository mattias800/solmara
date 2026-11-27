Six-Op FM is a frequency-modulation synthesizer in the image of the Japanese six-operator FM keyboard of 1983: the instrument that brought digital synthesis to every studio and stage of the decade. Its electric piano is on more ballads than anyone can count, its basses drove the dance music of the eighties, and its bells, marimbas, brass and slap basses defined what "digital" sounded like. It also had a reputation for being impossible to program: there are no filters, no oscillators in the usual sense, and its sound is made by sines modulating sines.

This chapter explains how that works, and once it clicks, FM is one of the most expressive kinds of synthesis there is. Six-Op FM models the original's six operators, its 32 algorithms and feedback, its envelopes and keyboard scaling, velocity, the pitch envelope, the LFO, and the converter's character, and it loads the original's own voice banks (SysEx) as they are.

## At a glance

- **Sixteen voices.**
- **Six operators**, each a sine oscillator with its own **frequency** (a ratio of the key, or fixed), **level**, **envelope**, **keyboard scaling** and **velocity** sensitivity.
- **32 algorithms** that say which operators modulate which, and **feedback** on one operator.
- Beyond the original: **seven more waves** for each operator, from the later four-operator FM chips.
- **A pitch envelope** for all operators.
- **One LFO** with six waves, delay, pitch and amplitude depths, and key sync.
- **Mono** with **portamento**, **transpose**, a **reverb rate** for lingering releases, and **mod wheel, breath and foot** controllers.
- **DAC**: Vintage (the original's converter, its steps and faint noise) or Clean.
- **Loads SysEx voices**: banks of 32 or single voices, from this instrument and the later four-operator ones.

## How FM works

An **operator** is a sine-wave oscillator with its own envelope. An operator can do one of two jobs:

- A **carrier** is heard. Its level is how loud it is.
- A **modulator** is not heard. It wobbles the phase of the operator below it, so fast that you don't hear a wobble but new harmonics. Its level is how **bright** the result is.

A carrier alone is a pure sine. Add a modulator at the same frequency (a ratio of 1 to 1) and the carrier grows brighter, toward a saw-like buzz, as the modulator's level rises. Change the modulator's ratio and the harmonics change: at 2:1 the sound is hollow, like a square or a clarinet; at 1:1 it is like a saw; at ratios that are not whole numbers (3.5, 1.41) the harmonics are no longer a series and the sound turns metallic: bells, gongs, chimes.

And because each modulator has its own envelope, the brightness moves over time: a modulator that decays fast gives a bright attack that softens, the electric piano's bark or a plucked string; one that swells gives brass.

### Algorithms

The **algorithm** says which operators are carriers and which modulate which. Algorithm 5, for example, is three pairs, each a modulator over a carrier:

<Flow
  caption="Algorithm 5: three two-operator pairs. Operators 2, 4 and 6 modulate 1, 3 and 5; the three carriers are heard. Operator 6 feeds back on itself."
  columns={[
    [{id: 'op2', label: 'Operator 2', note: 'modulator'}, {id: 'op4', label: 'Operator 4', note: 'modulator'}, {id: 'op6', label: 'Operator 6', note: 'modulator · feedback'}],
    [{id: 'op1', label: 'Operator 1', note: 'carrier'}, {id: 'op3', label: 'Operator 3', note: 'carrier'}, {id: 'op5', label: 'Operator 5', note: 'carrier'}],
    [{id: 'mix', label: 'Sum', note: 'divided by 3'}],
    [{id: 'vol', label: 'Volume'}],
  ]}
  mods={[
    {label: 'Pitch envelope', to: ['op6']},
    {label: 'LFO', to: ['op5']},
  ]}
/>

Some algorithms stack four or five operators in a tower, each modulating the next, for complex, evolving timbres; some have all six as carriers, an organ of sines; most are in between. The face shows all 32 as a chart: click one to choose it. On the face, carriers are green and modulators maroon, so you can always see which is which.

**Feedback** (0 to 7) lets one operator modulate itself: from a pure sine at 0 to a saw-like buzz at 7. It is how a single operator can sound rich.

## The face

### In the device chain

In the chain, left to right: the **algorithm**, with an LCD showing the algorithm and feedback (and the control you turned last) over the chart of all 32; the **six operators**, each a membrane key (green for a carrier, maroon for a modulator) with its frequency, level, coarse, fine and detune and its envelope drawn; then the **pitch envelope**, the **voice** (poly or mono, glide, volume) and the **LFO**.

{{chain}}

### Its window

The window has every control: the algorithm and feedback, the pitch envelope, the LFO and the voice along the top, the controllers and the reverb rate under them, and each operator as a column: its frequency and what it comes to, its knobs, its envelope over its rates and levels, its keyboard scaling drawn over its break point, its sensitivities and its wave. Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Six-Op FM has the focus.

{{window}}

Click an operator's key to switch it on or off. Right-click it to copy, paste, swap or reset an operator. While you play, each envelope shows a dot for every sounding voice.

## The operators

### Frequency

- **Ratio** mode: the operator plays a multiple of the key's pitch: **coarse** 0.5 or 1 to 31, and **fine** adds hundredths. The classic ratios: 1 (the fundamental), 2 (an octave up), 3 (an octave and a fifth), 0.5 (an octave down); non-whole ratios for bells.
- **Fixed** mode: the operator plays one frequency whatever the key, 1, 10, 100 or 1,000 Hz times the fine setting. For noises, drums, and formants that stay put.
- **Detune** moves it a few cents, more at the bottom of the keyboard. Two carriers detuned against each other give a chorus.

### Level and envelope

**Output level** (0 to 99): for a carrier, its loudness; for a modulator, its brightness.

The **envelope** has four **rates** and four **levels**. When you strike a key, it moves from level 4 to level 1 at rate 1, then to level 2 at rate 2, then to level 3 at rate 3, and holds level 3 while you hold the key. When you let go it moves back to level 4 at rate 4. Higher rates are faster. So a piano-like envelope is: rate 1 fast to level 1 at 99, rate 2 slow to a lower level 2, rate 3 slower still to level 3 at 0, rate 4 medium.

Because a modulator's envelope is its brightness over time, the modulators' envelopes are the timbral envelopes of the sound: a fast-decaying modulator makes the attack bright.

### Keyboard scaling and velocity

- **Break point**, **left depth**, **right depth**, **left curve** and **right curve** scale the operator's level across the keyboard, on each side of the break point, linearly or exponentially, up or down. Use it to make a modulator weaker in the high notes (so they don't get harsh) or a carrier fade out above a point (to split a sound).
- **Rate scaling** (0 to 7) makes the envelope faster up the keyboard, as real strings die faster higher up.
- **Velocity sensitivity** (0 to 7): how much striking harder raises the operator's level. On a modulator, a harder strike is brighter: the most natural dynamics there are, and the reason FM pianos respond so well.
- **Amplitude sensitivity** (0 to 3): how much the LFO's amplitude depth reaches this operator.

### Waves

Beyond the original's sine, each operator can play one of seven waves of the later four-operator chips, all made from the sine: **Squared**, **Half**, **Half squared**, **Double**, **Double squared**, **Humps** and **Humps squared**. As a carrier, each is a different tone; as a modulator, it brings its own harmonics into what it moves, so two operators can do what took several.

## The voice

- **Pitch envelope**: four rates and levels, like an operator's, moving every operator's pitch (level 50 is no change). A fast drop from above makes a drum's thump; a slow rise a sweep.
- **LFO**: **wave** (triangle, saw down, saw up, square, sine, sample and hold), **speed**, **delay**, **pitch depth** (vibrato, as far as **pitch sensitivity** allows) and **amplitude depth** (tremolo or wah, per operator by its amplitude sensitivity). **Key sync** restarts it at every key.
- **Mono** plays one note at a time; a key played under another held goes on without restarting the envelopes. **Portamento time** and **mode**: **fingered** (only when legato) or **full time**.
- **Transpose**, **Volume** (up to +24 dB: the carriers are summed and divided by their number, so a sound with many carriers needs more volume), **Oscillator key sync** (every operator starts its wave from the same point at each key, for a consistent attack).
- **Reverb rate**: once the sound has fallen 18 dB after release, every operator's release slows to this rate, a lingering tail.
- **Wheel**, **breath** and **foot to pitch and amplitude**: how far each controller adds to the LFO's depths. Breath and foot come from MIDI controllers of those kinds.
- **Feedback steps**: **Six-op** (the original's) or **Four-op** (the later chips', reaching much further).
- **DAC**: **Vintage** gives the original's converter with its fine steps and a faint noise and hum while a voice sounds; **Clean** leaves them out.

## Loading voices

Six-Op FM reads the original's own SysEx voice files, the format its sound libraries are still traded in:

- **File > Import SysEx voices as presets** (or right-click the library's **PRESETS** title) saves each voice of a bank as a preset in your library, category FM.
- The four-operator FM synths' voice files load too, each voice turned into a six-operator one as closely as it goes.

## Your first patch: the electric piano

Start from a new Six-Op FM (operator 1 alone, a sine) and choose **algorithm 5** (three pairs).

1. **The body.** Operator 1 (carrier): ratio 1, level 99, rates 99/30/20/50, levels 99/80/0/0.
2. **The tine.** Operator 2 (its modulator): ratio 14, level 60, rates 99/60/30/60, levels 99/0/0/0: a bright ping that dies fast. Velocity sensitivity 5.
3. **Warmth.** Operator 3 (carrier): ratio 1, level 90, the same envelope as operator 1; operator 4 (modulator): ratio 1, level 70, velocity 4, a decay a little slower than operator 2's.
4. **Detune.** Operator 3's detune +3, for a slight chorus between the two carriers.
5. **Play softly and hard**: the harder you strike, the more the tine and the bark come through.

## Starting points

- **FM bass.** Algorithm 5 with one pair: carrier ratio 0.5, modulator ratio 0.5 or 1 at level 75 decaying fast, feedback 5, carrier velocity 2.
- **Bell.** Carrier ratio 1, modulator ratio 3.5, modulator level 70 with a long decay, both long releases.
- **Brass.** Carrier ratio 1, modulator ratio 1 with a slower attack than the carrier (rate 1 lower), feedback 6, LFO vibrato with delay.
- **Organ.** Algorithm 32 (all carriers), each at ratios 0.5, 1, 2, 3, 4, 6 with different levels, as drawbars.
- **Marimba.** Carrier ratio 1, modulator ratio 4 (or 3.5 for wood) with a very fast decay, carrier decay short.

## Tips

- **Modulator level is brightness.** If a sound is too harsh, lower the modulators, not the volume.
- **Watch the colors.** Green operators are heard, maroon ones only color the sound.
- **Use velocity on modulators** for natural dynamics.
- **Ratios tell the character:** whole numbers for harmonic, non-whole for metallic.
- **Start from a preset or a voice bank** and change one operator at a time to learn how it is built.
