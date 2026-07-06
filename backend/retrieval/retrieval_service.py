from retrieval.hybrid.hybrid_search import HybridSearch


class RetrievalService:

    def __init__(self):

        self.hybrid = HybridSearch()

    def build_index(
        self,
        chunks,
    ):

        self.hybrid.build_keyword_index(chunks)

    def retrieve(
        self,
        question: str,
        session_id,
        top_k: int = 5,
    ):

        return self.hybrid.search(
            query=question,
            session_id=session_id,
            top_k=top_k,
        )