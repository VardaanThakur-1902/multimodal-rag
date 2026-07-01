from embeddings.embedding_service import (
    EmbeddingService,
)

from vectordb.collection_manager import (
    CollectionManager,
)


class VectorSearch:

    def __init__(self):

        self.collection = (
            CollectionManager.get_collection()
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        embedding = (
            EmbeddingService.generate_text(
                query
            )
        )

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        return results