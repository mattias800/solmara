"""Exports Solmara's devices for the website and the manual: what each is,
its controls, and a fresh picture of its face, all from the app itself, so
the pages cannot fall behind it.

  python scripts/devices.py BUILD_DIR [--only TYPE_ID,...] [--no-faces] [--library DIR]
  python scripts/devices.py --presets LIBRARY_DIR

BUILD_DIR holds solmara and solmara-cli; the factory library is the one in
the source tree it was built from (BUILD_DIR/../../library), or DIR. It writes:

  src/data/devices.json            every device: name, kind, group, summary, ...
  src/data/controls/<slug>.json    each device's controls, for the manual
  src/data/presets/<slug>.json     each device's factory presets: name, category, description
  src/assets/devices/<slug>.webp   each device's face: its window, or its card
  src/assets/devices/chain/<slug>.webp  a device with a window: its card in the chain

The app runs with settings of its own, so nothing of this computer's shows
(a device's nickname names the hardware it is modelled on). Every text taken
from the app is checked against makers' and models' names, which the public
site never carries; a hit stops the export and names it.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

WEB = Path(__file__).resolve().parent.parent
DATA = WEB / "src" / "data"
FACES = WEB / "src" / "assets" / "devices"
# A device with a window: its card in the chain, beside the window in FACES.
CHAINS = FACES / "chain"
# Pictures are taken as on a display of twice the density, every point two
# pixels, and shown at their size in points: sharp, and never enlarged.
SCALE = 2

# Makers and models of the gear and plugins Solmara's devices are modelled
# on or measured against. None of them may appear on the public site.
FORBIDDEN = [
    r"\broland\b(?! schmidt)", r"\bmoog\b", r"\bkorg\b", r"\byamaha\b", r"sequential circuits", r"\bprophet\b", r"\boberheim\b",
    r"\bclavia\b", r"\bnord\b", r"\bhammond\b", r"\bfender\b", r"\brhodes\b", r"\bwurlitzer\b", r"\bhohner\b",
    r"\bclavinet\b", r"\bteletronix\b", r"\bla-2a\b", r"\b1176\b", r"\burei\b", r"universal audio", r"\bneve\b",
    r"\bpultec\b", r"\bfairchild\b", r"tube-tech", r"tube tech", r"\bmesa\b", r"\bboogie\b", r"\bmarshall\b",
    r"\bibanez\b", r"tube screamer", r"electro-harmonix", r"big muff", r"\blexicon\b", r"\beventide\b",
    r"\bstrymon\b", r"\bechoplex\b", r"space echo", r"\bbinson\b", r"\bjuno\b", r"\bjupiter\b", r"\bminimoog\b",
    r"\btb-303\b", r"\btr-[0-9]{3}\b", r"\bdx7\b", r"\bcasio\b", r"\bcz-[0-9]", r"\bcommodore\b", r"\bxfer\b",
    r"\bserum\b", r"\bgullfoss\b", r"\bsoothe\b", r"\bfabfilter\b", r"\bbrainworx\b", r"neural dsp", r"\bfortin\b",
    r"\bgojira\b", r"\bkemper\b", r"line 6", r"\bfractal\b(?! (?:sync|mode))", r"\bleslie\b", r"\bsolina\b", r"\bmellotron\b",
    r"\bbuchla\b", r"\belektron\b", r"\bnovation\b", r"\barturia\b", r"native instruments", r"\bspitfire\b",
    r"\bsoundtoys\b", r"\bvalhalla\b", r"\bmaag\b", r"api 550", r"\bhelios\b", r"\bchandler\b", r"\bmanley\b",
    r"\bavalon\b", r"\bdbx\b", r"\bdrawmer\b", r"empirical labs", r"\bdistressor\b", r"\bthermionic\b",
    r"plugin alliance", r"\bsoftube\b", r"ik multimedia", r"\bamplitube\b", r"orange amp", r"\bdumble\b",
    r"\bbogner\b", r"\bdiezel\b", r"\bengl\b", r"\bpeavey\b", r"\b5150\b", r"\bevh\b", r"\bdunlop\b",
    r"\bfulltone\b", r"\bklon\b", r"\bproco\b", r"\bmxr\b", r"\bdigitech\b", r"tc electronic", r"\bbehringer\b",
    r"\bensoniq\b", r"\bakai\b", r"\blinn\b", r"\bsimmons\b", r"\bcs-80\b", r"\bob-x", r"\bms-20\b", r"\bsh-101\b",
    r"\bjp-80[0-9]0\b", r"\bppg\b", r"\bwaldorf\b", r"dave smith", r"studio electronics", r"\bdoepfer\b",
    r"make noise", r"mutable instruments",
]
# Short names that are also words or abbreviations ("arp" for arpeggiator,
# "waves" of sound, "variable-mu") count only as their makers write them.
EXACT = [r"\bSequential\b(?! [Ss]witch)", r"\bARP\b",r"\bEMS\b", r"\bAPI\b", r"\bSSL\b", r"\bUAD\b", r"\bEMT\b", r"\bWaves\b", r"\bVital\b",
         r"\bVirus\b", r"\bE-mu\b", r"\bE-MU\b", r"\bRAT\b", r"\bBoss\b", r"\bBOSS\b", r"\bVox\b(?! Pad)", r"\bVOX\b"]
# Nor does a device say it was made after another company's software: what
# it is modelled on is the gear, never a plugin or another DAW's device.
FORBIDDEN += [r"\bplug-?ins?\b(?! (?:you|of your own))", r"another DAW"]
FORBIDDEN_RE = re.compile("|".join(FORBIDDEN), re.IGNORECASE)
EXACT_RE = re.compile("|".join(EXACT))
# Names a device may say because it imports their presets: interoperability
# is the one place the public site names another product.
IMPORTS = {
    "builtin.upward-downward-compressor": {"Vital"},
    "builtin.vintergatan": {"Vital", "Serum"},
}


def slug(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", label.lower().replace("&", "and")).strip("-")


def tool(build: Path, name: str) -> str:
    exe = build / (name + (".exe" if os.name == "nt" else ""))
    if not exe.exists():
        sys.exit(f"{exe} is not there: build Solmara first")
    return str(exe)


class App:
    def __init__(self, build: Path, work: Path):
        self.cli, self.app = tool(build, "solmara-cli"), tool(build, "solmara")
        self.env = dict(os.environ, SOLMARA_SETTINGS=str(work / "settings.json"))
        self.work = work

    def json(self, *args: str) -> dict:
        done = subprocess.run([self.cli, *args], env=self.env, check=True, capture_output=True)
        return json.loads(done.stdout)

    def shoot(self, *args: str) -> None:
        subprocess.run([self.app, *args], env=self.env, check=True, capture_output=True, timeout=300)


def check_words(where: str, text: str | None, hits: list[str]) -> None:
    if not text:
        return
    allowed = IMPORTS.get(where.split(" ")[0], set())
    for pattern in (FORBIDDEN_RE, EXACT_RE):
        for found in pattern.finditer(text):
            if found.group(0) not in allowed:
                hits.append(f"{where}: '{found.group(0)}' in \"{text[:120]}\"")
                return


def export_data(app: App, wanted: set[str] | None) -> list[dict]:
    listed = app.json("device-types", "--summary")["deviceTypes"]
    devices, hits = [], []
    for item in listed:
        if item.get("group") == "Modular" and item["id"] != "builtin.modular":
            continue  # The Modular's modules live inside it.
        if wanted and item["id"] not in wanted:
            continue
        full = app.json("device-types", item["id"])["deviceType"]
        record = {
            "id": item["id"],
            "slug": slug(item["label"]),
            "label": item["label"],
            "kind": item.get("kind"),
            "group": item.get("group"),
            "part": item.get("part"),
            "tag": item.get("tag"),
            "summary": item.get("summary"),
            "description": full.get("description"),
            "window": bool(item.get("window")),
            "sidechain": bool(item.get("sidechain")),
            "controls": item.get("parameterCount", 0),
        }
        for field in ("label", "tag", "summary", "description", "part"):
            check_words(f"{item['id']} {field}", record[field], hits)
        controls = [
            {k: p[k] for k in ("key", "label", "unit", "minimum", "maximum", "default", "choices") if k in p}
            for p in full.get("parameters", [])
        ]
        for control in controls:
            check_words(f"{item['id']} control {control['key']}", control.get("label"), hits)
        (DATA / "controls").mkdir(parents=True, exist_ok=True)
        (DATA / "controls" / f"{record['slug']}.json").write_text(json.dumps(controls, indent=1), encoding="utf-8")
        devices.append(record)
    if hits:
        sys.exit("Makers' or models' names in the app's words; say them otherwise first:\n  " + "\n  ".join(hits))
    slugs = [d["slug"] for d in devices]
    if len(set(slugs)) != len(slugs):
        sys.exit("Two devices share a page name: " + ", ".join(sorted({s for s in slugs if slugs.count(s) > 1})))
    return devices


def save_face(image: Image.Image, name: str, folder: Path = FACES) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(folder / f"{name}.webp", quality=88, method=6)


def without_title(image: Image.Image) -> Image.Image:
    """A window's picture from below its title bar: the rows as the bar's
    colour at the window's left edge, down to its edge."""
    rgb = image.convert("RGB")
    bar = rgb.getpixel((4, 2))
    top = 0
    while top < min(80 * SCALE, rgb.height - 1) and sum(abs(a - b) for a, b in zip(rgb.getpixel((4, top)), bar)) <= 9:
        top += 1
    return image.crop((0, top, image.width, image.height))


