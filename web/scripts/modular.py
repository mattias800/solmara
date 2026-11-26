"""Exports the Modular for its page: its modules by group, from the app, and
a picture of a factory patch in its window.

  python scripts/modular.py BUILD_DIR [PATCH_NAME] [--data-only]

Writes src/data/modules.json (each module's description, knobs and jacks,
which scripts/manual_modules.py makes the manual's pages of) and
src/assets/modular/patch.webp, unless --data-only. The patch is Berlin
School unless another factory patch is named. The words are checked as
scripts/devices.py checks a device's.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from devices import App, DATA, SCALE, WEB, check_words  # noqa: E402


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
