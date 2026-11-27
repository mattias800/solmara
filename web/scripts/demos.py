"""Renders the instruments' sound demos for their pages, from the app's
factory presets: two presets of different kinds each, each playing a phrase
that suits its kind (a bass line for a bass, chords for a pad, a melody for
a lead), four bars at 120 BPM in A minor, leveled to one loudness.

  python scripts/demos.py BUILD_DIR [--only SLUG,...]

Writes public/audio/demos/<slug>-<n>.mp3 and src/data/demos.json.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from devices import App, DATA, WEB  # noqa: E402

AUDIO = WEB / "public" / "audio" / "demos"
TARGET_LUFS, CEILING_DB = -16.0, -1.0
SKIP = {"builtin.modular", "builtin.drum-rack", "builtin.multisampler", "builtin.simple-sampler", "builtin.granular-sampler",
        "builtin.slice-player", "builtin.basic-synth", "builtin.instrument-rack"}
# The kinds a demo is chosen from, in the order they are wanted.
KINDS = ["Pad", "Brass", "Lead", "Bass", "Keys", "Strings", "Chord", "Pluck", "Sequence", "Organ", "Bell", "Kick"]

PHRASES = {
    "chords": ("chords", "grid 1/4\nnotes  [a3 c4 e4] = = = | [f3 a3 c4] = = = | [c4 e4 g4] = = = | [g3 b3 d4] = = = \n"),
    "comp": ("chords, played", "grid 1/8\nnotes  [a3 c4 e4] = - [a3 c4 e4] - [a3 c4 e4] = - | [f3 a3 c4] = - [f3 a3 c4] - [f3 a3 c4] = - | "
                               "[c4 e4 g4] = - [c4 e4 g4] - [c4 e4 g4] = - | [g3 b3 d4] = - [g3 b3 d4] - [g3 b3 d4] = - \n"),
    "melody": ("a melody", "grid 1/8\nnotes  e5 = = d5 c5 = d5 e5 | c5 = = = a4 = = - | e5 = g5 = e5 = d5 c5 | d5 = = = = = = - \n"),
    "bass": ("a bass line", "grid 1/8\nnotes  a1 a1 a2 a1 - a1 a2 a1 | f1 f1 f2 f1 - f1 f2 f1 | c2 c2 c3 c2 - c2 c3 c2 | g1 g1 g2 g1 - g1 g2 g1 \n"),
    "acid": ("an acid line", "grid 1/16\nnotes  a1 a1 a2 a1 c2 a1 a1 e2 a1 g1 a1 a2 c2 a1 d2 e2 | a1 a1 a2 a1 c2 a1 a1 e2 a1 g1 a1 a2 c2 a1 d2 e2 | "
                             "f1 f1 f2 f1 a1 f1 f1 c2 f1 e1 f1 f2 a1 f1 c2 e2 | g1 g1 g2 g1 b1 g1 g1 d2 g1 f1 g1 g2 b1 g1 d2 e2 \n"),
    "arp": ("an arpeggio", "grid 1/16\nnotes  a3 c4 e4 a4 e4 c4 a3 c4 e4 a4 e4 c4 a3 c4 e4 a4 | f3 a3 c4 f4 c4 a3 f3 a3 c4 f4 c4 a3 f3 a3 c4 f4 | "
                           "c4 e4 g4 c5 g4 e4 c4 e4 g4 c5 g4 e4 c4 e4 g4 c5 | g3 b3 d4 g4 d4 b3 g3 b3 d4 g4 d4 b3 g3 b3 d4 g4 \n"),
    "beat": ("a beat", "grid 1/16\nbars 4\nkick        x-----x---x-x--- \nsnare       ----x-------x--- \nclosed-hat  x-x-x-x-x-x-x-xx \nclap        ------------x--- \n"),
    "kicks": ("four to the floor", "grid 1/16\nbars 4\nkick  x---x---x---x--- \n"),
}
# Monophonic instruments play a bass line and a melody, not chords.
MONO = {"builtin.one-oscillator-monosynth", "builtin.three-oscillator-monosynth", "builtin.two-filter-monosynth",
        "builtin.titan-303", "builtin.arcturus-2600"}
PHRASE_OF = {"Pad": "chords", "Brass": "chords", "Strings": "chords", "Chord": "comp", "Keys": "comp", "Organ": "comp",
             "Lead": "melody", "Bass": "bass", "Pluck": "arp", "Sequence": "arp", "Bell": "arp", "Kick": "kicks"}


def phrase_for(device: dict, category: str | None) -> tuple[str, str]:
    if device["group"] == "Drums" and device["id"] != "builtin.kick":
        return PHRASES["beat"]
    if device["id"] == "builtin.titan-303" and category == "Bass":
        return PHRASES["acid"]
    return PHRASES[PHRASE_OF.get(category or "", "chords")]


def choose(presets: list[dict], mono: bool = False) -> list[dict]:
    """Two presets that play different phrases: one held or played chords
    where it has them, then a melody, a bass line or an arpeggio."""
    def first(kinds: list[str], phrase_not: str | None = None) -> dict | None:
        for kind in kinds:
            for preset in presets:
                if preset.get("category") == kind and PHRASE_OF.get(kind) != phrase_not:
                    return preset
        return None
    one = (first(["Bass"]) if mono else first(["Pad", "Brass", "Strings", "Chord", "Keys", "Organ"])) or first(KINDS)
    if not one:
        return presets[:2]
    two = first(["Lead", "Bass", "Pluck", "Sequence", "Bell", "Pad", "Brass", "Keys", "Chord"], PHRASE_OF.get(one.get("category")))
    two = two or next((preset for preset in presets if preset is not one), None)
    return [preset for preset in (one, two) if preset]


def render(app: App, device: dict, preset: dict | None, out: Path, not_phrase: str | None = None) -> dict:
    project = app.work / f"{out.stem}.daw"
    app.json("new", str(project), "Demo", "--empty")
    title, text = phrase_for(device, preset.get("category") if preset else None)
    if title == not_phrase and title != PHRASES["kicks"][0]:  # A second demo plays something else than the first.
        title, text = PHRASES["melody"]
    operations = [{"op": "add-device", "ref": "d", "track": "track_1", "type": device["id"]},
                  {"op": "add-clip", "ref": "c", "track": "track_1", "startBeat": 0, "lengthBeats": 16, "name": "Demo"},
                  {"op": "write-notes", "clip": "$c", "text": text}]
    batch = app.work / "demo.json"
    batch.write_text(json.dumps({"schemaVersion": 1, "operations": operations}), encoding="utf-8")
    made = app.json("apply", str(project), str(batch))
    if preset:
        app.json("library", "apply", str(project), preset["id"], "--device", made["refs"]["d"])
    loudness = app.json("mix-loudness", str(project))["tracks"][0]
    lufs, peak = loudness.get("integratedLufs"), loudness.get("truePeakDbtp")
    if lufs is None or lufs < -70:
        raise RuntimeError("silent")
    gain = TARGET_LUFS - lufs
    if peak is not None:
        gain = min(gain, CEILING_DB - peak)
    # A track's volume reaches 6 dB; a quieter preset gets the rest from a
    # Utility after it (up to 12 dB more).
    app.json("set-track", str(project), "track_1", "volume", f"{max(-60.0, min(6.0, gain)):.1f}")
    if gain > 6.0:
        more = {"schemaVersion": 1, "operations": [
            {"op": "add-device", "ref": "u", "track": "track_1", "type": "builtin.utility"},
            {"op": "set-param", "parameter": "$u.gainDb", "value": round(min(12.0, gain - 6.0), 1)}]}
        batch.write_text(json.dumps(more), encoding="utf-8")
        app.json("apply", str(project), str(batch))
    AUDIO.mkdir(parents=True, exist_ok=True)
    done = app.json("render", str(project), str(out), "--tail", "1.5")
    print(f"    {out.name}: {lufs:.1f} LUFS before, {gain:+.1f} dB, peak {done.get('peakDb')} dB", flush=True)
    name = preset["name"] if preset else "Its own kit"
    return {"title": f"{name}, {title}", "file": f"audio/demos/{out.name}"}


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    build = Path(args[0]).resolve()
    wanted = set(args[args.index("--only") + 1].split(",")) if "--only" in args else None
    devices = json.loads((DATA / "devices.json").read_text(encoding="utf-8"))
    hidden = set(json.loads((DATA / "site.json").read_text(encoding="utf-8"))["hidden"])
    path = DATA / "demos.json"
    demos = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    with tempfile.TemporaryDirectory() as folder:
        app = App(build, Path(folder))
        for device in devices:
            if device["kind"] != "instrument" or device["id"] in SKIP | hidden or (wanted and device["slug"] not in wanted):
                continue
            listed = app.json("library", "list", "--device", device["id"])
            presets = choose(listed.get("presets", listed), device["id"] in MONO)
            picks = presets or ([None] if device["group"] == "Drums" else [])
            made = []
            for number, preset in enumerate(picks, start=1):
                try:
                    first_title = made[0]["title"].split(", ", 1)[1] if made else None
                    made.append(render(app, device, preset, AUDIO / f"{device['slug']}-{number}.mp3", first_title))
                except Exception as error:  # noqa: BLE001 - a demo that fails is left out, and said
                    print(f"  {device['label']}: {preset['name'] if preset else 'its kit'} failed: {error}", file=sys.stderr)
            if made:
                demos[device["slug"]] = made
                print(f"  {device['label']}: {', '.join(m['title'] for m in made)}", flush=True)
    path.write_text(json.dumps(demos, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"written {path}")


if __name__ == "__main__":
    main()
