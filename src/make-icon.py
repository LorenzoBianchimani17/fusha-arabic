# Draws the home-screen icon: the app's own octagon, white on the teal,
# supersampled so the edges stay clean at every size iOS asks for.
# Writes icon.png and icon.b64; build.py inlines the base64 in the head.
import zlib, struct, math, base64, pathlib

S, SS = 180, 4
W = S * SS
BG = (11, 110, 127)
FG = (252, 250, 245)
cx = cy = W / 2
R = W * 0.33
STROKE = W * 0.055

def edge(x, y):
    dx, dy = abs(x - cx), abs(y - cy)
    return max(max(dx, dy), (dx + dy) * math.sqrt(0.5)) - R

rows = []
for py in range(S):
    row = bytearray([0])
    for px in range(S):
        r = g = b = 0
        for sy in range(SS):
            for sx in range(SS):
                c = FG if abs(edge(px * SS + sx + .5, py * SS + sy + .5)) <= STROKE / 2 else BG
                r += c[0]; g += c[1]; b += c[2]
        n = SS * SS
        row += bytes((r // n, g // n, b // n))
    rows.append(bytes(row))

def chunk(tag, data):
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff)

png = (b"\x89PNG\r\n\x1a\n" +
       chunk(b"IHDR", struct.pack(">IIBBBBB", S, S, 8, 2, 0, 0, 0)) +
       chunk(b"IDAT", zlib.compress(b"".join(rows), 9)) +
       chunk(b"IEND", b""))

here = pathlib.Path(__file__).parent
(here / "icon.png").write_bytes(png)
(here / "icon.b64").write_text(base64.b64encode(png).decode())
print("icon.png written, %d bytes" % len(png))
