SID is a three-voice chip instrument in the image of the sound chip of the best-selling home computer of the early 1980s. That little chip was a real synthesizer squeezed into silicon: three oscillators with four waveforms, an envelope for each voice, ring modulation and sync, and an analog filter, at a time when other computers beeped. Its musicians wrote whole worlds for it, arpeggiated chords that fake polyphony, buzzing pulse-width basses, drums made from noise and pitch drops, and its sound lives on in chiptune, demoscene music and countless producers' records.

SID gives you the chip as an instrument you can play from a keyboard or a clip, with every one of its controls. It also plays tracker channels, and packed `.sid` tunes play as clips of their own.

## At a glance

- **Three voices**, played **Poly** (three notes at once) or **Unison** (all three on one note).
- Each voice: **triangle**, **saw**, **pulse** or **noise**, or the chip's **combined waves**; a 12-bit **pulse width**; a 4-bit **ADSR**; **transpose** and **detune**; **sync** and **ring modulation**.
- **One shared filter**: low-pass, band-pass, high-pass and their combinations, with **cutoff** and **resonance**, for the voices you choose.
- **Voice 3 direct output** off, to use voice 3 as a modulation source only.
- **Chip model** (the original chip's two revisions, 6581 and 8580) and **clock** (PAL or NTSC).
- **Velocity** scales each voice; **Level** the output.

## Signal flow

<Flow
  caption="SID's signal flow. Each voice is an oscillator and an envelope; any of them can be routed through the one shared filter, the rest go straight to the mix. Sync and ring take the previous voice as their source: voice 1 takes voice 3."
  columns={[
    [{id: 'v1', label: 'Voice 1', note: 'wave · ADSR'}, {id: 'v2', label: 'Voice 2', note: 'wave · ADSR'}, {id: 'v3', label: 'Voice 3', note: 'wave · ADSR'}],
    [{id: 'route', label: 'Filter routing', note: 'per voice'}],
    [{id: 'vcf', label: 'Filter', note: 'LP · BP · HP'}],
    [{id: 'lvl', label: 'Level'}],
  ]}
  links={[['v1', 'route'], ['v2', 'route'], ['v3', 'route'], ['route', 'vcf'], ['vcf', 'lvl']]}
  mods={[
    {label: 'Sync / ring from the previous voice', to: ['v2']},
  ]}
/>

## The face

The face is the home computer itself: its beige case, with the blue screen in text mode at the left showing a line for each voice (its wave, pulse width and envelope in hex), the wave and envelope drawn under it in chunky pixels to drag, and the filter's numbers and response with a dot to drag for the cutoff and the resonance. At the right is the keyboard's well: the waves as keys that combine, **sync**, **ring** and **filter** as function keys, values as keys you drag, and a row for the chip, its clock, the voices, voice 3, the filter's modes and the volume. The compact face is the screen alone.

{{chain}}

## The voices

Each of the three voices has:

- **Waveform**:
  - **Triangle**: soft and flute-like, the classic for melodies and basses.
  - **Saw**: bright and buzzy.
  - **Pulse**: with its **pulse width**, from thin to square. The chip's most famous sound is a pulse whose width is swept: automate the pulse width.
  - **Noise**: for drums, hats and explosions. The noise follows the note's pitch: high notes are hiss, low notes rumble.
  - **Combined waves** (triangle + saw, triangle + pulse, saw + pulse, all three): the chip's odd hybrids, thin, metallic and characterful.
- **Attack**, **Decay**, **Sustain**, **Release**, each 0 to 15 as on the chip. Rate 0 is the fastest, 15 the slowest. The envelopes run on the chip's own clock, not in milliseconds.
- **Transpose** and **Detune**, for chords on one key (in Unison) and thickness.
- **Oscillator sync**: the voice restarts with the previous voice's cycle (voice 1 follows voice 3). Hard-sync tones.
- **Ring modulation**: the previous voice multiplies this one. It works on the triangle: metallic bells and gongs.

The oscillators run freely between notes: a note does not reset its wave or its noise.

## Poly and Unison

- **Poly**: three notes at once. Each new note takes the first free voice, then a released one, then the oldest held one. Because each voice has its own settings, successive notes can have different timbres, which the chip's musicians used deliberately.
- **Unison**: every note plays all three voices together, each with its own transpose and detune. Transpose voices 2 and 3 to a third and a fifth and one key plays a chord; detune them a few cents and it is one fat note. Sync and ring are reliable here, since all three voices always play.

## The filter

One filter, shared by all three voices.

- **Filter mode**: **Low pass**, **Band pass**, **High pass**, **Low + band**, **Notch** (low + high), **Band + high**, **All**, or **Off** (which silences the routed voices).
- **Filter cutoff** (0 to 2047, as on the chip) and **Filter resonance** (0 to 15).
- **Filtered voices** chooses which voices go through the filter, as a sum of 1 (voice 1), 2 (voice 2) and 4 (voice 3): 7 is all three, 5 is voices 1 and 3. The others go straight to the mix.
- **Voice 3 direct output** off removes voice 3's unfiltered sound, so it can be a silent source for sync and ring, or be heard only through the filter.

**Chip model** chooses the original chip's two revisions, the **6581** (the first) and the **8580** (the later). Their filters' cutoff curves differ, so a filter setting made for one is brighter or darker on the other; tunes were written for one or the other.

**Clock** chooses **PAL** or **NTSC** machines' clock. The pitch stays in tune; the envelope timing and the noise follow the clock, as on the real machines.

## Making it move

The chip has no LFO and no filter envelope of its own: its music made everything move from the player program, many times a second. In Solmara, do the same with automation, or play it from a tracker:

- **Pulse-width sweeps**: automate the pulse width slowly up and down.
- **Filter sweeps**: automate the cutoff.
- **Arpeggios**: play fast notes from an arpeggiator or a clip; the chip's chords are fast arpeggios.
- **Drums**: a noise note with a fast decay; a kick is a triangle or pulse note dropping fast in pitch (automate the transpose, or write it in a tracker).

[Trackers and modules](/solmara/manual/guides/tracker/) explains playing SID from tracker channels and playing `.sid` tunes.

## Your first sound: the pulse bass

1. **Voice mode Unison**, voices 2 and 3 waveform **Pulse** too, voice 2 detune a few cents up, voice 3 transpose -12.
2. **Waveform Pulse**, pulse width about a quarter.
3. **Envelope**: attack 0, decay 9, sustain 8, release 4.
4. **Filter**: filtered voices 7, Low pass, cutoff 800, resonance 8.
5. **Automate the pulse width** of voice 1 over two bars for the classic sweep.

## Starting points

- **Lead.** Saw on voice 1 alone, attack 0, decay 6, sustain 10, release 6; automate a little vibrato with detune.
- **Chord on one key.** Unison, voices 2 and 3 transposed +4 and +7 (major) or +3 and +7 (minor), pulse waves.
- **Ring bell.** Triangle with ring modulation on voice 2, voice 1 transposed a fifteenth up, decay 10, sustain 0.
- **Hi-hat.** Noise, a high note, attack 0, decay 3, sustain 0.
- **Sync sweep.** Unison, voice 2 sync on, voice 2 transposed up an octave and automated upward.

## Tips

- **Three voices is the art.** The chip's music made three voices sound like a band: drums on one voice between bass notes, chords as arpeggios.
- **Try both chip models** when a filtered sound is too bright or too dark.
- **Velocity** scales each voice's level.
