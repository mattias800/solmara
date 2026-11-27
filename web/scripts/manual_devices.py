"""Writes the manual's chapter for each device, from what scripts/devices.py
exported and the words written for it: what it is, its pictures in the
chain and in its window, the guide to it, and every control with its range
and where it starts.

  python scripts/manual_devices.py

A chapter is src/content/docs/manual/devices/<family>/<slug>.mdx. Its guide
is written by hand in src/data/manual/<slug>.md: Markdown that may say
{{chain}} and {{window}} where those pictures go (otherwise they come after
its first paragraphs, under headings of their own). A chapter that a person
has taken over (without the generated mark on its first lines) is left alone.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

WEB = Path(__file__).resolve().parent.parent
DATA = WEB / "src" / "data"
DOCS = WEB / "src" / "content" / "docs" / "manual" / "devices"
GUIDES = DATA / "manual"
FACES = WEB / "src" / "assets" / "devices"
MARK_WORDS = "Written by scripts/manual_devices.py"
MARK = "{/* " + MARK_WORDS + " from the app and src/data/manual; edit those, or remove this line to write it by hand. */}"
# The website's families, whose pages a device is shown on.
FAMILIES = {"instrument": "instruments", "effect": "effects", "midi": "midi"}


def folder_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def family(device: dict) -> str:
    """Its chapter's folder under DOCS: its section of the manual's Devices,
    as the app's browser groups it (src/lib/manual-sections.mjs, manualFolder:
    keep the two alike)."""
    if device.get("kind") == "midi":
        return "midi"
    if device["id"] == "builtin.modular":
        return "modular"
    if device.get("group") == "Guitar & bass":
        return folder_of(device.get("part") or "other")
    if device.get("group") == "Synths":
        return folder_of(f"{device.get('part') or 'other'} synths")
    return folder_of(device.get("group") or "other")


def site_family(device: dict) -> str:
    """Its family on the website, whose page it is shown on."""
    if device.get("group") == "Guitar & bass":
        return "guitar"
    return FAMILIES.get(device.get("kind"), "effects")


def up_to_src(device: dict) -> str:
    """From its chapter's folder back to src/, for its imports."""
    return "../" * (len((DOCS / family(device)).relative_to(WEB / "src").parts))


def number(value: float) -> str:
    text = f"{value:.3f}".rstrip("0").rstrip(".")
    return "0" if text == "-0" else text


# Units that are the control's kind rather than what its number counts.
PLAIN = {"dial", "ratio", "steps", "step", "choice", "switch", "raw", "count", "integer", "position", "drawbar", "width",
         "key", "note", "MIDI note", "velocity"}


def with_unit(value: float, unit: str | None) -> str:
    if unit == "linear":
        return number(value)
    if not unit or unit in PLAIN:
        return number(value)
    space = "" if unit in ("%",) else " "
    return f"{number(value)}{space}{unit}"


def control_row(control: dict) -> tuple[str, str, str]:
    choices = control.get("choices")
    default = control.get("default", 0)
    if choices:
        span = ", ".join(choices) if len(choices) <= 8 else f"{len(choices)} choices: {', '.join(choices[:4])}, …"
        index = int(round(default - control.get("minimum", 0)))
        start = choices[index] if 0 <= index < len(choices) else number(default)
        return control["label"], span, start
    unit = control.get("unit")
    if unit == "linear" and control.get("minimum", 0) >= 0 and control.get("maximum", 1) == 1:
        unit, control = "%", {**control, "minimum": control.get("minimum", 0) * 100, "maximum": 100,
                              "default": default * 100}
        default = control["default"]
    span = f"{with_unit(control.get('minimum', 0), unit)} to {with_unit(control.get('maximum', 1), unit)}"
    return control["label"], span, with_unit(default, unit)


def cell(text: str) -> str:
    return mdx(text.replace("|", "\\|").replace("\n", " "))


def mdx(text: str) -> str:
    """The app's words as MDX reads them: its braces and angle brackets as text."""
    return text.replace("{", "&#123;").replace("}", "&#125;").replace("<", "&lt;")


