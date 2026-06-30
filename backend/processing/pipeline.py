from processing.cleaner import TextCleaner
from processing.chunker import Chunker


class ProcessingPipeline:

    @staticmethod
    def process(document):

        # ---------- Clean Text ----------

        for page in document.pages:

            page.text = TextCleaner.clean(page.text)

        # ---------- Create Chunks ----------

        chunks = Chunker.chunk(document)

        return chunks