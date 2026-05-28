from pathlib import Path
from PIL import Image, ExifTags
import shutil

SOURCE_DIR = Path("/mnt/mowa/pictures/pictures-rot/original/1-original")

# utwórz foldery jeśli nie istnieją
folders = {
    "-90": SOURCE_DIR / "-90",
    "90": SOURCE_DIR / "90",
    "0": SOURCE_DIR / "0",
}

for folder in folders.values():
    folder.mkdir(exist_ok=True)

# znajdź numer taga Orientation
orientation_tag = None
for tag, name in ExifTags.TAGS.items():
    if name == "Orientation":
        orientation_tag = tag
        break

extensions = {".jpg", ".jpeg", ".JPG", ".JPEG", ".png", ".PNG"}

for img_path in SOURCE_DIR.iterdir():
    if not img_path.is_file():
        continue

    if img_path.suffix not in extensions:
        continue

    try:
        orientation = 1

        with Image.open(img_path) as img:
            exif = img.getexif()

            if exif and orientation_tag in exif:
                orientation = exif[orientation_tag]

        # mapowanie EXIF -> wymagany obrót
        if orientation == 6:
            target_dir = folders["90"]

        elif orientation == 8:
            target_dir = folders["-90"]

        else:
            target_dir = folders["0"]

        dst = target_dir / img_path.name
        shutil.move(str(img_path), str(dst))

        print(
            f"{img_path.name}: orientation={orientation} -> {target_dir.name}"
        )

    except Exception as e:
        print(f"Błąd {img_path.name}: {e}")