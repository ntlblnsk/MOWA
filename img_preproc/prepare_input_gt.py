from pathlib import Path
import shutil
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--src",
    type=str,
    default="/mnt/mowa/pictures/pictures-dist/ultrawide/preprocessing/resize-origin_aspekt",
    help="Folder źródłowy ze zdjęciami"
)

parser.add_argument(
    "--copy2gt",
    action="store_true",
    help="Skopiuj zdjęcia również do folderu gt"
)

args = parser.parse_args()

src_dir = Path(args.src)

input_dir = src_dir / "input"
gt_dir = src_dir / "gt"

input_dir.mkdir(parents=True, exist_ok=True)

if args.copy2gt:
    gt_dir.mkdir(parents=True, exist_ok=True)

extensions = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
    ".webp"
}

files = sorted(
    f for f in src_dir.iterdir()
    if (
        f.is_file()
        and f.suffix.lower() in extensions
    )
)

for file in files:
    dst_input = input_dir / file.name

    # przeniesienie do input
    shutil.move(str(file), str(dst_input))
    print(f"[MOVE -> INPUT] {file.name}")

    # opcjonalne kopiowanie do gt
    if args.copy2gt:
        dst_gt = gt_dir / file.name
        shutil.copy2(dst_input, dst_gt)
        print(f"[COPY -> GT]    {file.name}")

print("\nGotowe.")