def chain_card(app: App, project: Path, device: dict, device_id: str, track_id: str) -> Image.Image | None:
    """The device's card in its track's chain, cut out by its anchor
    (solmara --screenshot-anchors)."""
    shot, anchors = app.work / f"{device['slug']}-chain.bmp", app.work / f"{device['slug']}.json"
    app.shoot(str(project), "--select", track_id, "--screenshot", str(shot), "--screenshot-anchors", str(anchors),
              "--screenshot-size", "1600", "950", "--screenshot-scale", str(SCALE))
    found = [a for a in json.loads(anchors.read_text(encoding="utf-8"))["anchors"]
             if a["name"] == device_id.replace("device_", "device:") and a["window"] == "editor"]
    if not found:
        print(f"  {device['label']}: no card on screen", file=sys.stderr)
        return None
    x, y, w, h = (round(v * SCALE) for v in found[0]["rect"])
    return Image.open(shot).crop((x, y, x + w, y + h))


def export_faces(app: App, devices: list[dict]) -> None:
    """Each device on a track of its own in one project. Its face is its
    window's, or for a device without one its card in the chain; a device
    with a window has its card in the chain as well, in chain/, for the
    manual."""
    project = app.work / "Faces.daw"
    app.json("new", str(project), "Faces", "--empty")
    operations = []
    for index, device in enumerate(devices):
        kind = "audio" if device["kind"] == "effect" else "midi"
        operations += [
            {"op": "add-track", "ref": f"t{index}", "name": device["label"], "kind": kind},
            {"op": "add-device", "ref": f"d{index}", "track": f"$t{index}", "type": device["id"]},
        ]
    batch = app.work / "faces.json"
    batch.write_text(json.dumps({"schemaVersion": 1, "operations": operations}), encoding="utf-8")
    done = subprocess.run([app.cli, "apply", str(project), str(batch)], env=app.env, check=True, capture_output=True)
    refs = json.loads(done.stdout)["refs"]
    for index, device in enumerate(devices):
        device_id, track_id = refs[f"d{index}"], refs[f"t{index}"]
        card = chain_card(app, project, device, device_id, track_id)
        if device["window"]:
            shot = app.work / f"{device['slug']}.bmp"
            app.shoot(str(project), "--window", device_id, "--screenshot", str(shot), "--screenshot-size", "1600", "950",
                      "--screenshot-scale", str(SCALE))
            image = Image.open(shot.with_name(f"{shot.stem}-{device_id}.bmp"))
            save_face(without_title(image), device["slug"])
            if card:
                save_face(card, device["slug"], CHAINS)
        elif card:
            save_face(card, device["slug"])
        else:
            continue
        device["face"] = device["slug"]
        print(f"  {device['label']}", flush=True)


