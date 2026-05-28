import argparse
import csv
import math
import random
from pathlib import Path
from PIL import Image, ImageOps


IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}


def largest_rotated_rect(w: int, h: int, angle_rad: float):
    if w <= 0 or h <= 0:
        return 0, 0

    width_is_longer = w >= h
    side_long = w if width_is_longer else h
    side_short = h if width_is_longer else w

    sin_a = abs(math.sin(angle_rad))
    cos_a = abs(math.cos(angle_rad))

    if side_short <= 2 * sin_a * cos_a * side_long:
        x = 0.5 * side_short
        wr = x / sin_a if sin_a != 0 else side_long
        hr = x / cos_a if cos_a != 0 else side_short
    else:
        cos_2a = cos_a * cos_a - sin_a * sin_a
        wr = (w * cos_a - h * sin_a) / cos_2a
        hr = (h * cos_a - w * sin_a) / cos_2a

    return int(abs(wr)), int(abs(hr))


def center_crop(img, crop_w, crop_h):
    w, h = img.size

    left = max((w - crop_w) // 2, 0)
    top = max((h - crop_h) // 2, 0)

    return img.crop((
        left,
        top,
        left + crop_w,
        top + crop_h
    ))


def rotate_and_crop(img, angle):
    original_w, original_h = img.size
    original_aspect = original_w / original_h

    rotated = img.rotate(
        angle,
        resample=Image.Resampling.BICUBIC,
        expand=True
    )

    safe_w, safe_h = largest_rotated_rect(
        original_w,
        original_h,
        math.radians(angle)
    )

    safe_aspect = safe_w / safe_h

    if safe_aspect > original_aspect:
        crop_h = safe_h
        crop_w = int(crop_h * original_aspect)
    else:
        crop_w = safe_w
        crop_h = int(crop_w / original_aspect)

    return center_crop(
        rotated,
        crop_w,
        crop_h
    )

def sample_angle(max_angle, min_abs_angle):
    """
    Losuje z:
    [-max_angle,-min_abs_angle]
    lub
    [min_abs_angle,max_angle]
    """

    sign = random.choice([-1, 1])

    value = round(
        random.uniform(
            min_abs_angle,
            max_angle
        ),
        2
    )

    return sign * value


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--src",
        type=str,
        default="/home/natal/code/pictures-rot/2-original"
    )

    parser.add_argument(
        "--dst",
        type=str,
        default="/home/natal/code/pictures-rot/2-rotated"
    )

    parser.add_argument(
        "--angle_range",
        type=float,
        default=8.5
    )

    parser.add_argument(
        "--min_abs_angle",
        type=float,
        default=0.9
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None
    )

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.min_abs_angle >= args.angle_range:
        raise ValueError(
            "min_abs_angle musi być mniejsze od angle_range"
        )

    src = Path(args.src)
    dst = Path(args.dst)

    dst.mkdir(
        parents=True,
        exist_ok=True
    )

    files = sorted([
        p for p in src.iterdir()
        if p.is_file()
        and p.suffix.lower() in IMG_EXTS
    ])

    csv_path = dst / "rotate.csv"

    with open(
        csv_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)
        writer.writerow([
            "filename",
            "angle"
        ])

        for path in files:

            angle = sample_angle(
                args.angle_range,
                args.min_abs_angle
            )

            with Image.open(path) as img:

                img = ImageOps.exif_transpose(img)

                if img.mode not in ("RGB", "RGBA"):
                    img = img.convert("RGB")

                result = rotate_and_crop(
                    img,
                    angle
                )

                result.save(
                    dst / path.name
                )

            writer.writerow([
                path.name,
                f"{angle:.2f}"
            ])

            print(
                f"{path.name} -> "
                f"{angle:.2f}°"
            )

    print()
    print(f"Processed: {len(files)}")
    print(f"CSV: {csv_path}")


if __name__ == "__main__":
    main()