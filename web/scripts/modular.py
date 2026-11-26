"""Exports the Modular for its page: its modules by group, from the app, and
a picture of a factory patch in its window.

  python scripts/modular.py BUILD_DIR [PATCH_NAME] [--data-only] [--modules]

Writes src/data/modules.json (each module's description, knobs and jacks,
which scripts/manual_modules.py makes the manual's pages of) and
src/assets/modular/patch.webp, unless --data-only. The patch is Berlin
School unless another factory patch is named. The words are checked as
scripts/devices.py checks a device's.

With --modules, a picture of each module too, src/assets/modules/<id>.webp:
alone in a rack, its window shot, and the module cut out where the
screenshot's anchors say it is (module:<ID>).
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from devices import App, DATA, SCALE, WEB, check_words  # noqa: E402


PLACE = ("180", "140")  # On the canvas: right of From track, below To track.
EDGE = 4  # Points from the canvas's edge, where a module is cut off.


def module_pictures(app: App, types: list[str]) -> None:
    out = WEB / "src" / "assets" / "modules"
    out.mkdir(parents=True, exist_ok=True)
    missing, cut = [], []
    for type_id in types:
        project = app.work / f"{type_id.removeprefix('builtin.')}.daw"
        app.json("new", str(project), "Module", "--empty")
        rack = app.json("add-device", str(project), "track_1", "builtin.modular")["device"]
        try:
            module = app.json("modular-add", str(project), rack, type_id, *PLACE)["device"]
        except Exception:  # Subpatch Input and Output live only in a subpatch.
            missing.append(type_id)
            continue
        shot, anchors = app.work / "module.bmp", app.work / "anchors.json"
        app.shoot(str(project), "--window", rack, "--screenshot", str(shot), "--screenshot-size", "1600", "950",
                  "--screenshot-scale", str(SCALE), "--screenshot-anchors", str(anchors))
        kept = json.loads(anchors.read_text(encoding="utf-8"))["anchors"]
        name, window = f"module:{module.removeprefix('device_')}", f"device:{rack.removeprefix('device_')}"
        found = next((a for a in kept if a["name"] == name and a["window"] == window), None)
        if not found:
            missing.append(type_id)
            continue
        image = Image.open(shot.with_name(f"{shot.stem}-{rack}.bmp")).convert("RGB")
        x, y, w, h = found["rect"]
        if x + w >= image.width / SCALE - EDGE or y + h >= image.height / SCALE - EDGE:
            cut.append(type_id)  # It runs past the window: cut short.
        image.crop((round(x * SCALE), round(y * SCALE), round((x + w) * SCALE), round((y + h) * SCALE))).save(
            out / f"{type_id.removeprefix('builtin.')}.webp", quality=90, method=6)
        print(f"  {type_id}: {w:.0f} x {h:.0f}", flush=True)
    if missing:
        print("No picture of:", ", ".join(missing))
    if cut:
        print("Cut short by the window:", ", ".join(cut))


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    build = Path(sys.argv[1]).resolve()
    named = [word for word in sys.argv[2:] if not word.startswith("--")]
    patch_name = named[0] if named else "Berlin School"
    with tempfile.TemporaryDirectory() as folder:
        app = App(build, Path(folder))
        listed = app.json("device-types", "--summary")["deviceTypes"]
        modules, hits = [], []
        for item in listed:
            if item.get("group") != "Modular" or not item.get("part") or item["id"] == "builtin.modular-fx":
                continue
            full = app.json("device-types", item["id"])["deviceType"]
            # Its knobs, and its own jacks; each knob's input (param:) is the knob's.
            knobs = [{key: knob[key] for key in ("label", "unit", "minimum", "maximum", "default", "choices") if key in knob}
                     for knob in full.get("parameters", [])]
            jacks = [{key: jack[key] for key in ("label", "direction", "kind")}
                     for jack in full.get("modularPorts", []) if not jack["key"].startswith("param:")]
            record = {"id": item["id"], "label": item["label"], "part": item["part"], "summary": full.get("description"),
                      "knobs": knobs, "jacks": jacks}
            for field in ("label", "summary"):
                check_words(f"{item['id']} {field}", record[field], hits)
            for part in knobs + jacks:
                check_words(f"{item['id']} {part['label']}", " ".join([part["label"], *part.get("choices", [])]), hits)
            modules.append(record)
        if hits:
            sys.exit("Makers' or models' names in the modules' words:\n  " + "\n  ".join(hits))
        presets = app.json("library", "list", "--device", "builtin.modular")
        presets = presets.get("presets", presets)
        (DATA / "modules.json").write_text(json.dumps({"modules": modules, "patches": len(presets)}, indent=1, ensure_ascii=False),
                                           encoding="utf-8")
        print(f"{len(modules)} modules, {len(presets)} factory patches")
        if "--modules" in sys.argv:
            module_pictures(app, [m["id"] for m in modules])
        if "--data-only" in sys.argv:
            return

        chosen = next((p for p in presets if p.get("name") == patch_name), None)
        if not chosen:
            sys.exit(f"No factory patch named {patch_name}")
        project = app.work / "Modular.daw"
        app.json("new", str(project), "Modular", "--empty")
        made = app.json("library", "apply", str(project), chosen["id"], "--track", "track_1")
        device_id = made["devices"][0] if isinstance(made.get("devices"), list) else made.get("device")
        if isinstance(device_id, dict):
            device_id = device_id.get("id")
        shot = app.work / "modular.bmp"
        app.shoot(str(project), "--window", device_id, "--screenshot", str(shot), "--screenshot-size", "1600", "950",
                  "--screenshot-scale", str(SCALE))
        window = Image.open(shot.with_name(f"{shot.stem}-{device_id}.bmp"))
        out = WEB / "src" / "assets" / "modular"
        out.mkdir(parents=True, exist_ok=True)
        window.crop((0, 24 * SCALE, window.width, window.height)).convert("RGB").save(out / "patch.webp", quality=88, method=6)
        print(f"{patch_name} in its window: {out / 'patch.webp'}")


if __name__ == "__main__":
    main()
