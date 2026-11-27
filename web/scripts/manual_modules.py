"""Writes the manual's reference for the Modular's modules, a page for each
group, from what scripts/modular.py exported: what each module does, its
jacks, and every knob with its range and where it starts.

  python scripts/manual_modules.py

The pages are src/content/docs/manual/devices/modules/<group>.mdx, each
module with its picture from src/assets/modules (modular.py --modules) where
there is one, and an overview, index.md. The words are the app's own, so a
module is described again by changing its description in the app and
exporting anew.
"""
from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path

from manual_devices import cell, control_row

WEB = Path(__file__).resolve().parent.parent
DATA = WEB / "src" / "data"
DOCS = WEB / "src" / "content" / "docs" / "manual" / "devices" / "modules"
WRITTEN = "Written by scripts/manual_modules.py from the app; edit the app's words or the script, not this page."
MARK = f"<!-- {WRITTEN} -->"  # In Markdown; in MDX, a comment of its own.
PICTURES = WEB / "src" / "assets" / "modules"
GUIDE = "/solmara/manual/guides/modular/"

# The groups in the order of the Modular's library, each with a line of its own.
GROUPS = OrderedDict([
    ("Sources", "What makes a sound: oscillators, samples, grains and noise."),
    ("Filters and amps", "What shapes a sound's color and loudness: filters, resonators and amplifiers."),
    ("Shapers", "What bends a wave into another: folding, saturation, multiplying and rectifying."),
    ("Modulation", "What moves things: envelopes, LFOs, random voltages and followers."),
    ("Sequencing", "What keeps time and plays in it: clocks, dividers, sequencers and the song's place."),
    ("Effects", "Delays, choruses, phasers and pitch and frequency shifters, inside the patch."),
    ("Logic and math", "Gates combined and compared, signals added and multiplied, counted and latched."),
    ("Mixing and routing", "Signals mixed, panned, faded, switched, split and sent."),
    ("Utilities", "Voltages set and scaled, pitches quantized and moved, and the notes as signals."),
    ("Displays", "What a signal is doing, shown as it plays, and notes on the patch."),
    ("Subpatches", "Modules of your own, made of other modules."),
])
KINDS = {"audio": "audio", "cv": "control", "gate": "gate", "clock": "clock", "pitch": "pitch"}
UNITS = {"st": "semitones", "oct": "octaves", "/s": "per second"}
ONE = re.compile(r"(?<![\d.])(-?1) (bar|semitone|octave|step)s\b")


def singular(text: str) -> str:
    """1 bar, not 1 bars."""
    return ONE.sub(r"\1 \2", text)


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def knob_rows(knobs: list[dict]) -> list[tuple[str, str, str]]:
    """Each knob a row; knobs alike but for their numbers (Step 1 to Step 16) one row."""
    rows: OrderedDict[tuple[str, str], list[tuple[list[int], str, str]]] = OrderedDict()
    for knob in knobs:
        label, span, start = control_row(dict(knob, unit=UNITS.get(knob.get("unit"), knob.get("unit"))))
        if knob.get("choices"):
            span = ", ".join(knob["choices"])  # All of them, as a reference should.
        span, start = singular(span), singular(start)
        numbers = [int(n) for n in re.findall(r"\d+", label)]
        # A placeholder no label has, for where the numbers stood.
        pattern = re.sub(r"\d+", "\0", label) if numbers else label
        rows.setdefault((pattern, span), []).append((numbers, start, label))
    out = []
    for (pattern, span), members in rows.items():
        if len(members) < 3 or not members[0][0]:
            out += [(label, span, start) for _, start, label in members]
            continue
        # Each number in the label as its lowest to its highest.
        ranges = [(min(m[0][i] for m in members), max(m[0][i] for m in members)) for i in range(len(members[0][0]))]
        spans = iter(f"{low}–{high}" if low != high else str(low) for low, high in ranges)
        label = re.sub("\0", lambda _: next(spans), pattern)
        starts = [start for _, start, _ in members]
        start = starts[0] if len(set(starts)) == 1 else ", ".join(starts) if len(starts) <= 8 else "Different for each"
        out.append((label, span, start))
    return out


def jacks(module: dict, direction: str) -> str:
    found = [j for j in module["jacks"] if j["direction"] == direction]
    return ", ".join(f"{j['label']} ({KINDS.get(j['kind'], j['kind'])})" for j in found) or "None"


def mdx(text: str) -> str:
    """The app's words, safe in MDX, where braces and angle brackets are code."""
    return text.replace("{", "&#123;").replace("}", "&#125;").replace("<", "&lt;")