def export_presets(library: Path, devices: list[dict]) -> None:
    """The factory presets of each device, from the library's presets of
    that one device alone, their words checked as the app's are."""
    slugs = {d["id"]: d["slug"] for d in devices}
    found: dict[str, list[dict]] = {}
    hits: list[str] = []
    for meta in sorted(library.rglob("preset.json")):
        preset = json.loads(meta.read_text(encoding="utf-8"))
        types = preset.get("devices") or []
        if preset.get("kind") != "device" or len(types) != 1 or types[0] not in slugs:
            continue
        record = {k: preset[k] for k in ("name", "category", "description") if preset.get(k)}
        for field in ("name", "description"):
            check_words(f"{types[0]} preset {preset.get('name')} {field}", record.get(field), hits)
        found.setdefault(types[0], []).append(record)
    if hits:
        sys.exit("Makers' or models' names in the presets' words:\n  " + "\n  ".join(hits))
    folder = DATA / "presets"
    folder.mkdir(parents=True, exist_ok=True)
    for stale in folder.glob("*.json"):
        stale.unlink()
    for type_id, presets in found.items():
        presets.sort(key=lambda p: (p.get("category", "~"), p["name"].lower()))
        (folder / f"{slugs[type_id]}.json").write_text(json.dumps(presets, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"presets for {len(found)} devices, {sum(map(len, found.values()))} in all")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "--presets":
        export_presets(Path(args[1]), json.loads((DATA / "devices.json").read_text(encoding="utf-8")))
        return
    build = Path(args[0]).resolve()
    wanted = set(args[args.index("--only") + 1].split(",")) if "--only" in args else None
    with tempfile.TemporaryDirectory() as folder:
        app = App(build, Path(folder))
        devices = export_data(app, wanted)
        print(f"{len(devices)} devices")
        if "--no-faces" not in args:
            export_faces(app, devices)
    path = DATA / "devices.json"
    if wanted and path.exists():  # A part: merged into what is there.
        kept = {d["id"]: d for d in json.loads(path.read_text(encoding="utf-8"))}
        kept.update({d["id"]: d for d in devices})
        devices = list(kept.values())
    # A face saved under a name no device has now (one renamed) goes.
    slugs = {device["slug"] for device in devices}
    for stale in FACES.glob("*.webp"):
        if stale.stem not in slugs:
            stale.unlink()
            print(f"removed {stale.name}")
    for stale in CHAINS.glob("*.webp"):
        if stale.stem not in {d["slug"] for d in devices if d["window"]}:
            stale.unlink()
            print(f"removed chain/{stale.name}")
    for stale in (DATA / "controls").glob("*.json"):
        if stale.stem not in slugs:
            stale.unlink()
            print(f"removed controls/{stale.name}")
    for device in devices:
        device.setdefault("face", device["slug"] if (FACES / f"{device['slug']}.webp").exists() else None)
    DATA.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(devices, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"written {path}")
    library = Path(args[args.index("--library") + 1]) if "--library" in args else build.parent.parent / "library"
    if library.is_dir():
        export_presets(library, devices)


if __name__ == "__main__":
    main()
