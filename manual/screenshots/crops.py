"""Crops the manual's pictures out of the demo song's screenshot, as
shoot.py takes it (1400 by 700, the side panels hidden).

  python crops.py SHOT OUT_DIR
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

shot = Image.open(sys.argv[1]).convert("RGB")
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)

# The arrangement's first four bars, at its own size: the tracks and the keys' automation lane, without the
# window's bar or the status line (which shows the project's path).
shot.crop((0, 95, 700, 428)).save(out / "arrangement.webp", quality=92)

# The automation lane alone, its head and both clips.
shot.crop((0, 316, 930, 428)).save(out / "automation-lane.webp", quality=92)

# A clip's right edge, three times as large, with its two halves named.
scale = 3
edge = shot.crop((600, 192, 712, 252))
edge = edge.resize((edge.width * scale, edge.height * scale), Image.LANCZOS)
pad_right = 430
canvas = Image.new("RGB", (edge.width + pad_right, edge.height + 40), (17, 18, 25))
canvas.paste(edge, (0, 20))
draw = ImageDraw.Draw(canvas)
def face(size):
    # A clean sans the system has: Windows', macOS's, or most Linuxes'.
    for name in ("C:/Windows/Fonts/segoeui.ttf", "/System/Library/Fonts/Helvetica.ttc",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default(size)


font, small = face(26), face(20)
edge_x = (686 - 600) * scale  # the clip's right edge in the enlarged crop
top, bottom = 20 + (197 - 192) * scale, 20 + (248 - 192) * scale
middle = (top + bottom) // 2
gold, soft = (220, 192, 138), (201, 194, 180)
grab = 10 * scale
for y0, y1, colour in ((top, middle, (235, 230, 220)), (middle, bottom, gold)):
    draw.rectangle((edge_x - grab, y0, edge_x, y1), outline=colour, width=3)
label_x = edge.width + 30
for y, title, line, colour in (
    ((top + middle) // 2, "Upper half", "drag to make it longer or shorter", (235, 230, 220)),
    ((middle + bottom) // 2, "Lower half", "drag to loop it", gold),
):
    draw.line((edge_x + 4, y, label_x - 10, y), fill=colour, width=2)
    draw.text((label_x, y - 30), title, font=font, fill=colour)
    draw.text((label_x, y + 2), line, font=small, fill=soft)
canvas.save(out / "clip-edge.webp", quality=92)
print("written to", out)
