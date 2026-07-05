from retrieval.vector.vector_search import VectorSearch
from retrieval.keyword.bm25 import BM25Retriever
from retrieval.fusion.rrf import ReciprocalRankFusion
from retrieval.reranker.cross_encoder import CrossEncoderReranker

class HybridSearch:

    def __init__(self):

        self.vector = VectorSearch()

        self.keyword = BM25Retriever()

        self.reranker = CrossEncoderReranker()

    def build_keyword_index(
        self,
        chunks,
    ):

        self.keyword.build(chunks)

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        vector_results = self.vector.search(
            query,
            top_k=20,
        )

        keyword_results = self.keyword.search(
            query,
            top_k=20,
        )

        fused = ReciprocalRankFusion.fuse(
            vector_results,
            keyword_results,
        )

        reranked = self.reranker.rerank(
            query,
            fused,
            top_k=top_k,
        )

        vector_results = self.vector.search(
            query,
            top_k=20,
        )

        print("\n===== VECTOR RESULTS =====")
        for r in vector_results:
            print(r.source)

        keyword_results = self.keyword.search(
            query,
            top_k=20,
        )

        print("\n===== BM25 RESULTS =====")
        for r in keyword_results:
            print(r.source)

        return reranked