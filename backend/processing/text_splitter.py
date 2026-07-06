class TextSplitter:

    CHUNK_SIZE = 800
    OVERLAP = 150

    @staticmethod
    def split(text: str):

        if not text.strip():
            return []

        chunks = []

        start = 0

        while start < len(text):

            end = start + TextSplitter.CHUNK_SIZE

            chunks.append(
                text[start:end]
            )

            start += (
                TextSplitter.CHUNK_SIZE
                - TextSplitter.OVERLAP
            )

        return chunks