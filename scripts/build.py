"""Génère les visuels SVG du profil GitHub, dans l'identité du portfolio.

    python scripts/build.py            # tous les visuels
    python scripts/build.py --stats    # seulement la carte de statistiques (tâche quotidienne)

Statistiques : API GraphQL GitHub, jeton lu dans GITHUB_TOKEN (ou `gh auth token` en local).
Police : Bricolage Grotesque, réduite aux caractères utilisés puis embarquée dans chaque SVG
(GitHub affiche les SVG comme des images : aucune ressource externe n'est chargée).
"""

import base64
import io
import json
import math
import os
import random
import subprocess
import sys
import urllib.request
from html import escape

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "scripts", "src")
OUT = os.path.join(ROOT, "assets")
LOGIN = "Abdoulrazack1"

NIGHT, NIGHT2, NIGHT3 = "#0a0b1d", "#15172f", "#1d2050"
CREAM, CREAM2 = "#f1efe8", "rgba(241,239,232,.68)"
COBALT, SUN, CORAL, PINK, MINT, LAV = "#2a3bff", "#ffd23f", "#ff5c39", "#ff9ad5", "#12d6a0", "#b8b2ff"
INK = "#14152b"

# ---------------------------------------------------------------- police

_CHARS = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    " .,;:!?'’«»()[]/·–-+%&@#*=<>_|~^\"àâäçéèêëîïôöùûüÿœæÀÂÇÉÈÊËÎÏÔÖÙÛÜŒ…→↗✓"
)


def font_face():
    """Police réduite aux caractères du site, en base64 (≈ 20 Ko au lieu de 77)."""
    from fontTools.varLib import instancer

    font = TTFont(os.path.join(SRC, "bricolage.woff2"))
    # Taille optique figée (titres) et graisses utiles seulement : le fichier fond de moitié.
    font = instancer.instantiateVariableFont(font, {"opsz": 72, "wght": (500, 800)})
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["kern", "liga", "calt"]
    sub = subset.Subsetter(opts)
    sub.populate(text=_CHARS)
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    data = base64.b64encode(buf.getvalue()).decode()
    return (
        "@font-face{font-family:B;src:url(data:font/woff2;base64,%s) format('woff2');font-weight:100 900}" % data
    )


FONT = None


def svg(w, h, body, css="", title=""):
    global FONT
    if FONT is None:
        FONT = font_face()
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
        f"<title>{escape(title)}</title>"
        f"<style>{FONT}text{{font-family:B,'Segoe UI',sans-serif}}{css}"
        "@media (prefers-reduced-motion:reduce){*{animation:none!important}}</style>"
        f"{body}</svg>"
    )


def save(name, content):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"{name:28s} {len(content) // 1024:4d} Ko")


