#!/usr/bin/env python3
import argparse
from pathlib import Path

import cv2
import numpy as np


def create_inscribed_circle_mask(img, shrink=3):
    h, w = img.shape[:2]

    mask = np.zeros((h, w), dtype=np.uint8)

    cx = w // 2
    cy = h // 2

    radius = min(w, h) // 2 - shrink
    radius = max(radius, 1)

    cv2.circle(
        mask,
        center=(cx, cy),
        radius=radius,
        color=255,
        thickness=-1
    )

    return mask


def process_image(src_path, dst_path, shrink):
    img = cv2.imread(str(src_path), cv2.IMREAD_COLOR)

    if img is None:
        print(f"Pominięto, nie można wczytać: {src_path}")
        return

    mask = create_inscribed_circle_mask(img, shrink=shrink)
    cv2.imwrite(str(dst_path), mask)

    print(f"Zapisano: {dst_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="Folder ze zdjęciami")
    parser.add_argument("dst", help="Folder wyjściowy z maskami")
    parser.add_argument(
        "--shrink",
        type=int,
        default=3,
        help="O ile pikseli zmniejszyć promień koła, domyślnie 3"
    )
    args = parser.parse_args()

    src_dir = Path(args.src)
    dst_dir = Path(args.dst)
    dst_dir.mkdir(parents=True, exist_ok=True)

    exts = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

    for src_path in sorted(src_dir.iterdir()):
        if src_path.suffix.lower() not in exts:
            continue

        dst_path = dst_dir / f"{src_path.stem}.png"
        process_image(src_path, dst_path, shrink=args.shrink)


if __name__ == "__main__":
    main()