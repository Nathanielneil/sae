"""Regenerate the README plates (stdlib only). Run from any directory."""
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
SANS = "Inter,Arial,'PingFang SC','Microsoft YaHei',sans-serif"
SERIF = "Georgia,'Times New Roman',serif"
MONO = "'SFMono-Regular',Consolas,monospace"
INK, MUTED, RED, TEAL = "#172f3a", "#50656b", "#a13932", "#13665a"


def t(x, y, text, size=22, color=INK, face=SANS, extra=""):
    return f'  <text x="{x}" y="{y}" fill="{color}" font-family="{face}" font-size="{size}" {extra}>{escape(text)}</text>'


def rule(x1, y1, x2, y2, color, width=1):
    return f'  <path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>'


def rect(x, y, w, h, color, r=0):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{color}"/>'


def label(x, y, text, color=MUTED, size=15):
    return t(x, y, text, size, color, MONO, 'font-weight="600" letter-spacing="1"')


def plate(name, w, h, title, description, contents):
    (ASSETS / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">\n'
        f'  <title id="title">{escape(title)}</title>\n  <desc id="desc">{escape(description)}</desc>\n'
        + "\n".join(contents) + "\n</svg>\n", encoding="utf-8")


def cover(mobile):
    w, h = (400, 180) if mobile else (920, 248)
    # Two manuscript sheets and a diagonally laid editing pencil.
    art = '\n'.join([
        '<g transform="rotate(-9 138 88)">',
        rect(19, 16, 222, 154, "#708b89", 3),
        rect(12, 8, 222, 154, "#ccd7cb", 3), '</g>',
        '<g transform="rotate(7 130 87)">',
        rect(28, 11, 220, 152, "#fbf3da", 3),
        rect(44, 28, 55, 4, "#25454d"), rect(44, 39, 126, 2, "#adc0af"),
        rect(44, 60, 87, 5, "#6c8581"), rect(138, 60, 53, 5, "#a9b9ac"),
        rect(44, 78, 46, 5, "#89a19a"), rect(97, 78, 94, 5, "#89a19a"),
        rule(92, 82, 135, 77, "#c94e3d", 2.7),
        '<path d="M96 86q18 5 38 0m-25 9 6-5 5 4" fill="none" stroke="#b83c32" stroke-width="2.4" stroke-linecap="round"/>',
        rect(44, 103, 128, 5, "#a9b9ac"), rect(44, 122, 83, 5, "#a9b9ac"),
        '<path d="m193 98 5 5 10-12" fill="none" stroke="#177566" stroke-width="3.5" stroke-linecap="round"/>',
        '</g>',
        '<g transform="translate(137 122) rotate(-35)">',
        '<path d="M0 0 19-5h113q5 0 5 5t-5 5H19z" fill="#e87e62"/>',
        '<path d="M19 0h113v5H19z" fill="#c85548"/><path d="M0 0l19-5v10z" fill="#eac6a0"/><path d="m0 0 6-1.6V1.6z" fill="#1e3541"/>',
        '<path d="M121-5v10" stroke="#ae4139" stroke-width="3"/></g>',
    ])
    if mobile:
        c = [rect(0, 0, w, h, INK, 8), label(20, 28, "CODEX  /  SKILL", "#b5dace", 10),
             t(16, 103, "SAE", 81, "#fbf4df", SERIF),
             t(20, 135, "Standard Academic", 18, "#e0ebe3"),
             t(20, 158, "Editing", 18, "#e0ebe3"),
             f'<g transform="translate(207 40) scale(.65)">{art}</g>']
    else:
        c = [rect(0, 0, w, h, INK, 10), rule(38, 49, 417, 49, "#52716f"),
             label(40, 36, "CODEX  /  MANUSCRIPT EDITING", "#b5dace", 12),
             t(31, 161, "SAE", 120, "#fbf4df", SERIF),
             t(40, 203, "Standard Academic Editing", 27, "#e0ebe3"),
             f'<g transform="translate(528 16) scale(1.24)">{art}</g>']
    plate("hero-mobile.svg" if mobile else "hero.svg", w, h, "SAE · Standard Academic Editing",
          "A marked-up manuscript and editing pencil.", c)


