Juniper Eight is an eight-voice polyphonic synthesizer in the image of the Japanese flagship polysynths of the early 1980s: two oscillators a voice with sync and cross-modulation, a high-pass and a switchable low-pass filter, two envelopes, and a keyboard that can be split or layered with two complete patches. Instruments of this class were the most expensive synths a studio could buy, and they sounded like it: huge brass, glassy sync leads, deep basses, the shimmering pads of eighties film scores and pop records.

Where the smaller polysynths of the time had one oscillator and a chorus, this one had the full architecture of a big monosynth in every voice, and then eight of them, and then two patches at once. Juniper Eight models each stage from its circuit: the ramp oscillators and their sync, the four transconductance stages of the filter, the envelopes' curves, the voice assignment and the arpeggiator.

## At a glance

- **Eight voices**, each with two VCOs, a mixer, a high-pass, a low-pass, an amplifier and two envelopes.
- **VCO-1:** triangle, saw, pulse or square, from 64' to 2'.
- **VCO-2:** sine, saw, pulse or noise, tuned in semitones and cents, or slowed to a low-frequency modulator.
- **Oscillator sync** either way, and **cross-modulation** of VCO-1's pitch by VCO-2 at audio rate.
- **Pulse width** by hand, by ENV-1 or by the LFO.
- **A non-resonant high-pass** and **a resonant low-pass** of **12 or 24 dB an octave**.
- **Two ADSR envelopes** with keyboard tracking; ENV-1 can be inverted.
- **One LFO** with four waves and a delay.
- **Two patches, Upper and Lower**, played whole, layered (dual) or split across the keyboard.
- **Four assign modes:** solo, unison, poly 1 and poly 2; hold and portamento.
- **An arpeggiator**, free-running or locked to the song's tempo.
- **A bender and a modulation lever** for the pitch, the filter and vibrato.

## Signal flow

<Flow
  caption="One voice of Juniper Eight. The whole frame is built eight times; in dual and split, four voices play the upper patch and four the lower, each patch with every control of its own."
  voice={5}
  voices="Each of the eight voices"
  wrap={3}
  columns={[
    [{id: 'vcos', label: 'VCO-1 · VCO-2', note: 'sync · cross mod'}],
    [{id: 'mix', label: 'Mix', note: 'VCO-1 ↔ VCO-2'}],
    [{id: 'hpf', label: 'HPF', note: 'non-resonant'}],
    [{id: 'vcf', label: 'VCF', note: '12 or 24 dB low-pass'}],
    [{id: 'vca', label: 'VCA', note: 'by ENV-2'}],
    [{id: 'vol', label: 'Volume'}],
  ]}
  mods={[
    {label: 'LFO', to: ['vcos', 'vcf', 'vca']},
    {label: 'ENV-1', to: ['vcos', 'vcf']},
    {label: 'ENV-2', to: ['vcf', 'vca']},
    {label: 'Key', to: ['vcf']},
  ]}
/>

Each voice starts with two oscillators. VCO-2 can also play the role of a modulator, pushing VCO-1's pitch at audio rate (cross mod) or resetting it (sync). The **Mix** crossfades between the two, the high-pass thins the low end, the low-pass shapes the tone, and the amplifier follows ENV-2. The LFO and ENV-1 can bend the oscillators' pitch (to VCO-1, VCO-2 or both) and their pulse width; the filter takes either envelope, the LFO and the key.

## The face

### In the device chain

In the chain, Juniper Eight shows its whole panel in three rows, like the original: the LFO, the oscillators and their mix; the filters, the amplifier and both envelopes, with the PANEL keys, a lamp for each of the eight voices and the volume; and the keyboard modes, the arpeggiator and the controllers. A compact face, for a long chain, keeps the filter, the two envelopes drawn as curves, the source mix and the arpeggiator.

{{chain}}

### Its window

The window has the whole panel at full size, with both envelopes drawn underneath; drag their corners to shape them. Open it with the window key at the card's left, or with **Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while Juniper Eight has the focus.

{{window}}

**PANEL: UPPER and LOWER** choose which of the two patches the face shows and edits, as on the original. In **Whole** key mode only the upper patch plays. While you play, each voice's lamp lights, red for the upper patch and orange for the lower, and each drawn envelope shows a dot for every voice of the patch you are editing.

## The oscillators

### VCO-1

- **Waveform:** **triangle** (soft, flute-like, few harmonics), **saw** (bright, every harmonic, the brass and string wave), **pulse** (narrowed by the pulse width) or **square** (hollow, odd harmonics only).
- **Range:** 64' to 2', six octaves of footage. 8' is concert pitch.
- **Cross mod** (CROSS MOD) lets VCO-2 modulate VCO-1's frequency at audio rate, up to three octaves at full. This is frequency modulation, as in an FM synth: new partials appear that neither oscillator has, metallic and clangorous at high settings, a growl at low ones. VCO-2's wave matters. Its saw and pulse only push VCO-1 upward, so VCO-1's pitch rises with the amount; its sine swings VCO-1 both ways about its pitch, for bells and gongs that keep their note.

