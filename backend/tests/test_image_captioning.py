from captioning.image_captioner import ImageCaptioner
from processing.image_processor import ImageProcessor


def main():

    images = ImageProcessor.extract(
        "uploads/pdf/sample.pdf"
    )

    print("=" * 80)
    print("IMAGE CAPTIONS")
    print("=" * 80)

    for image in images:

        caption = ImageCaptioner.generate(image)

        print()

        print("Image:", caption.image_path)

        print("Caption:", caption.caption)

        print("-" * 80)


if __name__ == "__main__":
    main()