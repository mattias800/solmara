---
title: "Vireo"
description: "Wavetable and virtual analogue synth: hard leads, supersaw-style stacks, pads and basses."
---

<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->

A wavetable and virtual analogue synth of the early 2000s German kind: two Classic oscillators with sub, third oscillator, noise and ring, two multimode filters with an analogue ladder, four envelopes, three LFOs, a six-slot matrix and unison, wave and HyperSaw oscillator modes and its effects. Its state is the original's 512-byte Single, and its own SysEx patches and banks load. Another track's audio is its external input.

[Vireo on the website](/solmara/instruments/vireo/)

## Controls

Each of the device's controls, with the values it can take and the one it starts at.

| Control | Range | Starts at |
| --- | --- | --- |
| Portamento Time | 0 raw to 127 raw | 0 raw |
| Channel Volume | 0 raw to 127 raw | 0 raw |
| Balance | 0 raw to 127 raw | 0 raw |
| Panorama | 0 raw to 127 raw | 64 raw |
| Osc1 Shape (Osc1 HyperSaw/Density, Osc1 Wavetable/WaveTableIndex) | 0 raw to 127 raw | 64 raw |
| Osc1 Pulsewidth (Osc1 HyperSaw/DetuneSpread) | 0 raw to 127 raw | 64 raw |
| Osc1 Wave Select (Osc1 Wavetable/WaveTableSelect) | 100 choices: Sine, Triangle, Wave 3, Wave 4, … | Wave 65 |
| Osc1 Semitone | 16 raw to 112 raw | 64 raw |
| Osc1 Keyfollow | 0 raw to 127 raw | 96 raw |
| Osc2 Shape (Osc2 HyperSaw/Density, Osc2 Wavetable/WaveTableIndex) | 0 raw to 127 raw | 0 raw |
| Osc2 Pulsewidth (Osc2 HyperSaw/DetuneSpread) | 0 raw to 127 raw | 10 raw |
| Osc2 Wave Select (Osc2 Wavetable/WaveTableSelect) | 100 choices: Sine, Triangle, Wave 3, Wave 4, … | Sine |
| Osc2 Semitone | 16 raw to 112 raw | 64 raw |
| Osc2 Detune | 0 raw to 127 raw | 32 raw |
| Osc2 FM Amount (Osc2 HyperSaw/CrossOscSyncFreq, Osc2 Wavetable/FM Amount) | 0 raw to 127 raw | 0 raw |
| Osc2 Sync | 0 raw to 1 raw | 0 raw |
| Osc2 Filt Env Amt (Osc2 HyperSaw/FilterEnv > Pitch, Osc2 Wavetable/FilterEnv > Pitch) | 0 raw to 127 raw | 64 raw |
| FM Filt Env Amt (Osc2 Wavetable/FilterEnv > FM, Osc2 HyperSaw/FilterEnv > SyncFrequency) | 0 raw to 127 raw | 64 raw |
| Osc2 Keyfollow | 0 raw to 127 raw | 96 raw |
| Osc Balance | 0 raw to 127 raw | 0 raw |
| Suboscillator Volume | 0 raw to 127 raw | 0 raw |
| Suboscillator Shape | Square, Triangle | Square |
| Osc Mainvolume | 0 raw to 127 raw | 64 raw |
| Noise Volume | 0 raw to 127 raw | 0 raw |
| Noise Color | 0 raw to 127 raw | 64 raw |
| Cutoff (Vocoder/Carrier Center Frequency) | 0 raw to 127 raw | 127 raw |
| Cutoff2 (Cutoff2 Offset, Vocoder/Modulator Center Frequency, Vocoder/Modulator Frequency Offset, Offset for FilterLink) | 0 raw to 127 raw | 127 raw |
| Filter1 Resonance (Vocoder/Carrier Q Factor) | 0 raw to 127 raw | 0 raw |
| Filter2 Resonance (Vocoder/Modulator Q Factor) | 0 raw to 127 raw | 0 raw |
| Filter1 Env Amt | 0 raw to 127 raw | 0 raw |
| Filter2 Env Amt | 0 raw to 127 raw | 0 raw |
| Filter1 Keyfollow (Carrier Frequency Spread) | 0 raw to 127 raw | 64 raw |
| Filter2 Keyfollow (Vocoder/Modulator Frequency Spread) | 0 raw to 127 raw | 64 raw |
| Filter Balance (Vocoder/Balance) | 0 raw to 127 raw | 0 raw |
| Saturation Curve | 15 choices: Off, Light, Soft, Middle, … | Off |
| Ringmodulator Volume | 0 raw to 127 raw | 0 raw |
| Filter1 Mode | Low Pass, High Pass, Band Pass, Band Stop, Analog 1 Pole, Analog 2 Pole, Analog 3 Pole, Analog 4 Pole | Low Pass |
| Filter2 Mode | Low Pass, High Pass, Band Pass, Band Stop | Low Pass |
| Filter Routing | Serial 4, Serial 6, Parallel 4, Split Mode | Serial 4 |
| Filter Env Attack (Vocoder/Attack, Input Follower/Attack) | 0 raw to 127 raw | 0 raw |
| Filter Env Decay (Vocoder/Release) | 0 raw to 127 raw | 46 raw |
| Filter Env Sustain (Input Follower/Level) | 0 raw to 127 raw | 0 raw |
| Filter Env Sustain Time (Vocoder/Spectral Balance) | 0 raw to 127 raw | 64 raw |
| Filter Env Release (Vocoder/Bands, Input Follower/Release) | 0 raw to 127 raw | 127 raw |
| Amp Env Attack | 0 raw to 127 raw | 0 raw |
| Amp Env Decay | 0 raw to 127 raw | 0 raw |
| Amp Env Sustain | 0 raw to 127 raw | 127 raw |
| Amp Env Sustain Time | 0 raw to 127 raw | 64 raw |
| Amp Env Release | 0 raw to 127 raw | 0 raw |
| Lfo1 Rate | 0 raw to 127 raw | 48 raw |
| Lfo1 Shape | 68 choices: Sine, Triangle, Saw, Square, … | Triangle |
| Lfo1 Env Mode | 0 raw to 1 raw | 0 raw |
| Lfo1 Mode | 0 raw to 1 raw | 0 raw |
| Lfo1 Symmetry | 0 raw to 127 raw | 64 raw |
| Lfo1 Keyfollow | 0 raw to 127 raw | 0 raw |
| Lfo1 Keytrigger | 0 raw to 127 raw | 0 raw |
| Osc1 Lfo1 Amount | 0 raw to 127 raw | 64 raw |
| Osc2 Lfo1 Amount | 0 raw to 127 raw | 64 raw |
| PW Lfo1 Amount | 0 raw to 127 raw | 64 raw |
| Reso Lfo1 Amount | 0 raw to 127 raw | 64 raw |
| FiltGain Lfo1 Amount | 0 raw to 127 raw | 64 raw |
| Lfo2 Rate | 0 raw to 127 raw | 48 raw |
| Lfo2 Shape | 68 choices: Sine, Triangle, Saw, Square, … | Triangle |
| Lfo2 Env Mode | 0 raw to 1 raw | 0 raw |
| Lfo2 Mode | 0 raw to 1 raw | 0 raw |
| Lfo2 Symmetry | 0 raw to 127 raw | 64 raw |
| Lfo2 Keyfollow | 0 raw to 127 raw | 0 raw |
| Lfo2 Keytrigger | 0 raw to 127 raw | 0 raw |
| Shape Lfo2 Amount | 0 raw to 127 raw | 64 raw |
| FM Lfo2 Amount | 0 raw to 127 raw | 64 raw |
| Cutoff1 Lfo2 Amount | 0 raw to 127 raw | 64 raw |
| Cutoff2 Lfo2 Amount | 0 raw to 127 raw | 64 raw |
| Pan Lfo2 Amount | 0 raw to 127 raw | 64 raw |
| Patch Volume | 0 raw to 127 raw | 100 raw |
| Transpose | 0 raw to 127 raw | 64 raw |
| Key Mode | Poly, Mono 1, Mono 2, Mono 3, Mono 4, Hold | Poly |
| Chorus/Type | Off, Classic, Vintage, Hyper Chorus, Air Chorus, Vibrato, Rotary Speaker | Off |
| Chorus/Mix2 | 128 choices: 0, 1, 2, 3, … | 0 |
| Chorus Mix | 0 raw to 127 raw | 0 raw |
| Chorus Rate (Chorus/Speed) | 0 raw to 127 raw | 64 raw |
| Chorus Depth (Chorus/Distance) | 0 raw to 127 raw | 0 raw |
| Chorus Delay (Chorus/Amount, Chorus/Mic Angle) | 0 raw to 127 raw | 64 raw |
| Chorus Feedback (Chorus/LowHigh Bal) | 0 raw to 127 raw | 64 raw |
| Chorus Lfo Shape | Sine, Triangle, Saw, Square, S&H, S&G | Triangle |
| Chorus/X Over | 128 choices: 0, 1, 2, 3, … | 64 |
| Delay Mode | 23 choices: Off, Simple Delay, Ping Pong 2:1, Ping Pong 4:3, … | Off |
| Delay Send | 0 raw to 127 raw | 0 raw |
| Delay Time (Delay/Tape Delay Time) | 0 raw to 127 raw | 64 raw |
| Delay Feedback (Delay/Tape Delay Feedback) | 0 raw to 127 raw | 0 raw |
| Dly Rate / Rev Decay | 0 raw to 127 raw | 16 raw |
| Dly Depth  (Delay/Tape Delay Modulation) | 0 raw to 127 raw | 12 raw |
| Delay Lfo Shape | Sine, Triangle, Saw, Square, S&H, S&G | Triangle |
| Delay Color (Delay/Tape Delay Center Frequency) | 0 raw to 127 raw | 64 raw |
| Arp Pattern Selct | 64 choices: User, 2, 3, 4, … | 2 |
| Arp Octave Range | 01, 02, 03, 04 | 01 |
| Arp Hold Enable | 0 raw to 1 raw | 0 raw |
| Arp Note Length | 0 raw to 127 raw | 64 raw |
| Arp Swing | 0 raw to 127 raw | 0 raw |
| Lfo3 Rate | 0 raw to 127 raw | 92 raw |
| Lfo3 Shape | 68 choices: Sine, Triangle, Saw, Square, … | Triangle |
| Lfo3 Mode | 0 raw to 1 raw | 0 raw |
| Lfo3 Keyfollow | 0 raw to 127 raw | 0 raw |
| Lfo3 Destination | Osc 1 Pitch, Osc 1+2 Pitch, Osc 2 Pitch, Osc 1 Pulse Width, Osc 1+2 Pulse Width, Osc 2 Pulse Width, Sync Phase | Osc 1+2 Pitch |
| Osc Lfo3 Amount | 0 raw to 127 raw | 0 raw |
| Lfo3 Fade-In Time | 0 raw to 127 raw | 0 raw |
| Arp Mode | Off, Up, Down, Up&Down, As Played, Random, Chord, Arp>Matrix | Off |
| Clock Tempo | 0 raw to 127 raw | 57 raw |
| Arp Clock | 18 choices: , 1/128, 1/64, 1/32, … | 1/16 |
| Lfo1 Clock | 22 choices: Off, 1/64, 1/32, 1/16, … | Off |
| Lfo2 Clock | 22 choices: Off, 1/64, 1/32, 1/16, … | Off |
| Delay Clock | 17 choices: Off, 1/64, 1/32, 1/16, … | Off |
| Lfo3 Clock | 22 choices: Off, 1/64, 1/32, 1/16, … | Off |
| Control Smooth Mode | 21 choices: Off, On, Auto, Note, … | On |
| Bender Range Up | 128 choices: -64, -63, -62, -61, … | +2 |
| Bender Range Down | 128 choices: -64, -63, -62, -61, … | -2 |
| Bender Scale | Linear, Exponential | Exponential |
| Filter1 Env Polarity | 0 raw to 1 raw | 1 raw |
| Filter2 Env Polarity | 0 raw to 1 raw | 1 raw |
| Filter2 Cutoff Link (Vocoder Link) | 0 raw to 1 raw | 1 raw |
| Filter Keytrack Base | 128 choices: C-1, C#-1, D-1, D#-1, … | C4 |
| Osc FM Mode (Osc2 Wavetable/FM Mode WaveTable) | Pos Triangle, Triangle, Wave, Noise, In L, In L+R, In R | Pos Triangle |
| Osc Init Phase | 0 raw to 127 raw | 1 raw |
| Punch Intensity | 0 raw to 127 raw | 64 raw |
| Input Follower Mode | Off, In L, In L+R, In R | Off |
| Vocoder Mode | Off, Oscillator, Osc Hold, Noise, In L, In L+R, In R | Off |
| Osc3 Mode | 68 choices: Off, Slave, Saw, Pulse, … | Off |
| Osc3 Volume | 0 raw to 127 raw | 64 raw |
| Osc3 Semitone | 16 raw to 112 raw | 64 raw |
| Osc3 Detune | 0 raw to 127 raw | 32 raw |
| LowEQ Frequency | 0 raw to 127 raw | 5 raw |
| HighEQ Frequency | 0 raw to 127 raw | 0 raw |
| Osc1 Shape Velocity | 0 raw to 127 raw | 64 raw |
| Osc2 Shape Velocity | 0 raw to 127 raw | 64 raw |
| PulseWidth Velocity | 0 raw to 127 raw | 64 raw |
| Fm Amount Velocity | 0 raw to 127 raw | 64 raw |
| Soft Knob1 ShortName (Soft Knob1 ShortName Main) | 88 choices: ~Para, +3rds, +4ths, +5ths, … | ~Para |
| Soft Knob2 ShortName (Soft Knob2 ShortName Main) | 88 choices: ~Para, +3rds, +4ths, +5ths, … | ~Para |
| Soft Knob3 ShortName (Soft Knob3 ShortName Main) | 88 choices: ~Para, +3rds, +4ths, +5ths, … | ~Para |
| Flt1 EnvAmt Velocity | 0 raw to 127 raw | 64 raw |
| Flt2 EnvAmt Velocity | 0 raw to 127 raw | 64 raw |
| Resonance1 Velocity | 0 raw to 127 raw | 64 raw |
| Resonance2 Velocity | 0 raw to 127 raw | 64 raw |
| Second Output Balance | 0 raw to 127 raw | 0 raw |
| Amp Velocity | 0 raw to 127 raw | 64 raw |
| Panorama Velocity | 0 raw to 127 raw | 64 raw |
| Soft Knob-1 Single | 128 choices: Off, Modulation Wheel, Breath, Control 03, … | Off |
| Soft Knob-2 Single | 128 choices: Off, Modulation Wheel, Breath, Control 03, … | Off |
| Assign1 Source | 40 choices: Off, Pitch Bend, Chan Pressure, Mod Wheel, … | Off |
| Assign1 Destination | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign1 Amount | 0 raw to 127 raw | 64 raw |
| Assign2 Source | 40 choices: Off, Pitch Bend, Chan Pressure, Mod Wheel, … | Off |
| Assign2 Destination1 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign2 Amount1 | 0 raw to 127 raw | 64 raw |
| Assign2 Destination2 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign2 Amount2 | 0 raw to 127 raw | 64 raw |
| Assign3 Source | 40 choices: Off, Pitch Bend, Chan Pressure, Mod Wheel, … | Off |
| Assign3 Destination1 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign3 Amount1 | 0 raw to 127 raw | 64 raw |
| Assign3 Destination2 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign3 Amount2 | 0 raw to 127 raw | 64 raw |
| Assign3 Destination3 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign3 Amount3 | 0 raw to 127 raw | 64 raw |
| LFO1 Assign Dest | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| LFO1 Assign Amount | 0 raw to 127 raw | 64 raw |
| LFO2 Assign Dest | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| LFO2 Assign Amount | 0 raw to 127 raw | 64 raw |
| Phaser Mode | 1 Stage, 2 Stages, 3 Stages, 4 Stages, 5 Stages, 6 Stages | 4 Stages |
| Phaser Mix | 0 raw to 127 raw | 0 raw |
| Phaser Rate | 0 raw to 127 raw | 36 raw |
| Phaser Depth | 0 raw to 127 raw | 112 raw |
| Phaser Frequency | 0 raw to 127 raw | 64 raw |
| Phaser Feedback | 0 raw to 127 raw | 64 raw |
| Phaser Spread | 0 raw to 127 raw | 127 raw |
| MidEQ Gain | 0 raw to 127 raw | 64 raw |
| MidEQ Frequency | 0 raw to 127 raw | 84 raw |
| MidEQ Q-Factor | 0 raw to 127 raw | 32 raw |
| LowEQ Gain | 0 raw to 127 raw | 64 raw |
| HighEQ Gain | 0 raw to 127 raw | 64 raw |
| Bass Intensity | 0 raw to 127 raw | 0 raw |
| Bass Tune | 0 raw to 127 raw | 32 raw |
| Input Ringmodulator | 0 raw to 127 raw | 0 raw |
| Distortion Curve | 26 choices: Off, Light, Soft, Medium, … | Off |
| Distortion Intensity | 0 raw to 127 raw | 0 raw |
| Assign 4 Source | 40 choices: Off, Pitch Bend, Chan Pressure, Mod Wheel, … | Off |
| Assign 4 Destination | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 4 Amount | 0 raw to 127 raw | 64 raw |
| Assign 5 Source | 40 choices: Off, Pitch Bend, Chan Pressure, Mod Wheel, … | Off |
| Assign 5 Destination | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 5 Amount | 0 raw to 127 raw | 64 raw |
| Assign 6 Source | 40 choices: Off, Pitch Bend, Chan Pressure, Mod Wheel, … | Off |
| Assign 6 Destination | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 6 Amount | 0 raw to 127 raw | 64 raw |
| Filter Select | Filter 1, Filter 2, Filter 1+2 | Filter 1+2 |
| Category1 | 23 choices: --, Lead, Bass, Pad, … | -- |
| Category2 | 23 choices: --, Lead, Bass, Pad, … | -- |
| Oscillators/Select | 0, 1, 2 | 0 |
| Reverb Mode | Off, Reverb, Feedback 1, Feedback 2 | Reverb |
| Reverb Send | 128 choices: Off, -46.2dB, -40.2dB, -36.6dB, … | Off |
| Reverb Type | Ambience, Small Room, Large Room, Hall | Ambience |
| Reverb Time | 128 choices: 0, 1, 2, 3, … | 64 |
| Reverb Damping | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 7.8 % |
| Reverb Color | 128 choices: -64, -63, -62, -61, … | 0 |
| Reverb Predelay | 93 choices: 0.0, 5.5, 10.1, 16.4, … | 109.2 |
| Reverb Clock | 17 choices: Off, 1/64, 1/32, 1/16, … | Off |
| Reverb Feedback | 128 choices: 0, 1, 2, 3, … | 64 |
| Delay Type | Classic, Tape Clocked, Tape Free, Tape Doppler | Tape Clocked |
| Delay Tape Delay Ratio | 1/4, 2/4, 3/4, 4/4, 4/3, 4/2, 4/1 | 4/4 |
| Delay Tape Delay Left Clock | 1/32, 1/16, 2/16, 3/16, 4/16, 5/16 | 4/16 |
| Delay Tape Delay Right Clock | 1/32, 1/16, 2/16, 3/16, 4/16, 5/16 | 2/16 |
| Delay Tape Delay Bandwidth | 128 choices: 0, 1, 2, 3, … | 1 |
| Filter Bank/Type | 12 choices: Off, Ring Modulator, Frequency Shifter, Vowel Filter, … | Off |
| Filter Bank/Mix | 128 choices: Off, 0.8 %, 1.6 %, 2.3 %, … | Off |
| Filter Bank/Comb Frequency (Filter Bank/Filter Frequency, Filter Bank/Frequency, Filter Bank/Vowel Frequency) | 128 choices: C0, C#0, D0, D#0, … | C4 |
| Filter Bank/Stereo Phase | 128 choices: -180^, -177^, -174^, -172^, … | +0^ |
| Filter Bank/Filter Type (Filter Bank/Poles, Filter Bank/Shape L) | 128 choices: Low Pass, 1, 2, 3, … | Low Pass |
| Filter Bank/Shape R (Filter Bank/Slope) | 128 choices: -100.0 %, -98.4 %, -96.9 %, -95.3 %, … | +100.0 % |
| Filter Bank/Resonance | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 50.0 % |
| Character Type | 9 choices: Analog Boost, Vintage 1, Vintage 2, Vintage 3, … | Analog Boost |
| Soft Knobs/Destination 3 | 128 choices: Off, Modulation Wheel, Breath, Control 03, … | Off |
| Osc1 Mode | Classic, HyperSaw, Wavetable, Wave PWM, Grain Simple, Grain Complex, Formant Simple, Formant Complex | Classic |
| Osc2 Mode | Classic, HyperSaw, Wavetable, Wave PWM, Grain Simple, Grain Complex, Formant Simple, Formant Complex | Classic |
| Osc1 Wavetable/Sync | 128 choices: 0, 1, 2, 3, … | 0 |
| Osc1 Wavetable/FormantShift | 128 choices: -64, -63, -62, -61, … | 0 |
| Osc1 Wavetable/Internal Detune | 128 choices: 0, 1, 2, 3, … | 0 |
| Osc1 Wavetable/Interpolation | 128 choices: 0, 1, 2, 3, … | 0 |
| Osc2 Wavetable/Sync | 128 choices: 0, 1, 2, 3, … | 0 |
| Osc2 Wavetable/FormantShift | 128 choices: -64, -63, -62, -61, … | 0 |
| Osc2 Wavetable/Internal Detune | 128 choices: 0, 1, 2, 3, … | 0 |
| Osc2 Wavetable/Interpolation | 128 choices: 0, 1, 2, 3, … | 0 |
| Patch Distortion/Treble Booster | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 0 % |
| Patch Distortion/High Cut | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 100.0 % |
| Patch Distortion/Mix | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 100.0 % |
| Patch Distortion/Quality | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 100.0 % |
| Patch Distortion/Tone127 (Patch Distortion/Tone64) | 128 choices: -100.0 %, -98.4 %, -96.9 %, -95.3 %, … | +0 % |
| Envelope 3/Attack | 128 choices: 0, 1, 2, 3, … | 20 |
| Envelope 3/Decay | 128 choices: 0, 1, 2, 3, … | 70 |
| Envelope 3/Sustain | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 0 % |
| Envelope 3/Sustain Time | 0 raw to 127 raw | 0 raw |
| Envelope 3/Release | 128 choices: 0, 1, 2, 3, … | 70 |
| Envelope 4/Attack | 128 choices: 0, 1, 2, 3, … | 20 |
| Envelope 4/Decay | 128 choices: 0, 1, 2, 3, … | 70 |
| Envelope 4/Sustain | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 0 % |
| Envelope 4/Sustain Time | 0 raw to 127 raw | 0 raw |
| Envelope 4/Release | 128 choices: 0, 1, 2, 3, … | 70 |
| Assign 1 Destination 2 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 1 Amount 2 | 128 choices: -64, -63, -62, -61, … | Off |
| Assign 1 Destination 3 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 1 Amount 3 | 128 choices: -64, -63, -62, -61, … | Off |
| Assign 2 Destination 3 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 2 Amount 3 | 128 choices: -64, -63, -62, -61, … | Off |
| Assign 4 Destination 2 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 4 Amount 2 | 128 choices: -64, -63, -62, -61, … | Off |
| Assign 4 Destination 3 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 4 Amount 3 | 128 choices: -64, -63, -62, -61, … | Off |
| Assign 5 Destination 2 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 5 Amount 2 | 128 choices: -64, -63, -62, -61, … | Off |
| Assign 5 Destination 3 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 5 Amount 3 | 128 choices: -64, -63, -62, -61, … | Off |
| Assign 6 Destination 2 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 6 Amount 2 | 128 choices: -64, -63, -62, -61, … | Off |
| Assign 6 Destination 3 | 128 choices: Off, Patch Volume, Osc 1 Interpolation, Panorama, … | Off |
| Assign 6 Amount 3 | 128 choices: -64, -63, -62, -61, … | Off |
| LFO 1/BackupShape | 68 choices: Sine, Triangle, Saw, Square, … | Sine |
| LFO 2/BackupShape | 68 choices: Sine, Triangle, Saw, Square, … | Sine |
| LFO 3/BackupShape | 68 choices: Sine, Triangle, Saw, Square, … | Sine |
| Assigns/Slot Select | 18 choices: 0, 1, 2, 3, … | 0 |
| LFOs/Select | 17 choices: 0, 1, 2, 3, … | 0 |
| FX Upper/Select | 17 choices: 0, 1, 2, 3, … | 0 |
| FX Lower/Select | 17 choices: 0, 1, 2, 3, … | 0 |
| Oscillators/BackupKeyMode | Mono 1, Mono 2, Mono 3, Mono 4 | Mono 1 |
| Arpeggiator/BackupMode | 1, 2, 3, 4, 5, 6, 7 | 1 |
| Osc 3/BackupMode | 66 choices: Slave, Saw, Pulse, Sine, … | Slave |
| Arpeggiator/UserPatternLength | 32 choices: 01, 02, 03, 04, … | 32 |
| Step 1 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 1 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 1 Bitfield | 0, 1 | 1 |
| Step 2 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 2 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 2 Bitfield | 0, 1 | 1 |
| Step 3 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 3 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 3 Bitfield | 0, 1 | 1 |
| Step 4 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 4 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 4 Bitfield | 0, 1 | 1 |
| Step 5 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 5 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 5 Bitfield | 0, 1 | 1 |
| Step 6 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 6 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 6 Bitfield | 0, 1 | 1 |
| Step 7 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 7 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 7 Bitfield | 0, 1 | 1 |
| Step 8 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 8 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 8 Bitfield | 0, 1 | 1 |
| Step 9 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 9 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 9 Bitfield | 0, 1 | 1 |
| Step 10 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 10 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 10 Bitfield | 0, 1 | 1 |
| Step 11 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 11 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 11 Bitfield | 0, 1 | 1 |
| Step 12 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 12 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 12 Bitfield | 0, 1 | 1 |
| Step 13 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 13 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 13 Bitfield | 0, 1 | 1 |
| Step 14 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 14 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 14 Bitfield | 0, 1 | 1 |
| Step 15 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 15 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 15 Bitfield | 0, 1 | 1 |
| Step 16 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 16 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 16 Bitfield | 0, 1 | 1 |
| Step 17 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 17 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 17 Bitfield | 0, 1 | 1 |
| Step 18 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 18 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 18 Bitfield | 0, 1 | 1 |
| Step 19 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 19 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 19 Bitfield | 0, 1 | 1 |
| Step 20 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 20 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 20 Bitfield | 0, 1 | 1 |
| Step 21 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 21 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 21 Bitfield | 0, 1 | 1 |
| Step 22 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 22 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 22 Bitfield | 0, 1 | 1 |
| Step 23 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 23 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 23 Bitfield | 0, 1 | 1 |
| Step 24 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 24 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 24 Bitfield | 0, 1 | 1 |
| Step 25 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 25 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 25 Bitfield | 0, 1 | 1 |
| Step 26 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 26 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 26 Bitfield | 0, 1 | 1 |
| Step 27 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 27 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 27 Bitfield | 0, 1 | 1 |
| Step 28 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 28 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 28 Bitfield | 0, 1 | 1 |
| Step 29 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 29 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 29 Bitfield | 0, 1 | 1 |
| Step 30 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 30 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 30 Bitfield | 0, 1 | 1 |
| Step 31 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 31 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 31 Bitfield | 0, 1 | 1 |
| Step 32 Length | 128 choices: 0, 1, 2, 3, … | 64 |
| Step 32 Velocity | 128 choices: 0, 1, 2, 3, … | 100 |
| Step 32 Bitfield | 0, 1 | 1 |
| Unison Mode | Off, Twin, 3, 4, 5, 6, 7, 8 | Off |
| Unison Detune | 128 choices: 0, 1, 2, 3, … | 48 |
| Unison Pan Spread | 128 choices: 0 %, 0.8 %, 1.6 %, 2.3 %, … | 100.0 % |
| Unison Lfo Phase | 128 choices: -64, -63, -62, -61, … | 0 |
| Input Mode | Off, Dynamic, Static | Off |
| Input Select | Left, L + R, Right | L + R |
| Atomizer | 17 choices: Off, On, 2, 3, … | Off |
