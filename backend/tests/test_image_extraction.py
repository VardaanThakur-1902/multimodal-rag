from processing.image_processor import (
    ImageProcessor,
)


def main():

    images = ImageProcessor.extract(
        "uploads/pdf/sample.pdf"
    )

    print("=" * 80)
    print("EXTRACTED IMAGES")
    print("=" * 80)

    for image in images:

        print()

        print(image.document_name)

        print(image.page_number)

        print(image.image_path)

        print("-" * 80)


if __name__ == "__main__":
    main()