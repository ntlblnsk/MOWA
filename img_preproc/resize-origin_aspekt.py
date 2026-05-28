from pathlib import Path
from PIL import Image, ImageOps
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--src",
    type=str,
    default="/mnt/mowa/pictures/pictures-dist/ultrawide/original/0",
    help="Folder ze zdjęciami wejściowymi"
)

parser.add_argument(
    "--dst",
    type=str,
    default="/mnt/mowa/pictures/pictures-dist/ultrawide/preprocessing/resize-origin_aspekt",
    help="Folder wynikowy"
)

parser.add_argument(
    "--min_side",
    type=int,
    default=256,
    help="Docelowy rozmiar krótszego boku"
)

args = parser.parse_args()

src_dir = Path(args.src)
dst_dir = Path(args.dst)

dst_dir.mkdir(parents=True, exist_ok=True)

extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}

files = sorted(
    f for f in src_dir.iterdir()
    if f.is_file() and f.suffix.lower() in extensions
)

for file in files:
    try:
        with Image.open(file) as img:
            # popraw orientację z EXIF
            img = ImageOps.exif_transpose(img)

            width, height = img.size

            # wyliczenie nowego rozmiaru
            if width < height:
                new_width = args.min_side
                new_height = round(height * (args.min_side / width))
            else:
                new_height = args.min_side
                new_width = round(width * (args.min_side / height))

            resized = img.resize(
                (new_width, new_height),
                Image.LANCZOS
            )

            output_path = dst_dir / file.name
            resized.save(output_path)

            print(
                f"{file.name}: "
                f"{width}x{height} -> "
                f"{new_width}x{new_height}"
            )

    except Exception as e:
        print(f"Błąd dla {file.name}: {e}")