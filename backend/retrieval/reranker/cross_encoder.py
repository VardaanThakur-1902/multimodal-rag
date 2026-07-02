from sentence_transformers import CrossEncoder

from schemas.retrieval_result import RetrievalResult


class CrossEncoderReranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
        self,
        query: str,
        chunks: list[RetrievalResult],
        top_k: int = 5,
    ) -> list[RetrievalResult]:

        if not chunks:
            return []

        pairs = [
            (query, chunk.content)
            for chunk in chunks
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(chunks, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        reranked = []

        for chunk, score in ranked[:top_k]:

            chunk.score = float(score)

            reranked.append(chunk)

        return reranked