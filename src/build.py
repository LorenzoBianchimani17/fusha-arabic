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
<meta name="description" content="Modern Standard Arabic for beginners: thirty lessons, conversations you can hold out loud, no alphabet required.">
<meta name="theme-color" content="#F3F0E8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1417" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Fusha">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%97%A3%EF%B8%8F%3C/text%3E%3C/svg%3E">
<link rel="apple-touch-icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAIAAACyr5FlAAADGklEQVR42u3dIW5bURCG0cu9sKwkNFso8ApiHNLSUCPLxKBSNxRSFdQKrKKokf3enX/ekb4FjO49eGbsnr5JHzY8geAQHIJDcAgOwSE4BIfgEBwSHIJDcAgOwSE4BIfgEByCQ4JDcAgOwfFPD88vxYNjTt9//vrz+6141yHhIKOhj0EGH31wxMnI9THI4KMDjmgZiT4GGXxk42gjI8vHIIOPVBz/L+NwvuyPp+ldx2jjY/SQ8fjjtc7Y12F6+Bhk8BGGI1pGGx+DDD5icLSR0cDHIIOPABwtZUT7GGTwURpHexmhPgYZfBTFsSkZcT4GGXyUw7FZGUE+Bhl8FMJBRoqPQQYfJXCQkeVjkMHHZBxkJPoYZPAxDQcZuT4GGXxMwEFGuo9BBh+r4iCjh49BBh8r4SCjk4974nh4fiFjro/77i+cgIOM5Xxk4yBjUR/BOMhY2kcqjsP54ndv7/P9H6k49seTr7296zPCITgEBxxwwAEHHHDAAQcccMABBxxwwAEHHIJDcPhdOOCAAw444IADDjjggAMOOOCAAw7BITgEBxxwwAEHHHDAAQcccMABBxxwwAEHHIJDcMABBxxwwAEHHHDAAQcccMABBxxwwCE4tG0cFuPfpZ6L8Z3UuL22JzX4WFqGM15ktMbBx0IySuPYOR06VUbp06F8dJKxc66cjLVx8NFAxoI4+EiXsSwOPqJlLI6Dj1wZa+DgI1TGSjj4SJSxHg4+4mSsioOPLBlr4+AjSMYEHHykyJiDg48IGdNw8FFfxkwcW/YRIWMyjm36SJExH8fWfATJKIFjOz6yZFTBsQUfcTIK4ejtI1FGLRxdfYTKKIejn49cGRVxdPIRLaMojh4+0mXUxZHuo4GM0jhyffSQUR3Hl3wczpf98TS9z/dnBMkIwPElH0HVl5GBo5+PCBkxODr5SJGRhKOHjyAZYTjSfWTJyMOR6yNORiSORB+JMlJxZPkIlRGMI8VHroxsHLv3/YXFi37ebByCQ3AIDsEhOASH4JDgEByCQ3AIDsEhOASH4BAcEhyCQ3AIDsEhOASH4voLrhwYQb+D7KcAAAAASUVORK5CYII=">
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
