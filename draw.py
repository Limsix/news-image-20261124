"""Draw the front page of The World Today for 24 November 2026.

All drawing is done with PIL shapes and the bundled DejaVu fonts.
No network, no randomness, no timestamps: identical input gives
identical output bytes.
"""
from PIL import Image, ImageDraw, ImageFont
import os


W, H = 1024, 1024
INK = (18, 18, 18)
PAPER = (252, 250, 244)
GREY = (90, 90, 88)
LIGHT_GREY = (225, 222, 214)
RED = (158, 28, 22)
SEA = (38, 84, 112)
SEA_DARK = (24, 58, 82)
SKY = (214, 228, 235)
FIRE = (224, 122, 28)
FIRE2 = (240, 178, 44)
SMOKE = (70, 70, 70)


def _font(base, name, size):
    return ImageFont.truetype(os.path.join(base, "fonts", name), size)


def _wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def _para(draw, x, y, text, font, max_w, leading, color=INK):
    for line in _wrap(draw, text, font, max_w):
        draw.text((x, y), line, font=font, fill=color)
        y += leading
    return y


def _headline(draw, x, y, text, font, max_w, leading):
    return _para(draw, x, y, text, font, max_w, leading)


def _rule(draw, x0, y, x1, width=2):
    draw.line([(x0, y), (x1, y)], fill=INK, width=width)


def _draw_tanker_scene(draw, x0, y0, x1, y1):
    """Strait of Hormuz: sea, tanker, mine blast and fire. Pure PIL shapes."""
    draw.rectangle([x0, y0, x1, y1], fill=SKY, outline=INK, width=2)
    # distant headland
    draw.polygon([(x0, y0 + 118), (x0 + 150, y0 + 52), (x0 + 300, y0 + 118)],
                 fill=(148, 158, 140))
    draw.polygon([(x1 - 260, y0 + 118), (x1 - 120, y0 + 62), (x1, y0 + 118)],
                 fill=(148, 158, 140))
    # sun
    draw.ellipse([x1 - 92, y0 + 18, x1 - 42, y0 + 68], fill=FIRE2, outline=INK, width=1)
    # sea
    draw.rectangle([x0, y0 + 118, x1, y1], fill=SEA)
    for wy in (y0 + 150, y0 + 182, y0 + 214):
        for wx in range(x0 + 18, x1 - 40, 74):
            draw.line([(wx, wy), (wx + 38, wy)], fill=(150, 190, 205), width=3)
    # tanker hull
    hx0, hx1 = x0 + 58, x1 - 58
    hy = y0 + 168
    draw.polygon([(hx0, hy), (hx1, hy), (hx1 - 26, hy + 42), (hx0 + 26, hy + 42)],
                 fill=(122, 32, 26), outline=INK, width=2)
    draw.rectangle([hx0 + 30, hy - 52, hx1 - 170, hy], fill=(210, 198, 170),
                   outline=INK, width=2)
    # bridge tower
    draw.rectangle([hx1 - 150, hy - 78, hx1 - 84, hy], fill=(240, 236, 224),
                   outline=INK, width=2)
    for wx in range(hx1 - 142, hx1 - 88, 18):
        draw.rectangle([wx, hy - 66, wx + 10, hy - 52], fill=SEA_DARK)
    # funnel with smoke
    draw.rectangle([hx0 + 210, hy - 66, hx0 + 252, hy - 14], fill=(30, 30, 30),
                   outline=INK, width=2)
    draw.ellipse([hx0 + 268, hy - 118, hx0 + 322, hy - 68], fill=SMOKE)
    draw.ellipse([hx0 + 300, hy - 142, hx0 + 360, hy - 88], fill=(105, 105, 105))
    draw.ellipse([hx0 + 336, hy - 158, hx0 + 388, hy - 108], fill=(140, 140, 140))
    # mine blast: fireball and spray at the bow
    cx, cy = hx0 + 62, hy - 22
    draw.ellipse([cx - 52, cy - 52, cx + 52, cy + 52], fill=FIRE, outline=INK, width=2)
    draw.ellipse([cx - 32, cy - 32, cx + 32, cy + 32], fill=FIRE2)
    draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=(250, 232, 120))
    for dx, dy in ((-64, -30), (58, -42), (70, 6), (-58, 34), (30, -64)):
        draw.line([(cx, cy), (cx + dx, cy + dy)], fill=FIRE, width=4)
    # small naval mine in the water, foreground right
    mx, my = x1 - 150, y1 - 34
    draw.ellipse([mx - 20, my - 20, mx + 20, my + 20], fill=(40, 40, 40),
                 outline=INK, width=2)
    for dx, dy in ((-24, 0), (24, 0), (0, -24), (0, 24), (-17, -17), (17, 17)):
        draw.line([(mx, my), (mx + dx, my + dy)], fill=INK, width=3)
    # caption bar
    draw.rectangle([x0, y1 - 26, x1, y1], fill=(18, 18, 18))
    return y1