### VCO-2

- **Waveform:** **sine** (pure), **saw**, **pulse**, or **noise** (NSE) for breath, wind and percussion.
- **Range** (coarse) from an octave down to two octaves up in semitones, and **Fine**, a cent at a time. A new Juniper Eight has VCO-2 six cents sharp: the beating between the two oscillators is the start of its richness.
- **Low** takes VCO-2 down to a few hertz, where the keys no longer move it. It is then a second LFO, for cross mod or sync that sweeps slowly.

### Sync

Sync resets one oscillator's wave every time the other starts its cycle. The reset one keeps its own pitch in its harmonics but takes the other's fundamental. Sweep the reset oscillator's pitch and the harmonics move through the sound: the screaming, tearing sync lead.

- **OFF:** the oscillators run free.
- **1→2:** VCO-1 is reset by VCO-2.
- **2→1:** VCO-2 is reset by VCO-1. Then tune VCO-2 up with **Range** and sweep it with ENV-1 (in the **VCO MODULATOR**) for the classic sync sweep.

Every key restarts both oscillators at the same point of their cycle, as on the original, so each note starts with the same punch.

### Modulating the pitch: VCO MODULATOR

**LFO** (up to an octave) and **ENV-1** (up to three octaves) bend the oscillators' pitch. **VCO** chooses where: **1** (VCO-1), **1+2** (both) or **2** (VCO-2). The LFO on both is vibrato; ENV-1 on VCO-2 alone, with sync on 2→1, is the sync sweep; ENV-1 on both, short, is a pitch blip at the start of a note, for drums and zaps.

### Pulse width and mix: VCO-1 & 2

- **PW-PWM** sets the pulse width of both oscillators' pulses, from a square at 0 to a thin, reedy pulse toward 10.
- **BY** chooses who sets it: **MAN** (the knob), **ENV** (ENV-1 narrows it as it rises) or **LFO** (the LFO sweeps it, the knob setting how far). A swept pulse is chorus without a chorus.
- **MIX** crossfades from VCO-1 alone (0) through both (5) to VCO-2 alone (10), keeping the loudness even.

## The filters

### HPF

A gentle high-pass before the low-pass, without resonance, from 5 Hz (nothing taken) to about 2 kHz. Turn it up to take the weight out of a pad or a string sound so it sits above the bass, or to make a thin, nasal lead.

### VCF

A low-pass filter built like the original's: four transconductance stages with a resonance loop round them.

