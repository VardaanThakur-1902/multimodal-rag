from captioning.image_captioner import ImageCaptioner
from processing.chunker import Chunker
from processing.cleaner import TextCleaner
from processing.image_chunk_builder import ImageChunkBuilder
from processing.image_processor import ImageProcessor


class ProcessingPipeline:

    @staticmethod
    def process(document):

        # Clean pages
        for page in document.pages:
            page.text = TextCleaner.clean(page.text)

        # Text chunks
        text_chunks = Chunker.chunk(document)

        # Image extraction
        images = ImageProcessor.extract(document.file_path)

        # Captions
        captions = [
            ImageCaptioner.generate(image)
            for image in images
        ]

        # Image chunks
        image_chunks = ImageChunkBuilder.build(captions)

        # Merge everything
        return text_chunks + image_chunks