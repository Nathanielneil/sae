"""Draw SAE's README figures, including narrow layouts; Python standard library only."""
from html import escape
from pathlib import Path

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
    if mobile:
        c += [f'<g mask="url(#fade)"><g transform="translate(37 17) scale(.39 .57)">{silk()}</g></g>',
              txt(14,38,"SCIENTIFIC ENGLISH",10.5,"soft",attrs='letter-spacing="2" word-spacing="3"'),
              txt(9,127,"SAE",86,"ink",SERIF,'letter-spacing="-4"'),
              txt(15,167,"Standard Academic Editing",20,"soft",SERIF,'font-style="italic"'),
              line(15,195,57,195,"graph")]
    else:
        c += [f'<g mask="url(#fade)">{silk()}</g>',
              txt(30,52,"SCIENTIFIC ENGLISH",12,"soft",attrs='letter-spacing="2.6" word-spacing="3"'),
              txt(22,180,"SAE",133,"ink",SERIF,'letter-spacing="-6"'),
              txt(31,222,"Standard Academic Editing",31,"soft",SERIF,'font-style="italic"'),
              line(32,254,94,254,"graph")]
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
    if mobile:
        w,h=400,286
        c=[line(12,9,388,9),txt(12,38,"Original",16,"soft",SERIF,'font-style="italic"'),
           wording(12,68,[("delete","Of course,"),(""," these results do not establish")],20),
           txt(12,94,"that the method can fully replace",20,font=SERIF),
           txt(12,120,"conventional methods.",20,font=SERIF),
           line(12,142,44,142,"graph"),
           txt(12,168,"Edited",16,"violet",SERIF,'font-style="italic"'),
           wording(12,198,[("","These results "),("keep","do not establish"),(""," that")],20),
           txt(12,224,"the method can fully replace",20,font=SERIF),
           txt(12,250,"conventional methods.",20,font=SERIF), line(12,278,388,278)]
    else:
        w,h=920,208
        c=[line(20,11,900,11),line(20,197,900,197)]
        for x, tag, color, lines in [
            (30,"Original","soft",[[("delete","Of course,"),(""," these results do not")],
                                  [("","establish that the method can fully")],[("","replace conventional methods.")]]),
            (489,"Edited","violet",[[("","These results "),("keep","do not establish")],
                                    [("","that the method can fully replace")],[("","conventional methods.")]])]:
            c.append(txt(x,50,tag,19,color,SERIF,'font-style="italic"'))
            for j,words in enumerate(lines):
                c.append(wording(x,92+j*34,words,24))
        c.append(path("M434 115q10-3 23-1m-6-4 6 4-6 4","graph",1.1))
    plate("proof-mobile.svg" if mobile else "proof.svg",w,h,"Original and edited manuscript excerpt",
          "Of course is deleted. Do not establish is retained: the result does not establish full replacement.",c)


def numbers(mobile,zh):
    w,h=(400,168) if mobile else (920,185)
    margin=12 if mobile else 30
    c=[txt(margin,27 if mobile else 36,"测试队列中的准确率" if zh else "Accuracy in the test cohort",
           16 if mobile else 19,"soft",SERIF)]
    for i,(model,value) in enumerate([("所提方法" if zh else "Proposed method",87.4),
                                      ("基线模型" if zh else "Baseline model",81.2)]):
        x=(12+201*i) if mobile else (30+454*i)
        baseline=84 if mobile else 105
        c += [txt(x,baseline,f"{value:.1f}%",43 if mobile else 59,"violet" if i==0 else "ink",SERIF),
              txt(x+2,baseline+(25 if mobile else 29),model,16 if mobile else 19,"soft")]
        length=160 if mobile else 358
        y=139 if mobile else 163
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
    if mobile:
        w,h=400,176
        c=[]
        for idx,(condition,en,action,eng) in enumerate(data):
            y=37+51*idx
            c += [path(f"M12 88C30 88 23 {y} 49 {y}","graph"),
                  dot(50,y,2.8,"graph",True),
                  txt(64,y+6,condition if zh else en,17,"soft"),
                  txt(242 if not zh else 233,y+7,action if zh else eng,19,"violet",SERIF)]
    else:
        w,h=920,185
        c=[txt(29,98,"编辑判断" if zh else "Editorial judgement",24,"ink",SERIF,'font-style="normal"' if zh else 'font-style="italic"')]
        for idx,(condition,en,action,eng) in enumerate(data):
            y=39+54*idx
            c += [path(f"M252 92C303 92 289 {y} 344 {y}","graph",1.2),
                  dot(345,y,3.4,"graph",True),
                  txt(368,y+6,condition if zh else en,20,"soft"),
                  line(549,y,590,y,"hair"),txt(615,y+9,action if zh else eng,26,"violet",SERIF)]
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
