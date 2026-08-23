# Wraps fusha.html in the head the artifact host supplies for itself, and
# writes the result as index.html at the root of the repository, which is
# what GitHub Pages serves.
import pathlib

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Modern Standard Arabic for beginners: twenty-nine lessons, conversations you can hold out loud, no alphabet required.">
<meta name="theme-color" content="#0B6E7F" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1417" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Fusha">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%97%A3%EF%B8%8F%3C/text%3E%3C/svg%3E">
<link rel="manifest" href="manifest.webmanifest">
<title>Fusha - Modern Standard Arabic for beginners</title>
<style>
  html { -webkit-text-size-adjust: 100%; }
  body { margin: 0; }
</style>
</head>
<body>
"""

src = (HERE / "fusha.html").read_text(encoding="utf-8")
body = src.split("</title>", 1)[1].lstrip("\n")
(ROOT / "index.html").write_text(HEAD + body + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html written from src/fusha.html")
