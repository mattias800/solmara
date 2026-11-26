"""Makes the manual's pictures from Solmara itself, so they can be made again
whenever the editor changes.

  python shoot.py BUILD_DIR [extra]

With extra, only the session, the mastering suite, the guitar rig and the
Drum Player. The Drum Player needs a build with the AI on (DAW_BUILD_AI),
its model in assets/drums beside the editor or SOLMARA_DRUM_MODEL set.

BUILD_DIR holds solmara and solmara-cli (solmara.exe and solmara-cli.exe on
Windows). The demo song is built from night-drive.json in a folder of its
own, with settings of its own, so nothing of this computer's (a device's
nickname, a theme) shows; the editor draws it, and crops.py cuts the
pictures into src/assets.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "src" / "assets" / "clips"
SCALE = 2  # Pixels to a point: as sharp as a high-DPI screen.


def tool(build: Path, name: str) -> str:
    exe = build / (name + (".exe" if os.name == "nt" else ""))
    if not exe.exists():
        sys.exit(f"{exe} is not there: build Solmara first")
    return str(exe)


# Where the overview's numbers stand, in points: the top bar, the library,
# the arrangement, the devices, the inspector and the help bar.
MARKS = [(398, 28), (212, 112), (1300, 150), (250, 650), (1570, 112), (212, 786)]


def mark_overview(image):
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(image)
    for font_name in ("C:/Windows/Fonts/segoeuib.ttf", "/System/Library/Fonts/Helvetica.ttc", "DejaVuSans-Bold.ttf"):
        try:
            font = ImageFont.truetype(font_name, 13 * SCALE)
            break
        except OSError:
            font = ImageFont.load_default(13 * SCALE)
    for number, (x, y) in enumerate(MARKS, start=1):
        r = 11 * SCALE
        cx, cy = x * SCALE, y * SCALE
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(220, 192, 138), outline=(8, 9, 12), width=2 * SCALE)
        draw.text((cx, cy), str(number), font=font, fill=(8, 9, 12), anchor="mm")
    return image


def main() -> None:
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != "extra"):
        sys.exit(__doc__)
    build = Path(sys.argv[1]).resolve()
    cli, app = tool(build, "solmara-cli"), tool(build, "solmara")
    with tempfile.TemporaryDirectory() as folder:
        work = Path(folder)
        env = dict(os.environ, SOLMARA_SETTINGS=str(work / "settings.json"))
        song = work / "Night Drive.daw"
        run = lambda *args: subprocess.run(args, env=env, check=True, capture_output=True)
        if len(sys.argv) == 3:
            extra_shots(cli, app, work, run)
            return
        run(cli, "new", str(song), "Night Drive", "--empty")
        run(cli, "apply", str(song), str(HERE / "night-drive.json"))
        for panel in ("library", "inspector", "editor"):
            run(cli, "layout", str(song), panel, "off")
        shot = work / "arrangement.bmp"
        run(app, str(song), "--screenshot", str(shot), "--screenshot-size", "1400", "700", "--screenshot-scale", str(SCALE))
        subprocess.run([sys.executable, str(HERE / "crops.py"), str(shot), str(ASSETS), str(SCALE)], check=True)

        # The whole editor, for the website's home: the library open, the
        # Keys track's chain below the arrangement.
        for panel in ("library", "editor"):
            run(cli, "layout", str(song), panel, "on")
        whole = work / "editor.bmp"
        run(app, str(song), "--select", "track_3", "--screenshot", str(whole), "--screenshot-size", "1600", "900",
            "--screenshot-scale", str(SCALE))
        home = HERE.parent / "src" / "assets" / "home"
        home.mkdir(parents=True, exist_ok=True)
        # Without the status line, which shows the project's path.
        picture_of_editor = Image.open(whole).convert("RGB")
        picture_of_editor.crop((0, 0, picture_of_editor.width, picture_of_editor.height - 32 * SCALE)).save(
            home / "editor.webp", quality=88, method=6)
        print("Editor:", home / "editor.webp")

        # The manual's song: drums, bass, chords, a lead and a reverb return,
        # for the chapters' pictures.
        song2 = work / "Manual.daw"
        run(cli, "new", str(song2), "Night Drive", "--empty")
        run(cli, "apply", str(song2), str(HERE / "manual-song.json"))
        for panel in ("library", "inspector", "editor"):
            run(cli, "layout", str(song2), panel, "on")
        manual = HERE.parent / "src" / "assets" / "manual"
        manual.mkdir(parents=True, exist_ok=True)

        def take(name, *flags, crop=None, size=("1600", "950")):
            bmp = work / f"{name}.bmp"
            run(app, str(song2), *flags, "--screenshot", str(bmp), "--screenshot-size", *size, "--screenshot-scale", str(SCALE))
            image = Image.open(bmp).convert("RGB")
            left, top, right, bottom = crop or (0, 0, image.width // SCALE, image.height // SCALE - 32)
            image = image.crop((left * SCALE, top * SCALE, right * SCALE, bottom * SCALE))
            image.save(manual / f"{name}.webp", quality=88, method=6)
            return image

        # Never the status line: it shows the project's path, a user's folder.
        overview = take("overview", "--select", "track_3", crop=(0, 0, 1600, 918))
        mark_overview(overview).save(manual / "overview.webp", quality=88, method=6)
        take("devices", "--select", "track_3", crop=(236, 612, 1340, 918))
        take("mixer", "--view", "mixer")
        take("piano-roll", "--select", "clip_4")
        take("drum-editor", "--select", "clip_1")
        print("Manual's pictures:", manual)

        # Composer: a verse of melody over four chords, played by a sequence,
        # its window open as a clip's is when it plays alone.
        verse = work / "Composer.daw"
        run(cli, "new", str(verse), "Composer", "--empty")
        run(cli, "apply", str(verse), str(HERE / "composer.json"))
        picture = work / "composer.bmp"
        run(app, str(verse), "--play-clip", "clip_1", "--screenshot-playing", "1", "--screenshot", str(picture),
            "--screenshot-size", "1600", "950", "--screenshot-scale", str(SCALE))
        window = next(work.glob("composer-device_*.bmp"))
        out = HERE.parent / "src" / "assets" / "composer"
        out.mkdir(parents=True, exist_ok=True)
        Image.open(window).convert("RGB").save(out / "window.webp", quality=90, method=6)
        print("Composer:", out / "window.webp")
        extra_shots(cli, app, work, run)


def extra_shots(cli: str, app: str, work: Path, run) -> None:
    """The session, the mastering suite, a guitar rig and the Drum Player, for their chapters."""
    import json
    manual = HERE.parent / "src" / "assets" / "manual"
    manual.mkdir(parents=True, exist_ok=True)

    def project(name: str, *batches: str) -> Path:
        song = work / f"{name}.daw"
        run(cli, "new", str(song), "Night Drive", "--empty")
        operations = []
        for batch in batches:
            operations += json.loads((HERE / batch).read_text(encoding="utf-8"))["operations"]
        joined = work / f"{name}.json"
        joined.write_text(json.dumps({"schemaVersion": 1, "label": name, "operations": operations}), encoding="utf-8")
        run(cli, "apply", str(song), str(joined))
        return song

    def shot(song: Path, name: str, *flags, crop=None, size=("1600", "950")) -> Image.Image:
        bmp = work / f"{name}.bmp"
        run(app, str(song), *flags, "--screenshot", str(bmp), "--screenshot-size", *size, "--screenshot-scale", str(SCALE))
        image = Image.open(bmp).convert("RGB")
        # Never the status line: it shows the project's path, a user's folder.
        left, top, right, bottom = crop or (0, 0, image.width // SCALE, image.height // SCALE - 32)
        image = image.crop((left * SCALE, top * SCALE, right * SCALE, bottom * SCALE))
        image.save(manual / f"{name}.webp", quality=88, method=6)
        return image

    # The manual's song in four scenes, the session in place of the arrangement.
    scenes = project("Session", "manual-song.json", "session.json")
    for panel in ("library", "inspector"):
        run(cli, "layout", str(scenes), panel, "off")
    shot(scenes, "session", "--view", "session", crop=(0, 0, 1600, 650))

    # The manual's song with the default mastering chain, its suite open.
    mastered = project("Mastered", "manual-song.json")
    run(cli, "add-mastering", str(mastered))
    bmp = work / "suite.bmp"
    run(app, str(mastered), "--window", "suite", "--screenshot", str(bmp), "--screenshot-size", "1600", "950",
        "--screenshot-scale", str(SCALE))
    window = next(work.glob("suite-device_*.bmp"))
    Image.open(window).convert("RGB").save(manual / "mastering-suite.webp", quality=88, method=6)

    # A guitar's chain: gate, overdrive, amp and cabinet.
    rig = project("Guitar", "guitar.json")
    for panel in ("library", "inspector"):
        run(cli, "layout", str(rig), panel, "off")
    # Wide enough for the whole chain; only the devices pane is kept.
    shot(rig, "guitar-rig", "--select", "track_2", crop=(0, 664, 2350, 918), size=("2400", "950"))

    # The Drum Player's takes for a two-bar clip, written by the bundled model;
    # the screenshot waits for them.
    groove = project("Drums", "drum-takes.json")
    bmp = work / "drums.bmp"
    run(app, str(groove), "--drum-takes", "clip_1:funk beat", "--screenshot", str(bmp), "--screenshot-size", "1600", "950",
        "--screenshot-scale", str(SCALE))
    window = next(work.glob("drums-device_*.bmp"))
    Image.open(window).convert("RGB").save(manual / "drum-player.webp", quality=88, method=6)
    print("The extra pictures:", manual)


if __name__ == "__main__":
    main()
