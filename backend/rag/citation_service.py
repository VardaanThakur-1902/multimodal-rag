class CitationService:

    @staticmethod
    def build(chunks):

        citations = []
        seen = set()

        for chunk in chunks:

            metadata = chunk.metadata

            chunk_type = (
                metadata.get("chunk_type")
                or metadata.get("type")
            )

            key = (
                metadata.get("document_name"),
                metadata.get("page"),
                chunk_type,
            )

            if key in seen:
                continue

            seen.add(key)

            citations.append(
                {
                    "document": metadata.get("document_name"),
                    "page": metadata.get("page"),
                    "type": chunk_type,
                    "image_path": metadata.get("image_path"),
                }
            )

        return citations