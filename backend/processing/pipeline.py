from captioning.image_captioner import ImageCaptioner
from processing.chunker import Chunker
from processing.cleaner import TextCleaner
from processing.image_chunk_builder import ImageChunkBuilder
from processing.image_processor import ImageProcessor


class ProcessingPipeline:

    @staticmethod
    def process(
        document,
    ):

        # Clean pages
        for page in document.pages:
            page.text = TextCleaner.clean(page.text)

        text_chunks = Chunker.chunk(
            document,
        )
        print("Text chunks:", len(text_chunks))

        images = ImageProcessor.extract(document.file_path)
        print("Images:", len(images))

        captions = [
            ImageCaptioner.generate(image)
            for image in images
        ]
        print("Captions:", len(captions))

        image_chunks = ImageChunkBuilder.build(
            captions,
        )
        print("Image chunks:", len(image_chunks))

        print("Total:", len(text_chunks + image_chunks))

        return text_chunks + image_chunks