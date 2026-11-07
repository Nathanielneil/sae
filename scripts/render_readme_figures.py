"""Draw SAE's README figures, including narrow layouts; Python standard library only."""
from html import escape
from pathlib import Path
from typing import NamedTuple

ASSETS = Path(__file__).resolve().parents[1] / "assets"
SERIF = "Baskerville,'Iowan Old Style','Palatino Linotype',Georgia,'Songti SC',serif"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,'PingFang SC','Microsoft YaHei',sans-serif"
PALETTE = """
:root {
  --paper:#fff; --ink:#302d40; --soft:#625e73;
  --violet:#634f81; --old:#795e68; --hair:#d9d4e2; --graph:#aa9ebd;
  --bloom:#e9e4f2; --silk:#a08bb8; --glint:#c6b9d3; --echo:#b9a39c;
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper:#0d1117; --ink:#eeeaf1; --soft:#c0bbc9;
    --violet:#cfbce6; --old:#d4b7c1; --hair:#494858; --graph:#a699b8;
    --bloom:#292637; --silk:#88799f; --glint:#ad9ac3; --echo:#ad9596;
  }
}
"""


class Grid(NamedTuple):
    """Two equal columns; the 2-unit edge protects italic glyphs from clipping."""
    width: int
    gutter: int
    edge: int = 2

    @property
    def column(self):
        return (self.width - 2 * self.edge - self.gutter) // 2

    def left(self, index):
        return self.edge + index * (self.column + self.gutter)

    def center(self, index):
        return self.left(index) + self.column / 2


def grid(mobile):
    return Grid(400, 24) if mobile else Grid(920, 64)


CENTER = 'text-anchor="middle"'
ITALIC = 'font-style="italic"'
MIDLINE = 'dominant-baseline="central"'


def txt(x, y, words, size, color="ink", font=SANS, attrs=""):
    return (f'<text x="{x}" y="{y}" fill="var(--{color})" font-family="{font}" '
            f'font-size="{size}" {attrs}>{escape(words)}</text>')


def line(x1, y1, x2, y2, color="hair", width=1):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="var(--{color})" stroke-width="{width}" fill="none"/>'


def path(d, color, width=1, opacity=1):
    return (f'<path d="{d}" fill="none" stroke="var(--{color})" stroke-width="{width}" '
            f'opacity="{opacity}" stroke-linecap="round"/>')


def dot(x, y, r, color="violet", hollow=False):
    fill = "paper" if hollow else color
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--{fill})" stroke="var(--{color})" stroke-width="1.5"/>'


def plate(name, w, h, title, desc, content):
    (ASSETS / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-labelledby="title desc">\n<title id="title">{escape(title)}</title>\n'
        f'<desc id="desc">{escape(desc)}</desc>\n<style>{PALETTE}</style>\n'
        f'<rect width="{w}" height="{h}" fill="var(--paper)"/>\n' + "\n".join(content) + "\n</svg>\n",
        encoding="utf-8")


def silk():
    """Interpolate two folded cubic splines: every filament follows the same continuous sheet."""
    # Control points for the two selvedges of each length of silk (three cubic segments).
    edges = [
        ([(318,278),(464,240),(444,143),(554,111),(682,73),(668,214),(775,170),(846,140),(878,28),(968,-42)],
         [(307,303),(501,254),(480,140),(588,111),(706,79),(680,232),(779,204),(870,179),(916,94),(975,77)]),
        ([(467,298),(584,279),(668,228),(699,126),(736,6),(825,72),(859,90),(904,113),(941,112),(979,90)],
         [(443,285),(571,285),(658,190),(686,109),(735,-31),(796,50),(841,67),(884,96),(939,112),(980,103)])
    ]
    layers = []
    for k,(a,b) in enumerate(edges):
        count = 34 if k == 0 else 22
        for n in range(count):
            f=n/(count-1)
            points = ["%.2f %.2f" % (x+(u-x)*f, y+(v-y)*f)
                      for (x,y),(u,v) in zip(a,b)]
            d = "M"+points[0]+" C"+" ".join(points[1:])
            layers.append(path(d, "silk" if k == 0 else "glint", 0.82 if k == 0 else 0.68,
                               round((0.36 if k == 0 else 0.27)+0.44*(1-f)**1.8,3)))
    layers.append(path("M407 300C555 243 547 175 654 167S803 225 954 38","echo",1,0.7))
    return "".join(layers)