def img_data(name):
    with open(os.path.join(SRC, name), "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()


def wrap(text, size, width):
    """Coupe un texte en lignes selon une largeur approximative (≈ 0,52 em par caractère)."""
    max_chars = max(8, int(width / (size * 0.5)))
    lines, cur = [], ""
    for word in text.split():
        if len(cur) + len(word) + 1 > max_chars and cur:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    if cur:
        lines.append(cur)
    return lines


def text_lines(x, y, lines, size, lh, fill, weight=500, extra=""):
    out = []
    for i, line in enumerate(lines):
        out.append(
            f'<text x="{x}" y="{y + i * lh}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{escape(line)}</text>'
        )
    return "".join(out)


def mark(x, y, s):
    """Signature graphique de la bannière : quart de disque, disque, quart inversé, carré percé."""
    u = s / 2
    return (
        f'<g transform="translate({x},{y})">'
        f'<path d="M0 0h{u}v{u}A{u} {u} 0 0 1 0 0z" fill="{SUN}"/>'
        f'<circle cx="{u * 1.5}" cy="{u / 2}" r="{u / 2}" fill="{CORAL}"/>'
        f'<path d="M0 {u * 2}V{u}a{u} {u} 0 0 1 {u} {u}z" fill="{PINK}"/>'
        f'<path fill-rule="evenodd" d="M{u} {u}h{u}v{u}h-{u}zM{u * 1.5} {u * 1.25}a{u / 4} {u / 4} 0 1 0 0 {u / 2}a{u / 4} {u / 4} 0 1 0 0-{u / 2}z" fill="{MINT}"/>'
        "</g>"
    )


def galaxy(cx, cy, R, n, seed=7, tilt=0.34, skew=-0.38):
    """Galaxie spirale figée (même formule que le site), en trois groupes qui scintillent."""
    rnd = random.Random(seed)
    colors = ["#8e99ff", PINK, SUN, "#ffffff", "#5b68ff"]
    groups = {0: [], 1: [], 2: []}
    for i in range(n):
        t = rnd.random() ** 0.6
        r = 0.04 + t * 0.96
        sp = (rnd.random() - 0.5) * (0.5 - t * 0.28)
        a = (i % 2) * math.pi + r * 5.2 + sp * 2.4
        x, z = math.cos(a) * r * R, math.sin(a) * r * R
        px = cx + x * math.cos(skew) - z * tilt * math.sin(skew)
        py = cy + x * math.sin(skew) + z * tilt * math.cos(skew)
        size = 2.2 if rnd.random() < 0.07 else 1.4 if rnd.random() < 0.45 else 0.9
        col = colors[0] if rnd.random() < 0.55 else rnd.choice(colors)
        op = round((0.45 + rnd.random() * 0.55) * (1 - r * 0.3), 2)
        groups[i % 3].append(f'<rect x="{px:.1f}" y="{py:.1f}" width="{size}" height="{size}" fill="{col}" opacity="{op}"/>')
    return "".join(f'<g class="tw tw{k}">{"".join(v)}</g>' for k, v in groups.items())


TWINKLE = (
    "@keyframes tw{0%,100%{opacity:1}50%{opacity:.35}}"
    ".tw{animation:tw 4s ease-in-out infinite}.tw1{animation-delay:-1.3s}.tw2{animation-delay:-2.6s}"
    "@keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}"
    ".up{animation:up .9s cubic-bezier(.22,1,.36,1) both}.d1{animation-delay:.12s}.d2{animation-delay:.24s}.d3{animation-delay:.36s}"
)

# ---------------------------------------------------------------- bannière


def header():
    w, h = 1280, 460
    body = f"""
<defs>
  <radialGradient id="g1" cx="72%" cy="45%" r="55%"><stop offset="0" stop-color="{COBALT}" stop-opacity=".42"/><stop offset="1" stop-color="{COBALT}" stop-opacity="0"/></radialGradient>
  <radialGradient id="g2" cx="8%" cy="0%" r="40%"><stop offset="0" stop-color="{PINK}" stop-opacity=".16"/><stop offset="1" stop-color="{PINK}" stop-opacity="0"/></radialGradient>
  <clipPath id="c"><rect width="{w}" height="{h}" rx="28"/></clipPath>
</defs>
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="{NIGHT}"/><rect width="{w}" height="{h}" fill="url(#g1)"/><rect width="{w}" height="{h}" fill="url(#g2)"/>
  {galaxy(930, 240, 400, 2600)}
  <g transform="translate(64 64)">
    <path d="M0 0h18v18A18 18 0 0 1 0 0z" fill="{SUN}"/><circle cx="24" cy="24" r="9" fill="{PINK}"/>
    <text x="48" y="25" font-size="21" font-weight="750" fill="{CREAM}" letter-spacing="-.4">Abdoulrazack Abdillahi</text>
  </g>
  <text class="up" x="64" y="178" font-size="15" font-weight="700" fill="{CREAM2}" letter-spacing="2.6">DÉVELOPPEUR FULL-STACK · LILLE</text>
  <text class="up d1" x="60" y="262" font-size="78" font-weight="650" fill="{CREAM}" letter-spacing="-3.4">Je code des applis</text>
  <text class="up d2" x="60" y="346" font-size="78" font-weight="650" fill="{CREAM}" letter-spacing="-3.4">qui servent <tspan fill="{PINK}">vraiment.</tspan></text>
  <g class="up d3">
    <rect x="64" y="384" width="236" height="40" rx="10" fill="{CREAM}"/>
    <text x="84" y="410" font-size="16" font-weight="700" fill="{INK}">abdoulrazack1.github.io ↗</text>
    <text x="322" y="410" font-size="16" font-weight="600" fill="{CREAM2}">Node.js · NestJS · React · PHP · SQL</text>
  </g>
</g>"""
    save("header.svg", svg(w, h, body, TWINKLE, "Abdoulrazack Abdillahi · Je code des applis qui servent vraiment."))


# ---------------------------------------------------------------- bento « en ce moment »


def tile(x, y, w, h, fill, inner, stroke=True):
    s = ' stroke="rgba(255,255,255,.08)"' if stroke else ""
    return f'<g transform="translate({x} {y})"><rect width="{w}" height="{h}" rx="24" fill="{fill}"{s}/>{inner}</g>'


def now():
    w, h = 1280, 400
    portrait = img_data("portrait.jpg")
    t1 = tile(0, 0, 500, 400, NIGHT2, f"""
  <defs><clipPath id="av"><circle cx="76" cy="84" r="44"/></clipPath></defs>
  <circle cx="76" cy="84" r="47" fill="{PINK}"/>
  <image href="{portrait}" x="32" y="30" width="88" height="117" clip-path="url(#av)" preserveAspectRatio="xMidYMin slice"/>
  <text x="32" y="186" font-size="34" font-weight="700" fill="{CREAM}" letter-spacing="-1">Salut, moi c’est</text>
  <text x="32" y="224" font-size="34" font-weight="700" fill="{CREAM}" letter-spacing="-1">Abdoulrazack.</text>
  {text_lines(32, 268, wrap("L’économie d’abord, le code ensuite. Avant d’écrire une ligne, je me demande à quoi l’outil va servir, et à qui.", 18, 430), 18, 27, CREAM2)}
""")
    t2 = tile(516, 0, 372, 192, LAV, f"""
  {mark(268, 94, 84)}
  <text x="28" y="54" font-size="25" font-weight="750" fill="{INK}" letter-spacing="-.6">De l’économie au code</text>
  {text_lines(28, 88, wrap("Licence et master à Lille, puis titre Développeur Web et Web Mobile.", 16, 200), 16, 23, "rgba(20,21,43,.78)")}
""", False)
    t3 = tile(904, 0, 376, 192, "#10261f", f"""
  <text x="28" y="54" font-size="25" font-weight="750" fill="{CREAM}" letter-spacing="-.6">En ce moment</text>
  {text_lines(28, 88, wrap("Je refais le site de Bobo et Gamelles, du front-end au déploiement, en bénévole.", 16, 320), 16, 23, CREAM2)}
  <g transform="translate(28 150)"><rect width="88" height="30" rx="9" fill="rgba(255,255,255,.08)"/><text x="16" y="20" font-size="13" font-weight="700" fill="{CREAM}">refonte</text>
  <rect x="96" width="34" height="2" y="14" fill="rgba(255,255,255,.25)"/><rect x="138" width="44" height="30" rx="9" fill="{MINT}"/><text x="152" y="20" font-size="13" font-weight="700" fill="#0c2a21">CI</text>
  <rect x="190" width="34" height="2" y="14" fill="rgba(255,255,255,.25)"/><rect x="232" width="84" height="30" rx="9" fill="rgba(255,255,255,.08)"/><text x="248" y="20" font-size="13" font-weight="700" fill="{CREAM}">en ligne</text></g>
""")
    chips = "".join(
        f'<rect x="{x}" y="0" width="{wd}" height="32" rx="16" fill="{INK}"/><text x="{x + 16}" y="21" font-size="14" font-weight="700" fill="{SUN}">{t}</text>'
        for x, wd, t in [(0, 104, "Alternance"), (114, 58, "CDI"), (182, 82, "Missions")]
    )
    t4 = tile(516, 208, 764, 192, SUN, f"""
  <text x="28" y="54" font-size="25" font-weight="750" fill="{INK}" letter-spacing="-.6">Disponible</text>
  {text_lines(28, 88, wrap("Je cherche une alternance de 18 mois en Concepteur Développeur d’Applications, spécialisation éco-conception, à Lille ou en Île-de-France. Ouvert aux CDI, CDD et missions.", 16, 470), 16, 23, "rgba(20,21,43,.8)")}
  <g transform="translate(470 136)">{chips}</g>
""", False)
    save("now.svg", svg(w, h, t1 + t2 + t3 + t4, "", "Qui je suis, ce que je fais en ce moment, ma disponibilité"))


# ---------------------------------------------------------------- titres de section


def section(name, title, accent, shape):
    w, h = 1280, 96
    shapes = {
        "quarter": f'<path d="M0 0h30v30A30 30 0 0 1 0 0z" fill="{accent}"/>',
        "circle": f'<circle cx="15" cy="15" r="15" fill="{accent}"/>',
        "arch": f'<path d="M0 30V0a30 30 0 0 1 30 30z" fill="{accent}"/>',
        "square": f'<rect width="30" height="30" rx="4" fill="{accent}"/>',
    }
    body = f"""
<g transform="translate(4 30)">{shapes[shape]}</g>
<text x="52" y="60" font-size="44" font-weight="700" fill="#8b8fb3" letter-spacing="-1.6" class="t">{escape(title)}</text>
<rect x="52" y="80" width="1224" height="1.5" fill="#8b8fb3" opacity=".25"/>"""
    save(f"title-{name}.svg", svg(w, h, body, "", title))


# ---------------------------------------------------------------- cartes projets

PROJECTS = [
    dict(slug="cycling", name="C.C. Salouël", img="cycling-1.jpg", bg="#0b3a33", fg="#e9fff8", fg2="#a6d3c6", acc="#2fe0b6",
         line="L’outil de gestion d’un club cycliste de 100 membres, livré seul et toujours en service.",
         stack=["Node.js", "Express", "MySQL", "Leaflet"], status="Club réel"),
    dict(slug="cabinet", name="Cabinet d’avocats", img="cabinet-1.jpg", bg="#11221b", fg="#efe8d8", fg2="#b5ae9c", acc="#d1ad66",
         line="La plateforme d’un vrai cabinet : le secret professionnel garanti par PostgreSQL.",
         stack=["NestJS", "PostgreSQL", "RLS", "Next.js"], status="Client · code privé"),
    dict(slug="tsundoku", name="Tsundoku", img="tsundoku-1.jpg", bg="#f3ede1", fg="#1c1915", fg2="#5f574b", acc="#d8432b",
         line="Mon blog de chroniques manga, de la direction artistique au serveur en production.",
         stack=["Node.js", "MySQL", "Anilist", "Edge-TTS"], status="En ligne"),
    dict(slug="inko", name="Inko", img="inko-1.jpg", bg="#190f3d", fg="#f4efff", fg2="#b8acdf", acc="#b48dff",
         line="Un lecteur de manga qui marche hors connexion et s’installe sur Android.",
         stack=["JavaScript", "PWA", "Service Worker"], status="En ligne"),
    dict(slug="galactic-brain", name="Galactic Brain", img="galactic-1.jpg", bg="#0c0a2a", fg="#ecebff", fg2="#a9a6d6", acc="#9b8cff",
         line="Un serveur MCP qui donne une mémoire à Claude : 49 outils, 2 dépendances.",
         stack=["Node.js", "MCP", "BM25"], status="Open source"),
    dict(slug="inkstudio", name="InkStudio", img="inkstudio-1.jpg", bg="#fbfbf7", fg="#18204f", fg2="#4f567f", acc="#3a5bd9",
         line="Un studio d’animation tableau blanc où les dessins se calent sur la voix off.",
         stack=["JavaScript", "WebCodecs", "Electron"], status="Open source"),
    dict(slug="js-ranker", name="Js-Ranker", img="js-ranker-1.jpg", bg="#1a1008", fg="#fff3e4", fg2="#cdb79c", acc="#ffb24a",
         line="Un modèle qui note la qualité d’un code JavaScript et peut bloquer une CI.",
         stack=["TensorFlow.js", "AST", "GitHub Actions"], status="Open source"),
    dict(slug="logic-lens", name="Logic-Lens", img="logic-lens-1.jpg", bg="#0b1a4a", fg="#e9f0ff", fg2="#a5b6e4", acc="#73a6ff",
         line="Une IA qui reconnaît la formule derrière une fonction, et sait dire « je ne sais pas ».",
         stack=["TensorFlow.js", "Transformer", "AST"], status="Open source"),
]


def card(p):
    w, h = 632, 400
    shot = img_data(p["img"])
    light = p["bg"] in ("#f3ede1", "#fbfbf7")
    on_acc = "#ffffff" if light else p["bg"]
    lines = wrap(p["line"], 17, 262)
    chips, x = [], 0
    for s in p["stack"]:
        cw = int(len(s) * 7.6 + 26)
        chips.append(
            f'<rect x="{x}" y="0" width="{cw}" height="28" rx="14" fill="none" stroke="{p["fg2"]}" stroke-opacity=".45"/>'
            f'<text x="{x + 13}" y="19" font-size="13" font-weight="650" fill="{p["fg2"]}">{escape(s)}</text>'
        )
        x += cw + 8
    sw = int(len(p["status"]) * 7.8 + 30)
    body = f"""
<defs><clipPath id="c"><rect width="{w}" height="{h}" rx="26"/></clipPath>
<clipPath id="s"><rect x="0" y="0" width="420" height="300" rx="10"/></clipPath>
<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#000" flood-opacity=".35"/></filter></defs>
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="{p["bg"]}"/>
  <circle cx="{w - 40}" cy="40" r="150" fill="{p["acc"]}" opacity=".14"/>
  <g transform="translate(362 176) rotate(-4)" filter="url(#sh)">
    <rect x="-6" y="-24" width="432" height="330" rx="12" fill="{"#e9e5da" if light else "#24263f"}"/>
    <circle cx="8" cy="-12" r="3.5" fill="{CORAL}"/><circle cx="20" cy="-12" r="3.5" fill="{SUN}"/><circle cx="32" cy="-12" r="3.5" fill="{MINT}"/>
    <image href="{shot}" width="420" height="300" preserveAspectRatio="xMidYMin slice" clip-path="url(#s)"/>
  </g>
  <rect x="32" y="32" width="{sw}" height="30" rx="15" fill="{p["acc"]}"/>
  <text x="47" y="52" font-size="13.5" font-weight="750" fill="{on_acc}">{escape(p["status"])}</text>
  <text x="30" y="132" font-size="48" font-weight="750" fill="{p["fg"]}" letter-spacing="-2">{escape(p["name"])}</text>
  {text_lines(32, 172, lines, 17, 25, p["fg2"], 550)}
  <g transform="translate(32 {172 + len(lines) * 25 + 14})">{"".join(chips[:3])}</g>
  <text x="32" y="368" font-size="15" font-weight="750" fill="{p["acc"]}">Voir le projet ↗</text>
</g>"""
    save(f"project-{p['slug']}.svg", svg(w, h, body, "", f"{p['name']} : {p['line']}"))


# ---------------------------------------------------------------- statistiques

LANG_COLORS = [COBALT, PINK, SUN, MINT, CORAL, LAV]


def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t
    return subprocess.check_output(["gh", "auth", "token"], text=True).strip()


def gql(query):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"bearer {token()}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(data["errors"])
    return data["data"]


def stats():
    d = gql(
        """query{user(login:"%s"){
          createdAt
          repositories(ownerAffiliations:OWNER,privacy:PUBLIC,first:100,isFork:false){totalCount nodes{stargazerCount
            languages(first:10,orderBy:{field:SIZE,direction:DESC}){edges{size node{name}}}}}
          contributionsCollection{totalCommitContributions totalPullRequestContributions
            contributionCalendar{totalContributions weeks{contributionDays{contributionCount date}}}}}}"""
        % LOGIN
    )["user"]
    repos = d["repositories"]
    stars = sum(r["stargazerCount"] for r in repos["nodes"])
    langs = {}
    for r in repos["nodes"]:
        for e in r["languages"]["edges"]:
            langs[e["node"]["name"]] = langs.get(e["node"]["name"], 0) + e["size"]
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:5]
    cc = d["contributionsCollection"]
    weeks = cc["contributionCalendar"]["weeks"]
    days = [day for wk in weeks for day in wk["contributionDays"]]
    # Série de jours consécutifs avec au moins une contribution, la plus longue de l'année.
    best = cur = 0
    for day in days:
        cur = cur + 1 if day["contributionCount"] else 0
        best = max(best, cur)
    active = sum(1 for day in days if day["contributionCount"])

    w, h = 1280, 540
    figures = [
        (f"{cc['contributionCalendar']['totalContributions']:,}".replace(",", " "), "contributions", PINK),
        (f"{cc['totalCommitContributions']:,}".replace(",", " "), "commits", SUN),
        (str(repos["totalCount"]), "dépôts publics", MINT),
        (f"{best} j", "série record", LAV),
    ]
    fig = "".join(
        f'<g transform="translate({600 + i * 166} 0)"><text y="0" font-size="44" font-weight="750" fill="{c}" letter-spacing="-1.6">{v}</text>'
        f'<text y="28" font-size="14" font-weight="600" fill="{CREAM2}">{escape(l)}</text></g>'
        for i, (v, l, c) in enumerate(figures)
    )
    # Grille des contributions : 53 semaines × 7 jours, intensité en nuances de l'identité.
    mx = max((day["contributionCount"] for day in days), default=1) or 1
    scale = ["rgba(255,255,255,.06)", "#2b3577", "#3b4cff", "#8e99ff", PINK]
    cells = []
    for wi, wk in enumerate(weeks[-53:]):
        for di, day in enumerate(wk["contributionDays"]):
            n = day["contributionCount"]
            lvl = 0 if n == 0 else min(4, 1 + int(3 * n / mx + 0.5))
            cells.append((wi, di, scale[lvl]))
    grid = "".join(
        f'<rect x="{40 + wi * 22.7:.1f}" y="{214 + di * 22.7:.1f}" width="19" height="19" rx="4.5" fill="{col}"/>'
        for wi, di, col in cells
    )
    bar, x = [], 0
    legend = []
    for i, (name, size) in enumerate(top):
        pw = size / sum(s for _, s in top) * 1200
        bar.append(f'<rect x="{x:.1f}" y="0" width="{max(pw - 3, 2):.1f}" height="14" rx="4" fill="{LANG_COLORS[i]}"/>')
        legend.append(
            f'<g transform="translate({i * 240} 44)"><circle cx="6" cy="-5" r="6" fill="{LANG_COLORS[i]}"/>'
            f'<text x="20" y="0" font-size="16" font-weight="650" fill="{CREAM}">{escape(name)}</text>'
            f'<text x="20" y="22" font-size="14" font-weight="550" fill="{CREAM2}">{size / total * 100:.0f} %</text></g>'
        )
        x += pw
    body = f"""
<defs><clipPath id="c"><rect width="{w}" height="{h}" rx="28"/></clipPath>
<radialGradient id="g" cx="85%" cy="10%" r="60%"><stop offset="0" stop-color="{COBALT}" stop-opacity=".35"/><stop offset="1" stop-color="{COBALT}" stop-opacity="0"/></radialGradient></defs>
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="{NIGHT}"/><rect width="{w}" height="{h}" fill="url(#g)"/>
  <text x="40" y="62" font-size="15" font-weight="700" fill="{CREAM2}" letter-spacing="2.4">EN CHIFFRES</text>
  <text x="40" y="112" font-size="34" font-weight="700" fill="{CREAM}" letter-spacing="-1">{active} jours de code</text>
  <text x="40" y="146" font-size="34" font-weight="700" fill="{CREAM}" letter-spacing="-1">sur les 12 derniers mois.</text>
  <g transform="translate(0 110)">{fig}</g>
  <text x="40" y="198" font-size="14" font-weight="650" fill="{CREAM2}">Contributions sur l’année, semaine par semaine</text>
  {grid}
  <g transform="translate(40 418)">
    <text y="-14" font-size="14" font-weight="650" fill="{CREAM2}">Langages de mes dépôts publics</text>
    <g>{"".join(bar)}</g>{"".join(legend)}
  </g>
</g>"""
    save("stats.svg", svg(w, h, body, "", "Statistiques GitHub d’Abdoulrazack Abdillahi"))


