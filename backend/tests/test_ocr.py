from processing.image_processor import ImageProcessor
from ocr.ocr_service import OCRService


def main():

    images = ImageProcessor.extract(
        "uploads/pdf/52cd9318-6a49-4d4a-bf25-9842eb32980e.pdf"
    )

    print("=" * 80)
    print("OCR RESULTS")
    print("=" * 80)

    for image in images:

        print()

        print(image.image_path)

        print("-" * 40)

        text = OCRService.extract_text(
            image.image_path
        )

        print(text)

        print("-" * 80)


if __name__ == "__main__":
    main()