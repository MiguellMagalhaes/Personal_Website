from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


files = sorted(Path("tmp/pdfs/rumos_helpdesk_render").glob("page-*.png"))
out = Path("tmp/pdfs/rumos_helpdesk_contact")
out.mkdir(exist_ok=True)

thumb_width = 430
padding = 18

for start in range(0, len(files), 4):
    items = []
    for path in files[start : start + 4]:
        image = Image.open(path).convert("RGB")
        height = round(image.height * thumb_width / image.width)
        image = image.resize((thumb_width, height))
        image = ImageOps.expand(image, border=2, fill=(120, 130, 145))
        items.append((path, image))

    thumb_height = max(image.height for _, image in items)
    canvas = Image.new(
        "RGB",
        (thumb_width * 2 + padding * 3, thumb_height * 2 + padding * 3 + 24),
        (225, 230, 236),
    )
    draw = ImageDraw.Draw(canvas)
    for index, (path, image) in enumerate(items):
        x = padding + (index % 2) * (thumb_width + padding)
        y = padding + (index // 2) * (thumb_height + padding + 12)
        canvas.paste(image, (x, y))
        draw.text((x, y + image.height + 2), path.stem, fill=(20, 30, 45))

    canvas.save(out / f"contact-{start // 4 + 1}.png")
