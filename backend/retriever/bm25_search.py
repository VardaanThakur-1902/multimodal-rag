from retriever.bm25_manager import BM25Manager


class BM25Search:

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        if not BM25Manager.is_ready():

            return []

        tokens = query.lower().split()

        scores = BM25Manager.get_bm25().get_scores(
            tokens
        )

        ranked = sorted(
            zip(
                BM25Manager.get_chunks(),
                scores,
            ),
            key=lambda x: x[1],
            reverse=True,
        )

        results = []

        for chunk, score in ranked[:top_k]:

            results.append(
                {
                    "content": chunk.content,
                    "metadata": {
                        "document_name": chunk.document_name,
                        "page": chunk.page_number,
                        "chunk_type": chunk.chunk_type,
                    },
                    "score": float(score),
                }
            )

        return results