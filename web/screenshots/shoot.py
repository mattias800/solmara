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

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "src" / "assets" / "clips"


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
        run(app, str(song), "--screenshot", str(shot), "--screenshot-size", "1400", "700")
        subprocess.run([sys.executable, str(HERE / "crops.py"), str(shot), str(ASSETS)], check=True)


if __name__ == "__main__":
    main()