# ---------------------------------------------------------------- pied de page


def footer():
    w, h = 1280, 360
    body = f"""
<defs><clipPath id="c"><rect width="{w}" height="{h}" rx="28"/></clipPath>
<radialGradient id="g" cx="78%" cy="45%" r="50%"><stop offset="0" stop-color="{COBALT}" stop-opacity=".4"/><stop offset="1" stop-color="{COBALT}" stop-opacity="0"/></radialGradient></defs>
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="{NIGHT}"/><rect width="{w}" height="{h}" fill="url(#g)"/>
  {galaxy(960, 190, 330, 1500, seed=11)}
  <text x="56" y="84" font-size="15" font-weight="700" fill="{CREAM2}" letter-spacing="2.4">CONTACT</text>
  <text x="52" y="160" font-size="58" font-weight="650" fill="{CREAM}" letter-spacing="-2.4">Construisons quelque chose</text>
  <text x="52" y="226" font-size="58" font-weight="650" fill="{CREAM}" letter-spacing="-2.4">qui sert <tspan fill="{PINK}">vraiment.</tspan></text>
  <text x="56" y="292" font-size="24" font-weight="650" fill="{CREAM}">abdoul.abdillahi@gmail.com</text>
  <rect x="56" y="304" width="330" height="3" fill="{SUN}"/>
</g>"""
    save("footer.svg", svg(w, h, body, TWINKLE, "Contact : abdoul.abdillahi@gmail.com"))


if __name__ == "__main__":
    if "--stats" in sys.argv:
        stats()
    else:
        header()
        now()
        section("projets", "Ce que j’ai construit", CORAL, "quarter")
        section("chiffres", "En chiffres", MINT, "circle")
        section("stack", "Ma boîte à outils", SUN, "arch")
        for p in PROJECTS:
            card(p)
        stats()
        footer()