- **Cutoff** runs from about 24 Hz to 6.9 kHz, 535 Hz at 5.
- **Res** (resonance) emphasises the frequencies at the cutoff. On Juniper Eight it rings and whistles but does not quite break into a tone of its own, as on the original: the filter stays musical at the top of its range.
- **Slope** switches between **-24** (24 dB an octave, four poles: deep, round, the classic) and **-12** (12 dB an octave, two poles: brighter and more open, lets more of the oscillators' edge through; good for brass and strings).
- **ENV** is how far an envelope moves the cutoff, and **FROM** chooses which: **ENV-1** or **ENV-2**. With ENV-1 on the filter and ENV-2 on the amplifier, the filter and the loudness can have different shapes.
- **LFO** sweeps the cutoff with the LFO.
- **KYBD** (key follow) opens the filter as you play higher, about an octave an octave at 10.

## The amplifier and envelopes

**VCA LEVEL** sets the voice's level, and **VCA LFO** adds the LFO as tremolo. The amplifier follows **ENV-2**.

Each envelope has **A**ttack, **D**ecay, **S**ustain and **R**elease, plus:

- **KEY** (key follow), which makes the envelope faster the higher you play, as a struck string or a piano dies faster higher up.
- **INV** (ENV-1 only), which turns ENV-1 upside down where it moves the filter: the filter closes as the envelope rises.

The attack rises in a curve that bends over as it nears the top, and the decay and release fall exponentially, quickly and then slowly; the release is a little longer than a decay at the same setting. At its end the envelope closes completely, so nothing lingers under the next note.

The usual split of duties: **ENV-2** is the loudness (often a high sustain), **ENV-1** the filter's movement and the pitch effects.

## The LFO

**RATE** from one cycle in about half a minute to 30 Hz (1.5 Hz at 5). **DELAY** holds it back for up to 7.5 seconds after you strike a key with none of the patch's voices sounding, then fades it in. **WAVEFORM:**

- **SIN** for vibrato and gentle sweeps.
- **SAW**, a falling ramp, for repeating swoops down.
- **SQR**, low then high, for trills and gating.
- **RND**, a new random step every cycle: the bubbling sample-and-hold sound, best on the filter.

The LFO reaches the pitch (VCO MODULATOR), the pulse width, the filter and the amplifier, and the modulation lever brings it in by hand.

## Two patches: the keyboard

Juniper Eight holds two complete patches, **Upper** and **Lower**, each with its own settings of every control from the LFO to the envelopes. **KEY MODE** decides how they are played:

- **WHOLE:** the upper patch on all eight voices.
- **DUAL:** every key plays both patches, four voices each, layered. A brass over a string, a bell over a pad.
- **SPLIT:** the lower patch under the **SPLIT** point, the upper above it, four voices each. A bass in the left hand and a lead in the right.

**BALANCE** sets the level of the upper patch against the lower in dual and split.

**ASSIGN MODE** decides how keys find voices:

- **POLY 1:** each key takes the next free voice in turn, so released notes ring on under new ones. The default.
- **POLY 2:** a key takes the voice that last played it, or the one let go longest ago, cutting its release: tighter for fast parts.
- **SOLO:** one voice, the latest key; let go and it returns to a key still held without a new attack. A monosynth, for leads and basses.
- **UNI** (unison): all of the patch's voices on one note, spread by **DETUNE**. Eight detuned voices of two oscillators each: the biggest lead and bass sound the instrument has.

**HOLD** keeps the notes sounding after you let go. **PORTA** (portamento) glides between notes at a steady rate, switched in by its **ON** key.

## The arpeggiator

**ARPEGGIO ON** plays the held keys one after another: **UP**, **DOWN**, **U&D** (up and down) or **RND** (random), over **RANGE** of one to four octaves. **CLOCK** runs it **FREE**, at **RATE** from very slow to very fast, or locked to the song's **TEMPO**, where the rate knob steps through half notes, quarters, eighths, eighth triplets, sixteenths and thirty-seconds.

In **SPLIT**, the arpeggiator plays the lower half's keys, so the left hand runs a sequence while the right hand plays over it.

## Controllers

- The **bender** (the track's pitch bend) moves the pitch of VCO-1 and VCO-2, each switched on separately, over **BEND VCO**, up to two octaves, and the cutoff by **BEND VCF**.
- The **modulation lever** (your keyboard's mod wheel) adds the LFO to the oscillators by **LFO VCO** (vibrato) and to the filter by **LFO VCF**.
- **DETUNE** spreads the voices in unison.
- **VOLUME**, **master tune** (a semitone either way) and **Quality**: Full runs the oscillators and filters at twice the sample rate, Light at the rate for half the processing.

Juniper Eight does not answer velocity, as the original did not.

## Your first patch: sync lead

From a new Juniper Eight:

1. **One voice.** ASSIGN MODE **SOLO**, PORTA 2 and its ON key lit.
2. **Sync.** VCO-2 sync **2→1**, VCO-2 waveform **SAW**, Range +7. MIX 10, so you hear VCO-2 alone.
3. **The sweep.** VCO MODULATOR: **ENV-1** 6, VCO **2**. ENV-1: A 0, D 5, S 2, R 3. Each note now tears downward through its harmonics.
4. **Open it up.** Cutoff 8, RES 2, ENV 2.
5. **Vibrato on the wheel.** LFO RATE 6, **LFO VCO** 3, then push your mod wheel.

## Starting points

- **Eighties brass.** Both saws, VCO-2 fine +8, Slope -12, Cutoff 3.5, ENV 6 from ENV-1, ENV-1 A 2, D 4, S 4, R 2; ENV-2 A 1, S 10, R 2.
- **Huge unison bass.** ASSIGN MODE UNI, DETUNE 3, VCO-1 range 16', both saws, Cutoff 2.5, RES 3, ENV 6, ENV-1 D 3, S 1.
- **Cross-mod bell.** VCO-2 SIN, Range +19, CROSS MOD 5, MIX 0, Cutoff 8, ENV-2 A 0, D 7, S 0, R 7, ENV-2 KEY on.
- **Strings.** Both saws, VCO-2 fine +10, HPF 3, Slope -12, Cutoff 5, ENV-2 A 4, S 9, R 5. Push the mod wheel a little for vibrato.
- **Sample-and-hold bubbles.** LFO RND, RATE 7, VCF LFO 5, RES 6.
- **Split: bass and pad.** KEY MODE SPLIT at C3; PANEL LOWER: a bass; PANEL UPPER: a pad; BALANCE to taste.
- **Tempo arpeggio.** ARPEGGIO ON, UP, RANGE 2, CLOCK TEMPO, RATE at sixteenths, a short pluck patch.

## Tips

- **Two envelopes, two jobs.** Keep ENV-2 on the amplifier with a high sustain, and give the filter and the pitch their movement with ENV-1.
- **12 dB for brass, 24 dB for basses.** The two-pole slope keeps the edge of the saws; the four-pole one makes them round.
- **The high-pass is for mixing.** Lift HPF on pads and strings until they stop clouding the bass.
- **Dual halves the polyphony.** With two patches layered each has four voices; long releases will steal notes sooner.
- **Unison and portamento** together make the gliding, detuned lead of the era.
