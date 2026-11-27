Mini Moonbeam is a three-oscillator monophonic synthesizer in the image of the American portable monosynth of the early 1970s: the one that took the modular synthesizer out of the laboratory, put it in a wooden case with a keyboard, and wired it so that no patch cords were needed. Three oscillators, a mixer, the transistor ladder filter, two contour generators and a modulation section that uses the third oscillator as an LFO. It is the sound of funk and progressive-rock leads, of the fattest basses in hip-hop and G-funk, of countless film scores: a sound so round and heavy that it became the reference every other bass synth is measured against.

The design is simple and the sound is not. Three oscillators slightly out of step with each other, a filter that bends and saturates as it is driven, and the habit of players to turn every mixer level up past where it should be: that is the fatness. Mini Moonbeam models it stage by stage: each oscillator's ramp and its shaper, the mixer's soft limit into the filter, the ladder's transistor stages, the contours' capacitors and even the keyboard's single trigger.

## At a glance

- **Monophonic** like the original, with low-note priority and a single trigger, or **up to eight voices** if you want it polyphonic.
- **Three oscillators**, each with six ranges and six waveforms; oscillators 2 and 3 tuned against oscillator 1; oscillator 3 can leave the keyboard to become a modulator.
- **A mixer** for the three oscillators, the external input (Mini Moonbeam's own output fed back) and white or pink noise.
- **The 24 dB/octave transistor ladder filter**, with emphasis (resonance) that self-oscillates, contour amount and keyboard control.
- **Two contour generators** (attack, decay, sustain), one for the filter and one for the loudness, with the decay switch for the release.
- **Modulation** from oscillator 3 or noise to the oscillators' pitch and the filter, by the mod wheel.
- **Glide**, tune, and what the original did not have: drift, velocity, quality and polyphony.

## Signal flow

<Flow
  caption="Mini Moonbeam's signal flow. With Voices above Mono, each note gets the whole frame: its own oscillators, filter and contours."
  voice={4}
  voices="The voice"
  columns={[
    [{id: 'o1', label: 'Oscillator 1'}, {id: 'o2', label: 'Oscillator 2'}, {id: 'o3', label: 'Oscillator 3'}, {id: 'noise', label: 'Noise', note: 'white or pink'}],
    [{id: 'mix', label: 'Mixer', note: '+ external input'}],
    [{id: 'vcf', label: 'Filter', note: '24 dB ladder low-pass'}],
    [{id: 'vca', label: 'Loudness'}],
  ]}
  mods={[
    {label: 'Osc 3 / noise by the wheel', to: ['o2', 'vcf']},
    {label: 'Filter contour', to: ['vcf']},
    {label: 'Keyboard', to: ['vcf']},
    {label: 'Loudness contour', to: ['vca']},
  ]}
/>

Three oscillators and the noise meet in the mixer and go into the filter, which its contour opens and closes, then into the loudness amplifier, shaped by the second contour. The modulation section takes oscillator 3 or the noise and sends it, as far as the mod wheel lets it, to all the oscillators' pitch and to the filter.

The mixer's **external input** is fed from Mini Moonbeam's own output: turn it up and the instrument feeds back into its filter, the famous trick for an even thicker, overdriven sound.

## The face

### In the device chain

In the chain Mini Moonbeam shows its whole panel, as the original laid it out from left to right: the controllers, the oscillator bank with its range and waveform knobs, the mixer with its rocker switches, the modifiers (filter and contours) and the output, with what the device adds under **MORE**. A compact face, for a long chain, keeps the filter, both contours drawn, glide, the modulation and the mixer.

{{chain}}

### Its window

The window has the whole panel larger, in two rows, with each oscillator's wave drawn at its range, the filter's response (drag its corner sideways for the cutoff and up and down for the emphasis), and both contours, dragged by their corners. Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Mini Moonbeam has the focus.

{{window}}

Right-click an oscillator's range or frequency to tune oscillators 2 and 3 to oscillator 1, in unison, a fifth up or an octave down. Right-click a contour knob to copy that contour to the other, or reset it.

## The oscillators

The oscillator bank is three oscillators, each with:

- **RANGE:** **LO** (seven octaves below 8', a sub-audio wave for modulation), **32'**, **16'**, **8'**, **4'** and **2'**.
- **WAVEFORM:** **triangle** (soft, nearly a sine), **shark-tooth** (a triangle with a saw's edge, between the two), **saw** (bright and full), **square** (hollow), **wide pulse** and **narrow pulse** (thinner, nasal). Oscillator 3 has a **reverse saw** instead of the shark-tooth, which matters when it is a modulator: a ramp that rises slowly and drops.
- Oscillators 2 and 3 have a **frequency** knob, seven semitones either way of oscillator 1.

Each oscillator is built like the original's: an exponential converter, a ramp, and shaper stages that make the waveforms from the ramp, so they are not ideal textbook waves; they have the slight bends and skews of the circuit. The three converters share one reference, a little ripple from the power supply and a common drift. The oscillators run freely and no key restarts them.

**Detuning is the sound.** A new Mini Moonbeam has three saws, the second a few cents sharp and the third an octave down. The slow beating of the second against the first is what makes a single note sound alive.

### Oscillator 3 as a modulator

**OSC 3 CONTROL** off takes oscillator 3 off the keyboard: it rests at the keyboard's lowest C and its frequency knob reaches much further. Set it to **LO** range and it is an LFO for the modulation section, with six wave shapes: the triangle for vibrato, the square for trills, the reverse saw and saw for repeating swoops.

### Mixer

Each source has a level and a rocker switch: **OSC 1**, **OSC 2**, **OSC 3**, **EXTERNAL INPUT** and **NOISE**, the noise **white** (bright hiss) or **pink** (darker, rumbling).

The mixer feeds the filter through a soft limit. Below about half the levels the sound stays clean; above, the filter's input starts to saturate, and the sound gets thicker and more compressed. Players of the original routinely run all three oscillators near the top for exactly this.

## The filter

The heart of the instrument: a four-pole transistor ladder, 24 dB an octave, the filter design that this kind of synth made famous. Its stages bend gently as they are driven, its bass falls away as its resonance rises, and at high resonance it rings with a voice of its own.

- **CUTOFF** runs from -5 to 5 across about fifteen octaves, about 585 Hz at its middle.
- **EMPHASIS** is resonance. A little gives a vowel-like edge; around 7 the filter whistles; at the top it self-oscillates into a pure sine that the keyboard can play.
- **AMOUNT OF CONTOUR** is how far the filter contour opens it, up to more than ten octaves.
- **KEYBOARD CONTROL** has two switches: **1** makes the filter follow a third of each octave you play, **2** two thirds, and both together the whole octave. With both on, a self-oscillating filter plays in tune; with neither, the filter stays put and high notes are darker.

## The contours

Two contour generators, one for the filter and one for the loudness, each with **ATTACK**, **DECAY** and **SUSTAIN**. There is no release knob, as on the original. Instead the **DECAY** switch decides what happens when you let go:

- **Decay on:** the note dies away at the decay knob's time.
- **Decay off:** the note stops at once.

Each contour is a capacitor charging and discharging: the attack rises fast and bends over, the decay and the release fall exponentially. Attack times run from 2 ms to 25 seconds, decay times from a click to 12 seconds.

The loudness amplifier opens over a soft threshold, as the original's does: a slow attack is silent for its first part and then blooms, and a release falls quiet a little before the contour reaches nothing.

### Single trigger and low-note priority

With **Voices** on **Mono**, the keyboard works like the original's:

- **Low-note priority:** with several keys held, the lowest sounds.
- **Single trigger:** a key played while another is held changes the pitch but does not restart the contours. Play legato and the notes flow from one to the next under a single filter sweep; lift your fingers between notes to retrigger the contours.

This is how players of the instrument articulate: legato runs that glide under one envelope, detached notes that each bark.

## Modulation

The **MODULATION MIX** blends between **oscillator 3** and **noise** as the modulation source. Two switches send it: **OSCILLATOR MODULATION** (the oscillators' pitch, up to about half an octave) and **FILTER MODULATION** (the cutoff). The **mod wheel** sets how much reaches them.

- Oscillator 3 on LO with a triangle, to the oscillators: vibrato on the wheel.
- Oscillator 3 on LO with a square, to the filter: a rhythmic gate-like pulse.
- Oscillator 3 at an audio range, to the filter: the filter is modulated at audio rate, for growls, clangs and vowels.
- Noise to the filter: a rough, breathy edge.

## Controllers and output

- **TUNE** moves all three oscillators a few semitones either way.
- **GLIDE** slides from one note to the next at a steady rate, the same time an octave up or down, switched in by its rocker. 0.1 s an octave at 5.
- **The pitch bend** (the track's pitch bend) moves all three oscillators.
- **VOLUME** is the output level.

Under **MORE**, what the original did not have:

- **DRIFT**: a slow, random wander of the oscillators' tuning, each its own share. A little makes the sound breathe.
- **VELOCITY**: on, how hard you strike a key sets the note's loudness. Off (the default), every note plays at full level, as on the original.
- **QUALITY**: **Full** runs the filter at four times the sample rate, **Light** at twice, for less processing.
- **VOICES**: **Mono** (as the original) up to eight voices. With more than one, each note gets a whole voice, its own three oscillators, filter and contours: a polyphonic version of the instrument the original never was.

## Your first patch: the bass

From a new Mini Moonbeam:

1. **Weight.** Oscillator 1 at 16', saw; oscillator 2 at 16', saw, a few cents sharp; oscillator 3 at 32', square. All three mixer levels at 8.
2. **Close the filter.** CUTOFF -2, EMPHASIS 3, AMOUNT OF CONTOUR 6.
3. **Shape it.** Filter contour: ATTACK 0, DECAY 4, SUSTAIN 2. Loudness contour: ATTACK 0, DECAY 5, SUSTAIN 8. DECAY switch on.
4. **Play it.** Short notes bark; legato notes slide under one sweep. Turn GLIDE to 2 and switch it on for a funk slide.

## Starting points

- **Funk lead.** Oscillators 1 and 2 at 8', saw and square, oscillator 2 a few cents sharp; CUTOFF 0, EMPHASIS 5, AMOUNT 5; filter contour A 0, D 4, S 3; GLIDE 2 on.
- **Self-oscillating whistle.** All oscillators off, EMPHASIS 10, both KEYBOARD CONTROL switches on, loudness A 2, S 10: the filter itself plays the melody, in tune.
- **Feedback grit.** Any bass, plus EXTERNAL INPUT on at 5: the output feeds back into the filter.
- **Brass.** Three saws at 8', 8' and 4', CUTOFF -1, AMOUNT 6, filter contour A 3, D 5, S 5.
- **Vibrato on the wheel.** OSC 3 CONTROL off, oscillator 3 on LO with triangle, its mixer level off, MODULATION MIX all oscillator 3, OSCILLATOR MODULATION on; push the wheel.
- **Percussive pluck.** Filter contour A 0, D 2, S 0; loudness A 0, D 3, S 0; DECAY on; EMPHASIS 4.

## Tips

- **Turn the mixer up.** The filter is meant to be driven; the levels near the top are where the fatness is.
- **Use oscillator 3 twice.** Even as a modulator it can be heard if its mixer level is up: a slow drone or a sub that pulses.
- **Play legato for slides, detached for punch.** The single trigger rewards phrasing.
- **For a chord pad**, set Voices to 4 or more; each voice is a complete Mini Moonbeam.