def cover(mobile):
    w,h = (400,225) if mobile else (920,292)
    # A quiet vignette dissolves into the page at every edge.
    start, end = (159,260) if mobile else (304,493)
    wash = ('<defs><radialGradient id="wash"><stop offset="0" stop-color="var(--bloom)" stop-opacity=".94"/>'
            '<stop offset=".55" stop-color="var(--bloom)" stop-opacity=".53"/>'
            '<stop offset="1" stop-color="var(--paper)" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="veil" gradientUnits="userSpaceOnUse" x1="{start}" x2="{end}">'
            '<stop stop-color="black"/><stop offset="1" stop-color="white"/></linearGradient>'
            f'<mask id="fade" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}">'
            f'<rect width="{w}" height="{h}" fill="url(#veil)"/></mask></defs>')
    c=[wash,f'<ellipse cx="{w*.81}" cy="{h*.50}" rx="{w*.52}" ry="{h*.76}" fill="url(#wash)"/>']
    # Center the type within the title field, leaving the right field for the silk.
    axis = 110 if mobile else grid(False).center(0)
    art = silk()
    if mobile:
        art = f'<g transform="translate(37 17) scale(.39 .57)">{art}</g>'
    half_rule, rule_y = (21,193) if mobile else (31,251)
    c += [f'<g mask="url(#fade)">{art}</g>',
          txt(axis,38 if mobile else 52,"SCIENTIFIC ENGLISH",10.5 if mobile else 12,"soft",
              attrs=f'{CENTER} letter-spacing="2" word-spacing="3"'),
          txt(axis,127 if mobile else 180,"SAE",86 if mobile else 133,"ink",SERIF,
              f'{CENTER} letter-spacing="{-4 if mobile else -6}"'),
          txt(axis,161 if mobile else 221,"Standard Academic Editing",20 if mobile else 31,
              "soft",SERIF,f'{CENTER} {ITALIC}'),
          line(axis-half_rule,rule_y,axis+half_rule,rule_y,"graph")]
    plate("hero-mobile.svg" if mobile else "hero.svg",w,h,"SAE · Standard Academic Editing",
          "The SAE wordmark beside two folded ribbons drawn in fine violet lines.",c)


def wording(x,y,parts,size):
    # Accent stays attached to its actual words, even if the available serif face changes.
    content=[]
    for kind,words in parts:
        if kind == "delete":
            content.append(f'<tspan fill="var(--old)" text-decoration="line-through">{escape(words)}</tspan>')
        elif kind == "keep":
            content.append(f'<tspan fill="var(--violet)" text-decoration="underline">{escape(words)}</tspan>')
        else:
            content.append(escape(words))
    return f'<text x="{x}" y="{y}" font-size="{size}" font-family="{SERIF}" fill="var(--ink)">{"".join(content)}</text>'


