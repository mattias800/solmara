"""Exports the Modular for its page: its modules by group, from the app, and
a picture of a factory patch in its window.

  python scripts/modular.py BUILD_DIR [PATCH_NAME]

Writes src/data/modules.json and src/assets/modular/patch.webp. The patch is
Berlin School unless another factory patch is named. The words are checked
as scripts/devices.py checks a device's.
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
    patch_name = sys.argv[2] if len(sys.argv) > 2 else "Berlin School"
    with tempfile.TemporaryDirectory() as folder:
        app = App(build, Path(folder))
        listed = app.json("device-types", "--summary")["deviceTypes"]
        modules, hits = [], []
        for item in listed:
            if item.get("group") != "Modular" or not item.get("part") or item["id"] == "builtin.modular-fx":
                continue
            record = {"id": item["id"], "label": item["label"], "part": item["part"], "summary": item.get("summary")}
            for field in ("label", "summary"):
                check_words(f"{item['id']} {field}", record[field], hits)
            modules.append(record)
        if hits:
            sys.exit("Makers' or models' names in the modules' words:\n  " + "\n  ".join(hits))
        presets = app.json("library", "list", "--device", "builtin.modular")
        presets = presets.get("presets", presets)
        (DATA / "modules.json").write_text(json.dumps({"modules": modules, "patches": len(presets)}, indent=1), encoding="utf-8")
        print(f"{len(modules)} modules, {len(presets)} factory patches")

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
