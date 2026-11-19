"""Build the profile's static SVG assets. Requires fonttools; no API keys.

Run with --download once to obtain Manrope and the six Shields badges.
Subsequent runs use the committed assets and require no network access.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT = ASSETS / "fonts" / "Manrope.ttf"

DOWNLOADS = {
    "fonts/Manrope.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/Manrope%5Bwght%5D.ttf",
    "fonts/OFL.txt": "https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/OFL.txt",
    "badges/python.svg": "https://img.shields.io/badge/Python-244b40?style=flat-square&logo=python&logoColor=white",
    "badges/typescript.svg": "https://img.shields.io/badge/TypeScript-244b40?style=flat-square&logo=typescript&logoColor=white",
    "badges/aws.svg": "https://img.shields.io/badge/AWS-244b40?style=flat-square",
    "badges/fastapi.svg": "https://img.shields.io/badge/FastAPI-244b40?style=flat-square&logo=fastapi&logoColor=white",
    "badges/nextjs.svg": "https://img.shields.io/badge/Next.js-244b40?style=flat-square&logo=nextdotjs&logoColor=white",
    "badges/java.svg": "https://img.shields.io/badge/Java-244b40?style=flat-square",
}

THEMES = {
    "light": {"bg": "#f4f3ec", "ink": "#173d32", "muted": "#49665a", "line": "#6b8673", "panel": "#e4eadf", "accent": "#d7edb8"},
    "dark": {"bg": "#132b24", "ink": "#f0f5e9", "muted": "#b2c8b9", "line": "#5c7e6a", "panel": "#234338", "accent": "#d7edb8"},
}


def download(item):
    name, url = item
    target = ASSETS / name
    target.parent.mkdir(parents=True, exist_ok=True)
    request = Request(url, headers={"User-Agent": "pirlapal-profile-assets/1.0"})
    with urlopen(request, timeout=30) as response:
        content = response.read()
    if name.endswith(".svg") and b"<svg" not in content:
        raise ValueError(f"Expected an SVG badge: {name}")
    target.write_bytes(content)
    return name


class Lettering:
    def __init__(self):
        self.fonts = {}
        for weight in (500, 600, 750):
            font = instantiateVariableFont(TTFont(FONT), {"wght": weight})
            self.fonts[weight] = (font, font.getGlyphSet(), font.getBestCmap())

    def text(self, value, x, y, size, color, weight=500, anchor="start", tracking=0):
        font, glyphs, cmap = self.fonts[weight]
        scale = size / font["head"].unitsPerEm
        names = [cmap[ord(char)] for char in value]
        width = sum(font["hmtx"].metrics[name][0] * scale for name in names)
        width += tracking * max(0, len(names) - 1)
        if anchor == "middle":
            x -= width / 2
        pen = SVGPathPen(glyphs)
        for name in names:
            glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
            x += font["hmtx"].metrics[name][0] * scale + tracking
        return f'<path fill="{color}" d="{pen.getCommands()}"/>'


def svg(title, description, width, height, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-labelledby="title description">'
        f'<title id="title">{escape(title)}</title>'
        f'<desc id="description">{escape(description)}</desc>'
        + "".join(body) + "</svg>\n"
    )


def rect(x, y, w, h, fill, radius=0, stroke=None):
    border = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"{border}/>'


def arrow(x1, x2, y, color):
    return f'<path d="M{x1} {y}H{x2}m-8-7 8 7-8 7" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'


def header(theme, t, lettering):
    ink, muted = t["ink"], t["muted"]
    text = lettering.text
    body = [rect(0, 0, 1200, 352, t["bg"], 16)]
    body += [
        text("Pranav", 56, 120, 82, ink, 750, tracking=-2),
        text("Irlapale", 56, 213, 82, ink, 750, tracking=-2),
        text("Software engineering + applied AI", 60, 286, 27, muted, 500),
    ]
    # A real relationship diagram, rather than a simulated application screenshot.
    body += [
        rect(793, 47, 340, 72, t["panel"], 12),
        text("Data + documents", 963, 92, 26, ink, 600, "middle"),
        '<path d="M963 120v27m-7-8 7 8 7-8" fill="none" stroke="' + t["line"] + '" stroke-width="2.5"/>',
        rect(793, 151, 340, 72, t["panel"], 12),
        text("APIs + tools", 963, 196, 26, ink, 600, "middle"),
        '<path d="M963 224v27m-7-8 7 8 7-8" fill="none" stroke="' + t["line"] + '" stroke-width="2.5"/>',
        rect(793, 255, 340, 58, t["accent"], 12),
        text("AI workflows", 963, 293, 26, "#173d32", 750, "middle"),
    ]
    return svg("Pranav Irlapale — software engineering and applied AI", "Pranav Irlapale. Software engineering and applied AI. Data and documents connect through APIs and tools to AI workflows.", 1200, 352, body)


def pipeline(kind, t, lettering):
    text = lettering.text
    body = [rect(0, 0, 1200, 190, t["bg"], 12)]
    if kind == "planai":
        nodes = [(36, "Documents + rules", "case inputs"), (438, "Python orchestrator", "category agents"), (840, "Review findings", "PASS / FAIL / NEEDS_REVIEW")]
        title = "PlanAI review flow"
        description = "Case documents and review rules feed a Python orchestrator with category agents, producing structured review findings."
    else:
        nodes = [(36, "Demo / Google Sheets", "evaluation records"), (438, "FastAPI adapter", "validation + data contract"), (840, "Next.js dashboard", "filter + review + update status")]
        title = "Recruiter dashboard data flow"
        description = "Fictional demo records or an optional Google Sheets data source pass through the FastAPI adapter into the Next.js review dashboard."
    for x, label, sublabel in nodes:
        body += [rect(x, 38, 324, 114, t["panel"], 12), text(label, x + 162, 88, 25, t["ink"], 750, "middle"), text(sublabel, x + 162, 123, 18, t["muted"], 500, "middle")]
    body += [arrow(374, 420, 95, t["line"]), arrow(776, 822, 95, t["line"])]
    return svg(title, description, 1200, 190, body)


def mobile_header(t, lettering):
    text = lettering.text
    body = [rect(0, 0, 600, 260, t["bg"], 12)]
    body += [text("Pranav Irlapale", 32, 86, 56, t["ink"], 750, tracking=-1.2), text("Software engineering + applied AI", 34, 138, 25, t["muted"])]
    for index, (x, label) in enumerate(((32, "Data"), (240, "APIs"), (448, "AI"))):
        body += [rect(x, 176, 120, 56, t["accent"] if index == 2 else t["panel"], 10), text(label, x + 60, 212, 25, "#173d32" if index == 2 else t["ink"], 600, "middle")]
        if index < 2:
            body += [arrow(x + 136, x + 192, 204, t["line"])]
    return svg("Pranav Irlapale — software engineering and applied AI", "Pranav Irlapale. Software engineering and applied AI. Data connects through APIs to AI workflows.", 600, 260, body)


def mobile_pipeline(kind, t, lettering):
    text = lettering.text
    body = [rect(0, 0, 600, 352, t["bg"], 12)]
    if kind == "planai":
        nodes = [("Documents + rules", "case inputs"), ("Python orchestrator", "category agents"), ("Review findings", "PASS / FAIL / NEEDS_REVIEW")]
        title = "PlanAI review flow"
    else:
        nodes = [("Demo / Google Sheets", "evaluation records"), ("FastAPI adapter", "validation + data contract"), ("Next.js dashboard", "filter + review + update status")]
        title = "Recruiter dashboard data flow"
    for index, (label, sublabel) in enumerate(nodes):
        y = 20 + index * 116
        body += [rect(60, y, 480, 80, t["panel"], 12), text(label, 300, y + 34, 27, t["ink"], 750, "middle"), text(sublabel, 300, y + 63, 20, t["muted"], 500, "middle")]
        if index < 2:
            body += [f'<path d="M300 {y + 85}v25m-6-6 6 6 6-6" fill="none" stroke="{t["line"]}" stroke-width="2.5"/>']
    return svg(title, "A vertical version of the project's documented data flow.", 600, 352, body)


def mobile_lumos(t, lettering):
    body = [rect(0, 0, 600, 464, t["bg"], 12)]
    for index, label in enumerate(("Source", "Lexer", "Parser", "AST", "Interpreter")):
        y = 20 + index * 90
        body += [rect(100, y, 400, 64, t["accent"] if index == 4 else t["panel"], 12), lettering.text(label, 300, y + 42, 28, "#173d32" if index == 4 else t["ink"], 750, "middle")]
        if index < 4:
            body += [f'<path d="M300 {y + 69}v16m-6-6 6 6 6-6" fill="none" stroke="{t["line"]}" stroke-width="2.5"/>']
    return svg("Lumos interpreter pipeline", "Source, lexer, parser, abstract syntax tree, and interpreter, shown vertically.", 600, 464, body)


def lumos(t, lettering):
    text = lettering.text
    body = [rect(0, 0, 1200, 190, t["bg"], 12)]
    stages = [(40, "Source"), (272, "Lexer"), (504, "Parser"), (736, "AST"), (968, "Interpreter")]
    for index, (x, label) in enumerate(stages):
        body += [rect(x, 54, 192, 82, t["accent"] if index == 4 else t["panel"], 12), text(label, x + 96, 104, 25, "#173d32" if index == 4 else t["ink"], 750, "middle")]
        if index < 4:
            body += [arrow(x + 204, x + 220, 95, t["line"])]
    return svg("Lumos interpreter pipeline", "Lumos source passes through a handwritten lexer, recursive-descent parser, abstract syntax tree, and tree-walking interpreter.", 1200, 190, body)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    if args.download:
        with ThreadPoolExecutor(max_workers=6) as pool:
            for name in pool.map(download, DOWNLOADS.items()):
                print("Downloaded", name)
    if not FONT.is_file():
        parser.error("Manrope is missing. Run once with --download.")
    lettering = Lettering()
    for theme, colors in THEMES.items():
        for name, contents in {
            "header": header(theme, colors, lettering),
            "planai": pipeline("planai", colors, lettering),
            "dashboard": pipeline("dashboard", colors, lettering),
            "lumos": lumos(colors, lettering),
            "header-mobile": mobile_header(colors, lettering),
            "planai-mobile": mobile_pipeline("planai", colors, lettering),
            "dashboard-mobile": mobile_pipeline("dashboard", colors, lettering),
            "lumos-mobile": mobile_lumos(colors, lettering),
        }.items():
            path = ASSETS / f"{name}-{theme}.svg"
            path.write_text(contents)
            print("Built", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