def generated(path: Path) -> bool:
    return any(MARK_WORDS in line for line in path.read_text(encoding="utf-8").splitlines()[:8])


def pictures(device: dict) -> tuple[list[str], dict[str, list[str]]]:
    """The imports, and each picture as the page shows it."""
    slug, label = device["slug"], device["label"]
    up = up_to_src(device) + "assets/devices/"
    imports, shown = [f"import Shot from '{up_to_src(device)}components/Shot.astro';"], {}
    chain = FACES / "chain" / f"{slug}.webp"
    if chain.exists() or (not device["window"] and (FACES / f"{slug}.webp").exists()):
        imports.append(f"import chain from '{up}{'chain/' if chain.exists() else ''}{slug}.webp';")
        shown["chain"] = [f'<a href={{chain.src}} title="The picture at its full size"><Shot src={{chain}} '
                          f'alt="{label} in a track\'s device chain, as it starts." /></a>']
    if device["window"] and (FACES / f"{slug}.webp").exists():
        imports.append(f"import window from '{up}{slug}.webp';")
        shown["window"] = [f'<a href={{window.src}} title="The picture at its full size"><Shot src={{window}} '
                           f'alt="{label}\'s window, as it starts." /></a>']
    return imports, shown


def preset_list(device: dict) -> list[str]:
    """Its factory presets by category, their names only: an appendix."""
    path = DATA / "presets" / f"{device['slug']}.json"
    presets = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    if not presets:
        return []
    count = "one factory preset" if len(presets) == 1 else f"{len(presets)} factory presets"
    lines = ["## Appendix: the factory presets", "",
             f"{device['label']} comes with {count}. Click the device's name to browse them, each with a line on "
             f"what it is, and try one while the song plays. See [presets](/solmara/manual/guides/devices/#presets).", ""]
    categories: dict[str, list[str]] = {}
    for preset in presets:
        categories.setdefault(preset.get("category") or "Other", []).append(mdx(preset["name"]))
    if len(categories) == 1:
        return lines + [", ".join(next(iter(categories.values()))) + ".", ""]
    return lines + [f"- **{mdx(category)}:** {', '.join(names)}." for category, names in categories.items()] + [""]


def guide(device: dict, shown: dict[str, list[str]]) -> list[str]:
    """The guide written for the device, with its pictures placed."""
    path = GUIDES / f"{device['slug']}.md"
    text = path.read_text(encoding="utf-8").strip("\n") if path.exists() else ""
    lines = text.splitlines() if text else []
    headed = {
        "chain": ["## In the device chain", "", f"{device['label']} on a track, as it starts."],
        "window": ["## Its window", "", "The window opens from the key in the device's header, or with "
                   "**Ctrl+Shift+W** (**Cmd+Shift+W** on a Mac) while the device has the focus."],
    }
    loose: list[str] = []
    for name in ("chain", "window"):
        marker = "{{" + name + "}}"
        if name not in shown:
            lines = [line for line in lines if line.strip() != marker]
        elif any(line.strip() == marker for line in lines):
            lines = [x for line in lines for x in (shown[name] if line.strip() == marker else [line])]
        else:
            loose += headed[name] + [""] + shown[name] + [""]
    if loose:  # After the guide's opening paragraphs, before its first heading.
        at = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
        lines = lines[:at] + ([""] if at else []) + loose + lines[at:]
    return lines + ([""] if lines else [])


