from captioning.image_captioner import ImageCaptioner
from processing.image_chunk_builder import (
    ImageChunkBuilder,
)
from processing.image_processor import ImageProcessor
from vectordb.chroma_manager import ChromaManager


def main():

    images = ImageProcessor.extract(
        "uploads/pdf/sample.pdf"
    )

    captions = [
        ImageCaptioner.generate(image)
        for image in images
    ]

    chunks = ImageChunkBuilder.build(captions)

    db = ChromaManager()

    db.add_chunks(chunks)

    print("=" * 80)
    print("IMAGE CHUNKS INDEXED")
    print("=" * 80)

    print(len(chunks))


if __name__ == "__main__":
    main()