def proof(mobile):
    g = grid(mobile)
    w, left, right, mid = g.width, g.edge, g.width - g.edge, g.width // 2
    if mobile:
        h=272
        c=[line(left,4,right,4), line(mid-16,h//2,mid+16,h//2,"graph"), line(left,h-4,right,h-4)]
        columns = [
            ("Original","soft",[[("delete","Of course,"),(""," these results do not establish")],
                                 [("","that the method can fully replace")],[("","conventional methods.")]]),
            ("Edited","violet",[[("","These results "),("keep","do not establish"),(""," that")],
                                [("","the method can fully replace")],[("","conventional methods.")]])]
        for i,(tag,color,lines) in enumerate(columns):
            top = i * 132
            c.append(txt(left,top+35,tag,16,color,SERIF,ITALIC))
            for j,words in enumerate(lines):
                c.append(wording(left,top+65+j*26,words,20))
    else:
        h=204
        c=[line(left,6,right,6),line(left,h-6,right,h-6)]
        for x, tag, color, lines in [
            (g.left(0),"Original","soft",[[("delete","Of course,"),(""," these results do not")],
                                  [("","establish that the method can fully")],[("","replace conventional methods.")]]),
            (g.left(1),"Edited","violet",[[("","These results "),("keep","do not establish")],
                                    [("","that the method can fully replace")],[("","conventional methods.")]])]:
            c.append(txt(x,44,tag,19,color,SERIF,ITALIC))
            for j,words in enumerate(lines):
                c.append(wording(x,89+j*34,words,24))
        c.append(path(f"M{mid-12} 116h24m-5-4 5 4-5 4","graph",1.1))
    plate("proof-mobile.svg" if mobile else "proof.svg",w,h,"Original and edited manuscript excerpt",
          "Of course is deleted. Do not establish is retained: the result does not establish full replacement.",c)


def numbers(mobile,zh):
    g = grid(mobile)
    w,h=g.width,164 if mobile else 180
    c=[txt(w/2,26 if mobile else 32,"测试队列中的准确率" if zh else "Accuracy in the test cohort",
           16 if mobile else 19,"soft",SERIF,CENTER)]
    for i,(model,value) in enumerate([("所提方法" if zh else "Proposed method",87.4),
                                      ("基线模型" if zh else "Baseline model",81.2)]):
        axis = g.center(i)
        baseline=83 if mobile else 101
        c += [txt(axis,baseline,f"{value:.1f}%",43 if mobile else 59,"violet" if i==0 else "ink",SERIF,CENTER),
              txt(axis,baseline+(27 if mobile else 30),model,16 if mobile else 19,"soft",attrs=CENTER)]
        length = g.column - 2 * (12 if mobile else 28)
        x = axis - length / 2
        y=137 if mobile else 159
        c += [line(x,y,x+length,y),line(x,y,x+length*value/100,y,"graph",1.6),
              dot(round(x+length*value/100,2),y,3.8,"violet" if i==0 else "soft",hollow=i==1)]
    plate(f"values-{'zh' if zh else 'en'}{'-mobile' if mobile else ''}.svg",w,h,
          "测试队列中的准确率" if zh else "Test-cohort accuracy",
          "Illustrative values on identical 0 to 100 percent scales: proposed method 87.4%, baseline model 81.2%.",c)


def routes(mobile,zh):
    data=[("措辞问题","Language only","直接编辑","Edit directly"),
          ("证据冲突","Conflicting evidence","向作者确认","Ask the author"),
          ("缺少上下文","Missing context","保留原主张","Keep the claim")]
    # The three stems are alternatives from one origin, not three successive steps.
    g = grid(mobile)
    w,h=g.width,168 if mobile else 176
    row_mid, pitch = h // 2, 49 if mobile else 52
    origin, tip, condition_x, action_x = (g.edge,31,44,234) if mobile else (220,302,323,629)
    c=[] if mobile else [txt(g.edge,row_mid,"编辑判断" if zh else "Editorial judgement",24,"ink",
                             SERIF,MIDLINE if zh else f"{MIDLINE} {ITALIC}")]
    for idx,(condition,en,action,eng) in enumerate(data):
        y=row_mid+(idx-1)*pitch
        c += [path(f"M{origin} {row_mid}C{origin+(tip-origin)*.54} {row_mid} {origin+(tip-origin)*.50} {y} {tip} {y}","graph"),
              dot(tip,y,2.8 if mobile else 3.4,"graph",True),
              txt(condition_x,y,condition if zh else en,17 if mobile else 20,"soft",attrs=MIDLINE),
              txt(action_x,y,action if zh else eng,19 if mobile else 26,"violet",SERIF,MIDLINE)]
        if not mobile:
            c.append(line(547,y,599,y))
    plate(f"decisions-{'zh' if zh else 'en'}{'-mobile' if mobile else ''}.svg",w,h,
          "如何选择编辑方式" if zh else "Choosing an edit",
          "Edit language directly, query concrete conflicts when allowed, and preserve a claim when context is missing.",c)


if __name__ == "__main__":
    for narrow in (False,True):
        cover(narrow)
        proof(narrow)
        for chinese in (False,True):
            numbers(narrow,chinese)
            routes(narrow,chinese)
