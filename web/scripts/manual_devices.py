"""Writes the manual's reference chapter for each device, from what
scripts/devices.py exported: what it is, and every control with its range
and where it starts.

  python scripts/manual_devices.py

A chapter is src/content/docs/manual/devices/<family>/<slug>.md. One that a
person has written (without the generated mark on its first lines) is left
alone, so a chapter can be taken over by hand and keep its words.
"""
from __future__ import annotations

import json
from pathlib import Path

WEB = Path(__file__).resolve().parent.parent
DATA = WEB / "src" / "data"
DOCS = WEB / "src" / "content" / "docs" / "manual" / "devices"
MARK = "<!-- Written by scripts/manual_devices.py from the app; edit the script, or remove this line to write it by hand. -->"
FAMILIES = {"instrument": "instruments", "effect": "effects", "midi": "midi"}


def family(device: dict) -> str:
    if device.get("group") == "Guitar & bass":
        return "guitar"
    return FAMILIES.get(device.get("kind"), "effects")


def number(value: float) -> str:
    text = f"{value:.3f}".rstrip("0").rstrip(".")
    return "0" if text == "-0" else text


def with_unit(value: float, unit: str | None) -> str:
    if not unit or unit in ("dial", "ratio", "steps"):
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
    span = f"{with_unit(control.get('minimum', 0), unit)} to {with_unit(control.get('maximum', 1), unit)}"
    return control["label"], span, with_unit(default, unit)


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def write(device: dict, site_hidden: set[str]) -> Path | None:
    folder = DOCS / family(device)
    path = folder / f"{device['slug']}.md"
    if path.exists() and MARK not in path.read_text(encoding="utf-8").splitlines()[:8]:
        return None  # Written by hand.
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
    if device.get("description"):
        lines += [device["description"], ""]
    elif lede:
        lines += [lede, ""]
    if device["id"] not in site_hidden:
        place = {"instruments": f"/solmara/instruments/{device['slug']}/", "guitar": f"/solmara/guitar/#{device['slug']}",
                 "midi": f"/solmara/write/#{device['slug']}"}.get(family(device), f"/solmara/effects/#{device['slug']}")
        lines += [f"[{device['label']} on the website]({place})", ""]
    if controls:
        lines += [
            "## Controls",
            "",
            "Each of the device's controls, with the values it can take and the one it starts at.",
            "",
            "| Control | Range | Starts at |",
            "| --- | --- | --- |",
        ]
        lines += [f"| {cell(a)} | {cell(b)} | {cell(c)} |" for a, b, c in map(control_row, controls)]
    folder.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main() -> None:
    devices = json.loads((DATA / "devices.json").read_text(encoding="utf-8"))
    hidden = set(json.loads((DATA / "site.json").read_text(encoding="utf-8"))["hidden"])
    written = [p for p in (write(d, hidden) for d in devices) if p]
    print(f"{len(written)} chapters written, {len(devices) - len(written)} kept as written by hand")


if __name__ == "__main__":
    main()
