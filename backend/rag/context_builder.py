from schemas.retrieval_result import RetrievalResult


class ContextBuilder:

    @staticmethod
    def build(
        chunks: list[RetrievalResult],
    ) -> str:

        context = []

        for chunk in chunks:

            metadata = chunk.metadata

            context.append(
                f"""
Document: {metadata.get('document_name', 'Unknown')}
Page: {metadata.get('page', 'Unknown')}
Type: {metadata.get('chunk_type', 'text')}

{chunk.content}
"""
            )

        return "\n\n".join(context)