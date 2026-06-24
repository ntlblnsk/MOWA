#!/usr/bin/env python3

import argparse
import shutil
from pathlib import Path

from PIL import Image


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="Ścieżka do folderu źródłowego")
    args = parser.parse_args()

    src_dir = Path(args.src).resolve()

    if not src_dir.is_dir():
        raise ValueError(f"Folder nie istnieje: {src_dir}")

    input_dir = src_dir / "input"
    gt_dir = src_dir / "gt"
    mask_dir = src_dir / "mask"

    input_dir.mkdir(exist_ok=True)
    gt_dir.mkdir(exist_ok=True)
    mask_dir.mkdir(exist_ok=True)

    images = [
        p for p in src_dir.iterdir()
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    ]

    for image_path in images:
        input_path = input_dir / image_path.name
        gt_path = gt_dir / image_path.name
        mask_path = mask_dir / image_path.name

        with Image.open(image_path) as img:
            width, height = img.size

        # przenieś do input
        shutil.move(str(image_path), str(input_path))

        # skopiuj do gt
        shutil.copy2(input_path, gt_path)

        # utwórz białą maskę
        mask = Image.new("L", (width, height), 255)
        mask.save(mask_path)

        print(f"Przetworzono: {image_path.name}")

    print(f"\nGotowe. Przetworzono {len(images)} plików.")


if __name__ == "__main__":
    main()