#!/usr/bin/env python3
"""
Generate a print-quality QR code for your published site.

Usage:
    python3 make_qr.py https://your-site.netlify.app/app.html
    python3 make_qr.py https://your-site.netlify.app/app.html --label "Scan for the live tool"

Outputs  dvs_manager_qr.png  (2000 px, print-ready)  and  dvs_manager_qr.svg  (vector).
"""
import sys, argparse

def main():
    ap = argparse.ArgumentParser(description="QR code generator for the DVS Manager site")
    ap.add_argument("url", help="Full published URL, e.g. https://site.example/app.html")
    ap.add_argument("--out", default="dvs_manager_qr", help="Output filename stem")
    ap.add_argument("--label", default=None, help="Optional caption printed under the code")
    ap.add_argument("--px", type=int, default=2000, help="PNG size in pixels (default 2000)")
    a = ap.parse_args()

    if not a.url.startswith(("http://", "https://")):
        print("! Warning: a QR must encode a full URL starting with http:// or https://")
        print("  A file:// path or bare filename will not open on anyone else's phone.\n")

    try:
        import qrcode
        from qrcode.constants import ERROR_CORRECT_M
    except ImportError:
        sys.exit("Install the dependency first:  pip install qrcode pillow")

    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_M,
                       box_size=10, border=4)
    qr.add_data(a.url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#0b2754", back_color="white").convert("RGB")
    img = img.resize((a.px, a.px), 0)   # NEAREST keeps modules crisp

    if a.label:
        from PIL import Image, ImageDraw, ImageFont
        pad = int(a.px * 0.09)
        canvas = Image.new("RGB", (a.px, a.px + pad), "white")
        canvas.paste(img, (0, 0))
        d = ImageDraw.Draw(canvas)
        size = int(pad * 0.42)
        try:
            f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        except Exception:
            f = ImageFont.load_default()
        w = d.textbbox((0, 0), a.label, font=f)[2]
        d.text(((a.px - w) / 2, a.px + pad * 0.20), a.label, font=f, fill="#0b2754")
        img = canvas

    png = f"{a.out}.png"
    img.save(png)

    # vector version
    m = qr.get_matrix()
    n = len(m); q = 4; total = n + 2 * q
    path = "".join(f"M{c+q} {r+q}h1v1h-1z"
                   for r in range(n) for c in range(n) if m[r][c])
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total} {total}" '
           f'width="1000" height="1000" shape-rendering="crispEdges">'
           f'<rect width="{total}" height="{total}" fill="#fff"/>'
           f'<path d="{path}" fill="#0b2754"/></svg>')
    svgf = f"{a.out}.svg"
    open(svgf, "w").write(svg)

    print(f"URL encoded : {a.url}")
    print(f"PNG written : {png}  ({a.px}×{a.px})")
    print(f"SVG written : {svgf}  (vector — best for print)")

if __name__ == "__main__":
    main()
