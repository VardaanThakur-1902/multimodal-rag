from rank_bm25 import BM25Okapi

from retrieval.keyword.tokenizer import Tokenizer
from schemas.chunk import Chunk
from schemas.retrieval_result import RetrievalResult


class BM25Retriever:

    def __init__(self):

        self.bm25 = None

        self.chunks: list[Chunk] = []

    def build(
        self,
        chunks: list[Chunk],
    ):

        self.chunks = chunks

        corpus = [
            Tokenizer.tokenize(chunk.content)
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(corpus)

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievalResult]:

        if self.bm25 is None:
            return []

        query_tokens = Tokenizer.tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        ranked = sorted(
            zip(self.chunks, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        results = []

        for chunk, score in ranked[:top_k]:

            results.append(
                RetrievalResult(
                    chunk_id=chunk.chunk_id,
                    content=chunk.content,
                    score=float(score),
                    metadata=chunk.metadata,
                    source=chunk.document_name,
                )
            )

        return results