def write(device: dict, site_hidden: set[str]) -> Path | None:
    folder = DOCS / family(device)
    path, old = folder / f"{device['slug']}.mdx", folder / f"{device['slug']}.md"
    if any(p.exists() and not generated(p) for p in (path, old)):
        return None  # Written by hand.
    if old.exists():
        old.unlink()
    controls = json.loads((DATA / "controls" / f"{device['slug']}.json").read_text(encoding="utf-8"))
    summary = device.get("summary") or ""
    lede = (summary[:1].upper() + summary[1:] + ".") if summary else ""
    lines = [
        "---",
        f"title: {json.dumps(device['label'], ensure_ascii=False)}",
        f"description: {json.dumps(lede or device['label'], ensure_ascii=False)}",
        "---",
        "",
        MARK,
        "",
    ]
    imports, shown = pictures(device)
    written = GUIDES / f"{device['slug']}.md"
    if written.exists() and "<Flow" in written.read_text(encoding="utf-8"):
        imports.append(f"import Flow from '{up_to_src(device)}components/Flow.astro';")
    lines += imports + [""]
    origin = device.get("origin")
    if origin:
        kind = "an analogue" if origin["circuit"] == "analogue" else "a digital"
        lines += [f"**An emulation of {kind} original,** modelled on {origin['modelledOn']}.", ""]
    elif device.get("kind") != "midi":  # The players' origin is not told.
        lines += ["**A design of Solmara's own.**", ""]
    if (GUIDES / f"{device['slug']}.md").exists():
        pass  # Its guide opens with what it is, in a player's words.
    elif device.get("description"):
        lines += [mdx(device["description"]), ""]
    elif lede:
        lines += [mdx(lede), ""]
    if device["id"] not in site_hidden:
        place = {"instruments": f"/solmara/instruments/{device['slug']}/", "guitar": f"/solmara/guitar/#{device['slug']}",
                 "midi": f"/solmara/write/#{device['slug']}"}.get(site_family(device), f"/solmara/effects/#{device['slug']}")
        if device["id"] == "builtin.modular":
            place = "/solmara/modular/"
        lines += [f"[{device['label']} on the website]({place})", ""]
    lines += guide(device, shown)
    lines += preset_list(device)
    if controls:
        lines += [
            "## Appendix: every control",
            "",
            "Each of the device's controls by the name automation and the inspector give it, with the values it "
            "can take and the one it starts at.",
            "",
            "| Control | Range | Starts at |",
            "| --- | --- | --- |",
        ]
        lines += [f"| {cell(a)} | {cell(b)} | {cell(c)} |" for a, b, c in map(control_row, controls)]
    folder.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def check_site_words() -> None:
    """The website's own words about the devices, checked as the app's are."""
    import devices as export
    hits: list[str] = []
    for name, words in json.loads((DATA / "blurbs.json").read_text(encoding="utf-8")).items():
        for field in ("kind", "text"):
            found: list[str] = []
            export.check_words(f"{name} {field}", words.get(field), found)
            # Vintergatan opens Serum's and Vital's presets: interoperability.
            hits += [hit for hit in found if not (name == "Vintergatan" and ("'Serum'" in hit or "'Vital'" in hit))]
    for type_id, origin in json.loads((DATA / "origins.json").read_text(encoding="utf-8"))["emulations"].items():
        export.check_words(f"{type_id} modelledOn", origin["modelledOn"], hits)
    if hits:
        raise SystemExit("Makers' or models' names in the website's words:\n  " + "\n  ".join(hits))


def main() -> None:
    check_site_words()
    devices = json.loads((DATA / "devices.json").read_text(encoding="utf-8"))
    origins = json.loads((DATA / "origins.json").read_text(encoding="utf-8"))["emulations"]
    for device in devices:
        device["origin"] = origins.get(device["id"])
    hidden = set(json.loads((DATA / "site.json").read_text(encoding="utf-8"))["hidden"])
    written = [p for p in (write(d, hidden) for d in devices) if p]
    # A generated chapter for a device that is no longer there, is named
    # anew or has moved to another folder goes; one written by hand stays,
    # to be moved by hand.
    places = {DOCS / family(d) / f"{d['slug']}.mdx" for d in devices}
    for old in [*DOCS.rglob("*.md"), *DOCS.rglob("*.mdx")]:
        if old not in places and generated(old):
            old.unlink()
            print(f"removed {old.relative_to(WEB)}")
    print(f"{len(written)} chapters written, {len(devices) - len(written)} kept as written by hand")


if __name__ == "__main__":
    main()
