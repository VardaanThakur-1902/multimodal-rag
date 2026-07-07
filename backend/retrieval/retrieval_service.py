from retrieval.hybrid.hybrid_search import HybridSearch


class RetrievalService:

    def __init__(self):

        self.hybrid = HybridSearch()

    def retrieve(
        self,
        question: str,
        document_ids: list[str],
        top_k: int = 5,
    ):

        return self.hybrid.search(
            query=question,
            document_ids=document_ids,
            top_k=top_k,
        )