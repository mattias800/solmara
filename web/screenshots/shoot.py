"""Makes the manual's pictures from Solmara itself, so they can be made again
whenever the editor changes.

  python shoot.py BUILD_DIR

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


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build = Path(sys.argv[1]).resolve()
    cli, app = tool(build, "solmara-cli"), tool(build, "solmara")
    with tempfile.TemporaryDirectory() as folder:
        work = Path(folder)
        env = dict(os.environ, SOLMARA_SETTINGS=str(work / "settings.json"))
        song = work / "Night Drive.daw"
        run = lambda *args: subprocess.run(args, env=env, check=True, capture_output=True)
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


if __name__ == "__main__":
    main()