def picture_name(module: dict) -> str:
    return module["id"].removeprefix("builtin.")


def variable(module: dict) -> str:
    return "m_" + re.sub(r"[^a-z0-9]", "_", picture_name(module))


def section(module: dict) -> list[str]:
    lines = [f"## {mdx(module['label'])}", ""]
    if (PICTURES / f"{picture_name(module)}.webp").exists():
        alt = f"The {module['label']} module on the Modular's canvas, as it starts."
        lines += [f"<Shot src={{{variable(module)}}} alt={json.dumps(alt)} />", ""]
    if module.get("summary"):
        lines += [mdx(module["summary"]), ""]
    if module["jacks"]:
        lines += [f"- **In:** {mdx(jacks(module, 'input'))}", f"- **Out:** {mdx(jacks(module, 'output'))}", ""]
    else:
        lines += ["No jacks.", ""]
    if module["knobs"]:
        lines += ["| Knob | Range | Starts at |", "| --- | --- | --- |"]
        lines += [f"| {mdx(cell(a))} | {mdx(cell(b))} | {mdx(cell(c))} |" for a, b, c in knob_rows(module["knobs"])]
        lines.append("")
    return lines


def front(title: str, description: str, label: str, order: int, comment: str = MARK) -> list[str]:
    return ["---", f"title: {json.dumps(title)}", f"description: {json.dumps(description)}",
            "sidebar:", f"  label: {json.dumps(label)}", f"  order: {order}", "---", "", comment, ""]


def imports(members: list[dict]) -> list[str]:
    lines = ["import Shot from '../../../../../components/Shot.astro';"]
    for module in members:
        if (PICTURES / f"{picture_name(module)}.webp").exists():
            lines.append(f"import {variable(module)} from '../../../../../assets/modules/{picture_name(module)}.webp';")
    return lines + [""]


def main() -> None:
    exported = json.loads((DATA / "modules.json").read_text(encoding="utf-8"))
    modules = exported["modules"]
    unknown = {m["part"] for m in modules} - set(GROUPS)
    if unknown:
        raise SystemExit(f"Groups the script does not know: {', '.join(sorted(unknown))}")
    DOCS.mkdir(parents=True, exist_ok=True)
    for old in [*DOCS.glob("*.md"), *DOCS.glob("*.mdx")]:
        if WRITTEN in old.read_text(encoding="utf-8"):
            old.unlink()
    overview = front("Modular modules", f"The Modular's {len(modules)} modules, group by group: what each does, its jacks and its knobs.",
                     "Overview", 0)
    overview += [
        f"The [Modular]({GUIDE}) has {len(modules)} modules in {len(GROUPS)} groups. Each group has a page: what each module "
        "does, its jacks, and its knobs with their ranges and where they start.",
        "",
        "## Jacks",
        "",
        "Inputs are on the left of a module and outputs on the right. A jack carries a voltage, and its kind says what "
        "the voltage means:",
        "",
        "- **audio:** a sound, ten volts from peak to peak at full scale.",
        "- **control:** a voltage that moves something, slowly or as fast as audio.",
        "- **gate:** on at 10 V or off at 0 V; a short gate is a trigger.",
        "- **clock:** pulses that keep time.",
        "- **pitch:** one volt an octave, with 0 V at middle C.",
        "",
        "The kinds are a guide, not a rule: any output can go into any input.",
        "",
        "Every knob also has an input of its own. A cable into it moves the knob from where it is set, so a patch is "
        "still played with its knobs. The group pages list only a module's own jacks.",
        "",
        "## The groups",
        "",
    ]
    for order, (part, line) in enumerate(GROUPS.items(), start=1):
        members = [m for m in modules if m["part"] == part]
        if not members:
            continue
        page = slug(part)
        overview.append(f"- **[{part}](./{page}/)**: " + ", ".join(m["label"] for m in members) + ".")
        lines = front(f"Modules: {part}", line, part, order, "{/* " + WRITTEN + " */}") + imports(members)
        lines += [line, "", f"Every knob also has an input of its own; see [jacks](../#jacks) for what each kind carries.", ""]
        for module in members:
            lines += section(module)
        (DOCS / f"{page}.mdx").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (DOCS / "index.md").write_text("\n".join(overview).rstrip() + "\n", encoding="utf-8")
    print(f"{len(modules)} modules on {len(GROUPS)} pages in {DOCS.relative_to(WEB)}")


if __name__ == "__main__":
    main()
