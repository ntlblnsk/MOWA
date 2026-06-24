from pathlib import Path
from PIL import Image, ImageOps
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--src", type=str, default="/home/natal/code/pictures-dist/original/",
                    help="Folder ze zdjęciami wejściowymi")
parser.add_argument("--dst", type=str, default="/home/natal/code/pictures-dist/resized512/",
                    help="Folder wynikowy")
parser.add_argument("--size", type=int, default=512,
                    help="Rozmiar wynikowego kwadratu")
parser.add_argument("--fix_orientation", action="store_true",
                    help="Popraw orientację zdjęć na podstawie EXIF")

args = parser.parse_args()

src_dir = Path(args.src)
dst_dir = Path(args.dst)
dst_dir.mkdir(parents=True, exist_ok=True)

extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

files = sorted(
    f for f in src_dir.iterdir()
    if f.is_file() and f.suffix.lower() in extensions
)

for file in files:
    try:
        with Image.open(file) as img:

            if args.fix_orientation:
                img = ImageOps.exif_transpose(img)

            img = img.resize(
                (args.size, args.size),
                Image.Resampling.LANCZOS
            )

            output_path = dst_dir / file.name

            if output_path.suffix.lower() in [".jpg", ".jpeg"]:
                img = img.convert("RGB")

            img.save(output_path)

            print(f"OK: {file.name}")

    except Exception as e:
        print(f"Błąd {file.name}: {e}")

print("Gotowe")