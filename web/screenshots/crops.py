"""Crops the manual's pictures out of the demo song's screenshot, as
shoot.py takes it: 1400 by 700 points, the side panels hidden, at SCALE
pixels to a point. Every place below is in points; a picture is shown at
its size in points, sharp and never enlarged.

  python crops.py SHOT OUT_DIR [SCALE]
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

shot = Image.open(sys.argv[1]).convert("RGB")
out = Path(sys.argv[2])
scale = int(sys.argv[3]) if len(sys.argv) > 3 else 2
out.mkdir(parents=True, exist_ok=True)


def crop(left, top, right, bottom):
    return shot.crop((left * scale, top * scale, right * scale, bottom * scale))


def face(size):
    # A clean sans the system has: Windows', macOS's, or most Linuxes'.
    for name in ("C:/Windows/Fonts/segoeui.ttf", "/System/Library/Fonts/Helvetica.ttc",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size * scale)
        except OSError:
            pass
    return ImageFont.load_default(size * scale)


# The arrangement's first four bars: the tracks and the keys' automation lane,
# without the window's bar or the status line (which shows the project's path).
crop(0, 95, 700, 428).save(out / "arrangement.webp", quality=90)

# The automation lane alone, its head and both its clips.
crop(0, 316, 700, 428).save(out / "automation-lane.webp", quality=90)

# A clip's right edge at its own size, its two halves marked and named.
left, top, right, bottom = 540, 176, 700, 270
edge = crop(left, top, right, bottom)
labels = 250
canvas = Image.new("RGB", (edge.width + labels * scale, edge.height), (17, 18, 25))
canvas.paste(edge, (0, 0))
draw = ImageDraw.Draw(canvas)
title, small = face(14), face(11)
edge_x = (686 - left) * scale  # the Bassline clip's right edge
clip_top, clip_bottom = (197 - top) * scale, (248 - top) * scale
middle = (clip_top + clip_bottom) // 2
white, gold, soft = (235, 230, 220), (220, 192, 138), (201, 194, 180)
grab = 10 * scale
for y0, y1, color in ((clip_top, middle, white), (middle, clip_bottom, gold)):
    draw.rectangle((edge_x - grab, y0, edge_x, y1), outline=color, width=scale)
label_x = edge.width + 18 * scale
# The upper half's words stand above its line and the lower half's below
# theirs, so the two never meet.
for y, name, line, color, above in (
    ((clip_top + middle) // 2, "Upper half", "longer or shorter", white, True),
    ((middle + clip_bottom) // 2, "Lower half", "loops it", gold, False),
):
    draw.line((edge_x + 3 * scale, y, label_x + 150 * scale, y), fill=color, width=scale)
    first = y - 34 * scale if above else y + 3 * scale
    draw.text((label_x, first), name, font=title, fill=color)
    draw.text((label_x, first + 17 * scale), line, font=small, fill=soft)
canvas.save(out / "clip-edge.webp", quality=90)
print("written to", out)