def render(base_dir):
    serif = _font(base_dir, "DejaVuSerif-Bold.ttf", 64)
    serif_small = _font(base_dir, "DejaVuSerif-Bold.ttf", 30)
    serif_head = _font(base_dir, "DejaVuSerif-Bold.ttf", 40)
    serif_sub = _font(base_dir, "DejaVuSerif-Bold.ttf", 23)
    sans = _font(base_dir, "DejaVuSans.ttf", 19)
    sans_small = _font(base_dir, "DejaVuSans.ttf", 17)
    sans_bold = _font(base_dir, "DejaVuSans-Bold.ttf", 15)
    sans_kicker = _font(base_dir, "DejaVuSans-Bold.ttf", 16)

    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    m = 36
    x1 = W - m

    # ---- Masthead ----
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=serif)
    d.text(((W - tw) / 2, 18), title, font=serif, fill=INK)
    d.text((m, 92), "Tuesday, 24 November 2026", font=sans_bold, fill=INK)
    tag = "One day's world news, in one page"
    tw2 = d.textlength(tag, font=sans_small)
    d.text((x1 - tw2, 94), tag, font=sans_small, fill=GREY)
    _rule(d, m, 122, x1, 4)
    _rule(d, m, 130, x1, 1)

    # ---- Lead story ----
    y = 148
    d.text((m, y), "LEAD  |  STRAIT OF HORMUZ", font=sans_kicker, fill=RED)
    y += 26
    y = _headline(d, m, y, "TANKER HIT BY MINE IN", serif_head, x1 - m, 48)
    y = _headline(d, m, y, "STRAIT OF HORMUZ", serif_head, x1 - m, 48)
    y += 6
    lead_body = (
        "Iran's Revolutionary Guard Navy says an oil tanker was struck by a "
        "naval mine in the Strait of Hormuz and caught fire, as Iran vows to "
        "use all its tools against the US naval blockade."
    )
    y = _para(d, m, y, lead_body, sans, x1 - m, 26)
    y += 10
    scene_top = y
    scene_bottom = scene_top + 210
    _draw_tanker_scene(d, m, scene_top, x1, scene_bottom)
    d.text((m + 10, scene_bottom - 22), "A tanker burns after a mine strike in the Strait of Hormuz.",
           font=sans_small, fill=(255, 255, 255))
    y = scene_bottom + 16
    _rule(d, m, y, x1, 2)
    y += 14

    # ---- Secondary stories: 2 x 2 grid ----
    stories = [
        ("DIPLOMACY  |  WASHINGTON",
         "Vance, Rubio meet Qatari PM at White House",
         "US Vice President JD Vance and Secretary of State Marco Rubio met "
         "separately with Qatar's Prime Minister Sheikh Mohammed bin "
         "Abdulrahman Al Thani as Iran crisis diplomacy continues."),
        ("GAZA",
         "Israeli strike kills Hamas security chief in Gaza",
         "Naeem Abu Nahel, director of Hamas' internal security apparatus, "
         "killed with six others including two police officers."),
        ("UKRAINE",
         "Russian strike hits Zaporizhzhia flats: 2 dead, 40 hurt",
         "Overnight attack on an apartment building, four children among "
         "the wounded."),
        ("SPACE  |  NATO",
         "NATO vows space defence after Russian satellite reports",
         "Chief Mark Rutte says the alliance will defend against threats "
         "in space."),
    ]
    col_w = (x1 - m - 28) // 2
    row_h = 172
    for i, (kicker, head, body) in enumerate(stories):
        cx = m + (i % 2) * (col_w + 28)
        cy = y + (i // 2) * row_h
        d.text((cx, cy), kicker, font=sans_kicker, fill=RED)
        cy += 22
        cy = _headline(d, cx, cy, head, serif_sub, col_w, 30)
        cy += 2
        _para(d, cx, cy, body, sans_small, col_w, 22)
        if i % 2 == 0:
            d.line([(cx + col_w + 14, y + (i // 2) * row_h),
                    (cx + col_w + 14, y + (i // 2) * row_h + row_h - 16)],
                   fill=LIGHT_GREY, width=2)
    y = y + 2 * row_h + 4
    _rule(d, m, y, x1, 1)
    footer = "Sources: AP  |  Reuters  |  BBC  —  The World Today, 24 November 2026"
    fw = d.textlength(footer, font=sans_small)
    d.text(((W - fw) / 2, y + 8), footer, font=sans_small, fill=GREY)
    return img
