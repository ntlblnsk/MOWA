from pathlib import Path
from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--src",
    type=str,
    default="/home/ubuntu/pictures/pictures-dist/wide_n_makro/gt",
    help="Folder ze zdjęciami wejściowymi"
)

parser.add_argument(
    "--dsc",
    type=str,
    default="/home/ubuntu/pictures/pictures-dist/wide_n_makro/mask",
    help="Folder wyjściowy"
)

args = parser.parse_args()

src_dir = Path(args.src)
dsc_dir = Path(args.dsc)

dsc_dir.mkdir(parents=True, exist_ok=True)

extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}

files = sorted(
    f for f in src_dir.iterdir()
    if f.is_file() and f.suffix.lower() in extensions
)

for file in files:
    try:
        with Image.open(file) as img:
            width, height = img.size

            # Biała maska
            white_img = Image.new("RGB", (width, height), (255, 255, 255))

            out_path = dsc_dir / file.name
            white_img.save(out_path)

            print(f"Saved: {out_path}")

    except Exception as e:
        print(f"Error processing {file}: {e}")