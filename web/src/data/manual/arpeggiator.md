The Arpeggiator plays the notes you hold one after another, in time with the song. Hold a chord and it becomes a rising line, a falling one, a shuffle, or a rhythm you drew yourself. It is a MIDI device: put it in an instrument track's chain before the instrument, and it plays the keys you hold and the notes of the track's clips alike.

The same arpeggiator is built into Vintergatan, as its Arp page.

## In the device chain

The card in the chain has every setting. Its picture draws the notes the chosen shape plays over a chord of three, as they fall; while the song plays, it follows the steps as they sound.

{{chain}}

## Its window

The window has the shapes as cards you can click, every setting, and the pattern editor, where you draw your own patterns. Open it with the window key at the card's left, or with **Edit pattern…** on the card.

{{window}}

## How it plays

A chord begins when you strike a key with none held. Its first step falls on the next beat of the **Rate**'s grid, so a chord struck a little early or late still starts in time. While you hold it, adding or lifting keys changes the notes it plays without starting over.

The notes are taken from the lowest held key up. **Range** plays them over more than one pass, each pass moved by **Shift**: with Range 2 and Shift +12, a chord of three is played, then played again an octave up.

## The shapes

**Shape** chooses the order the notes come in. Each card in the window draws its shape.

| Shape | What it plays |
| --- | --- |
| **Up** | Lowest to highest, then over again. |
| **Down** | Highest to lowest. |
| **Up/Down** | Up and back down, the top and bottom notes once each. |
| **Down/Up** | Down and back up, the ends once each. |
| **Up&Down** | Up and back down, the top and bottom notes twice. |
| **Down&Up** | Down and back up, the ends twice. |
| **Played** | In the order you struck the keys. |
| **Chord** | Every held note at once, on every step. |
| **Converge** | Lowest, highest, next lowest, next highest, toward the middle. |
| **Diverge** | From the middle out. |
| **Conv+Div** | In from the outside and out again. |
| **Random** | Any held note on each step. |
| **Rnd shuffle** | Every note once a round, in a new order each round. |
| **Rnd drift** | A step up or down from where it was, wandering. |
| **Rnd once** | One shuffled order, kept every round: a fixed random riff. |
| **Pattern** | The pattern you drew, in the slot **Pattern slot** chooses. |

The random shapes follow **Seed**: the same seed plays the same notes every time the song plays, so a random line you like stays. Change the seed for another.

## The settings

- **Rate** is the length of a step: whole notes to 1/32, triplets (T) and dotted (.).
- **Gate** is how long each note sounds, as a share of its step. Under 100% is staccato; over 100% the notes overlap, which a legato instrument plays as a slide.
- **Range** is the number of passes over the held notes, 1 to 8.
- **Shift** is how far each pass moves, in semitones: +12 is an octave up each pass, -12 an octave down, +7 a fifth.
- **Swing** holds every second step back, by up to half a step.
- **Seed** picks the random shapes' notes; see above.
- **Latch** keeps a chord playing after you let go of its keys, until you strike another.
- **Restart** says when the steps start over: **After silence** (a chord struck with no keys held starts from its first step), **Each note** (every key struck starts it again), or **Never** (the steps keep to the song's bars from its start, so a pattern always lines up with the bar).
- **Scale** and **Root** are the scale that scale steps walk, in a drawn pattern: the project's own key, or one chosen here.
- **Pattern slot** chooses which of twelve drawn patterns the **Pattern** shape plays. Automate it to change patterns as the song goes.

## Drawing a pattern

With the **Pattern** shape chosen, the editor under the cards holds the pattern in the chosen slot. Its rows are not pitches but roles:

- **Chord** plays every held note at once.
- **1, 2, 3…** play the held notes from the lowest. A row past the highest held note plays the notes again, an octave up.
- **Root**, **Third**, **Fifth** and **Octave** play under the chord: the lowest held note an octave down, and its third, fifth and octave above that.

So one pattern plays any chord you hold.

- **Click** in a row to add a step; drag its end to make it longer.
- **Drag** a step to move it, **Alt-drag** to copy it, **Shift-click** to select more than one, and **double-click** or **Delete** to delete.
- **The velocity lane** under the rows: draw on it to set each step's velocity.
- **The glide lane**: click a step's switch to hold it on into the next, which an instrument playing legato slides.
- **Right-click a step** for its octave, its strum (for a Chord step), a chance it plays, a ratchet (repeats within the step), which cycles it plays on, and **Scale steps**, which walk the scale up or down from the held note.

Any shape can be the start of a pattern: choose it, then **Draw on it as a pattern** copies its steps into the slot, to change as you like.

## Starting points

- **A classic synth arpeggio.** Up, 1/16, Gate 50%, Range 2, Shift +12.
- **Trance gate on a pad.** Chord, 1/16, Gate 40%: the whole chord chopped in time.
- **An evolving line.** Rnd drift, 1/8, Range 3, with Latch on: hold a chord once and let it wander.
- **A bass riff from a chord.** Pattern, with steps on Root and Octave and a few on Fifth, Restart Never.

## Tips

- A step plays with the velocity drawn for it in a pattern; the shapes play each note at the velocity you struck it.
- MIDI devices play one into the next: put a [Note Chance](../note-chance/) after it to leave out some of its notes, or a [Note Repeater](../note-repeater/) to echo them.
- To record the arpeggio's notes rather than the keys you held, turn on the track's **Direct Record** in the track inspector before you record.
