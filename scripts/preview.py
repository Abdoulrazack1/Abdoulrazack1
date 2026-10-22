"""Aperçu local du README tel que GitHub le rend (clair et sombre).

    python scripts/preview.py <dossier-de-sortie>
Rend le Markdown via l'API GitHub (`gh api markdown`), puis capture la page avec Chrome headless.
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out = sys.argv[1]

md = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
html = subprocess.check_output(
    ["gh", "api", "markdown", "-f", "mode=gfm", "-f", f"context=Abdoulrazack1/Abdoulrazack1", "-f", f"text={md}"],
    text=True, encoding="utf-8",
)
assets = "file:///" + os.path.join(ROOT, "assets").replace("\\", "/") + "/"
html = html.replace('src="./assets/', f'src="{assets}').replace('src="assets/', f'src="{assets}')

for theme, bg, fg, link in [("light", "#ffffff", "#1f2328", "#0969da"), ("dark", "#0d1117", "#e6edf3", "#4493f8")]:
    page = f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;background:{bg};color:{fg};font:16px/1.5 -apple-system,'Segoe UI',Helvetica,Arial,sans-serif}}
article{{max-width:880px;margin:24px auto;padding:0 24px}} a{{color:{link}}} img{{max-width:100%}} p{{margin:0 0 16px}}
</style><article>{html}</article>"""
    path = os.path.join(out, f"readme-{theme}.html")
    open(path, "w", encoding="utf-8").write(page)
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
         "--virtual-time-budget=12000", "--window-size=930,3900", f"--screenshot={os.path.join(out, f'readme-{theme}.png')}",
         "file:///" + path.replace("\\", "/")],
        capture_output=True,
    )
    print("capture", theme)
