from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).parent
pages = sorted(root.glob("page-*.jpg"))
thumb_w, thumb_h = 384, 216
cols, rows = 4, 3
for sheet_index in range(0, len(pages), cols * rows):
    group = pages[sheet_index:sheet_index + cols * rows]
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + 22)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(group):
        with Image.open(path) as src:
            thumb = src.convert("RGB").resize((thumb_w, thumb_h))
        x = (i % cols) * thumb_w
        y = (i // cols) * (thumb_h + 22)
        sheet.paste(thumb, (x, y))
        page_no = sheet_index + i + 1
        draw.text((x + 6, y + thumb_h + 3), f"PDF page {page_no}", fill="black")
    out = root / f"contact-{sheet_index // (cols * rows) + 1:02d}.jpg"
    sheet.save(out, quality=88)
