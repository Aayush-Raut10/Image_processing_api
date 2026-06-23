from pathlib import Path
from PIL import Image, ImageFilter

OUTPUT_DIR = Path("static/processed")
OUTPUT_DIR.mkdir(exist_ok=True)



def resize_image(image_path: str, width: int, height: int) -> str:

    image = Image.open(image_path)

    resized_image = image.resize((width, height))

    output_path = (
        Path(OUTPUT_DIR)
        / f"resized_{Path(image_path).name}"
    )

    resized_image.save(output_path)

    return str(output_path)


def blur_image(image_path: str, radius: int = 5) -> str:

    image = Image.open(image_path)

    blurred_image = image.filter(
        ImageFilter.GaussianBlur(radius=radius)
    )

    output_path = (
        Path(OUTPUT_DIR)
        / f"blurred_{Path(image_path).name}"
    )

    blurred_image.save(output_path)

    return str(output_path)


def grayscale_image(image_path: str) -> str:

    image = Image.open(image_path)

    gray_image = image.convert("L")

    output_path = (
        Path(OUTPUT_DIR)
        / f"grayscale_{Path(image_path).name}"
    )

    gray_image.save(output_path)

    return str(output_path)


def compress_image(
    image_path: str,
    quality: int = 70
) -> str:

    image = Image.open(image_path)

    if image.mode == "RGBA":
        image = image.convert("RGB")

    output_path = (
        Path(OUTPUT_DIR)
        / f"compressed_{Path(image_path).stem}.jpg"
    )

    image.save(
        output_path,
        optimize=True,
        quality=quality
    )

    return str(output_path)


def create_thumbnail(
    image_path: str,
    width: int = 200,
    height: int = 200
) -> str:

    image = Image.open(image_path)

    image.thumbnail((width, height))

    output_path = (
        Path(OUTPUT_DIR)
        / f"thumbnail_{Path(image_path).name}"
    )

    image.save(output_path)

    return str(output_path)