def proof(mobile):
    # Set an actual excerpt twice. The green rule marks the words limiting the inference.
    w, h = (400, 298) if mobile else (920, 255)
    x = 20 if mobile else 32
    c = [rect(0, 0, w, h, "#f9f5eb", 8)]
    def marked(x, y, before, words, after, size, original=False):
        mark = "line-through" if original else "underline"
        color = RED if original else TEAL
        return (f'<text x="{x}" y="{y}" fill="{INK}" font-family="{SERIF}" font-size="{size}">'
                f'{escape(before)}<tspan fill="{color}" text-decoration="{mark}">{escape(words)}</tspan>'
                f'{escape(after)}</text>')

    if mobile:
        c += [label(x, 29, "01  /  MANUSCRIPT PROOF", size=12), rule(x, 42, 380, 42, "#c7c6b9"),
              label(x, 66, "ORIGINAL", RED, 12), marked(x, 94, "", "Of course,", " these results do not establish", 19, True),
              t(x, 120, "that the method can fully replace", 19, face=SERIF),
              t(x, 146, "conventional methods.", 19, face=SERIF), rule(x, 164, 380, 164, "#dad6c6"),
              label(x, 188, "EDITED", TEAL, 12), marked(x, 216, "These results ", "do not establish", " that", 19),
              t(x, 242, "the method can fully replace", 19, face=SERIF),
              t(x, 268, "conventional methods.", 19, face=SERIF)]
    else:
        c += [label(x, 32, "01  /  MANUSCRIPT PROOF", size=14), rule(x, 48, 888, 48, "#c7c6b9"),
              label(x, 82, "ORIGINAL", RED), marked(175, 85, "", "Of course,", " these results do not establish that the method", 24, True),
              t(175, 116, "can fully replace conventional methods.", 24, face=SERIF),
              rule(x, 142, 888, 142, "#dad6c6"),
              label(x, 177, "EDITED", TEAL), marked(175, 180, "These results ", "do not establish", " that the method", 24),
              t(175, 211, "can fully replace conventional methods.", 24, face=SERIF)]
    plate("proof-mobile.svg" if mobile else "proof.svg", w, h, "Removing an empty preface",
          "Remove Of course; retain the statement that the results do not establish full replacement.", c)


def numbers(mobile, zh):
    w, h = (400, 222) if mobile else (920, 195)
    x = 20 if mobile else 32
    start, end = (20, 378) if mobile else (278, 865)
    c = [rect(0, 0, w, h, "#edf4ef", 8), label(x, 29, "02  /  DATA CHECK", size=12 if mobile else 14),
         t(w-x, 29, "测试队列 · 准确率" if zh else "Test cohort · Accuracy", 15 if mobile else 18, TEAL,
           extra='text-anchor="end"')]
    for i, (en, cn, value, color) in enumerate([
        ("Proposed method", "所提方法", 87.4, TEAL), ("Baseline model", "基线模型", 81.2, "#506979")]):
        y = (81+72*i) if mobile else (83+51*i)
        tx, ty = (x, y-13) if mobile else (x, y+6)
        c.append(t(tx, ty, cn if zh else en, 17 if mobile else 19))
        nx, ny = (end, ty) if mobile else (244, ty)
        c.append(t(nx, ny, f"{value:.1f}%", 19 if mobile else 21, color, MONO, 'text-anchor="end" font-weight="bold"'))
        c += [rect(start, y, end-start, 8, "#d5e1d9", 4),
              rect(start, y, (end-start)*value/100, 8, color, 4)]
    axis = 200 if mobile else 174
    for v in (0, 50, 100):
        xx = start + (end-start)*v/100
        align = {0:"start",50:"middle",100:"end"}[v]
        c += [rule(xx, axis-17, xx, axis-12, "#81978e"),
              t(xx, axis+2, f"{v}%", 12 if mobile else 14, MUTED, MONO, f'text-anchor="{align}"')]
    plate(f"values-{'zh' if zh else 'en'}{'-mobile' if mobile else ''}.svg", w, h,
          "测试队列中的准确率" if zh else "Accuracy in the illustrative test cohort",
          "Proposed method: 87.4%. Baseline model: 81.2%. Both bars use the same 0–100% scale.", c)


def routes(mobile, zh):
    w, h = (400, 223) if mobile else (920, 213)
    x = 20 if mobile else 32
    c = [rect(0, 0, w, h, "#f0f3f6", 8), label(x, 29, "03  /  EDITORIAL DECISIONS", size=12 if mobile else 14)]
    rows = [("Language only","仅涉及语言","Edit directly","直接编辑",TEAL),
            ("Conflicting evidence","发现证据冲突","Ask the author","向作者确认",RED),
            ("Missing context","缺少上下文","Retain the claim","保留原主张",INK)]
    for i,(ei,ci,eo,co,color) in enumerate(rows):
        if mobile:
            y = 72+i*59
            c += [rule(x, y-26, 380, y-26, "#cdd7d9"),
                  t(x, y+6, ci if zh else ei, 17),
                  rule(182, y, 217, y, "#789191", 1.5),
                  f'<path d="m211 {y-4} 6 4-6 4" fill="none" stroke="#789191" stroke-width="1.5"/>',
                  t(232, y+6, co if zh else eo, 17, color, extra='font-weight="600"')]
        else:
            left = x+i*297
            if i: c.append(rule(left-18, 59, left-18, 182, "#c6d0d3"))
            c += [t(left, 79, ci if zh else ei, 19), rule(left+5, 92, left+5, 120, "#789191", 1.5),
                  f'<path d="m{left} 115 5 6 5-6" fill="none" stroke="#789191" stroke-width="1.5"/>',
                  t(left, 162, co if zh else eo, 27, color, SANS if zh else SERIF)]
    plate(f"decisions-{'zh' if zh else 'en'}{'-mobile' if mobile else ''}.svg", w, h,
          "编辑判断" if zh else "Three editorial decisions",
          "Edit language directly; query concrete conflicts when permitted; retain claims when context is missing.", c)


if __name__ == "__main__":
    for narrow in (False, True):
        cover(narrow)
        proof(narrow)
        for chinese in (False, True):
            numbers(narrow, chinese)
            routes(narrow, chinese)
