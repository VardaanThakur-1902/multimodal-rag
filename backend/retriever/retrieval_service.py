from retriever.vector_search import (
    VectorSearch,
)


from typing import Any


class RetrievalService:

    def __init__(self):

        self.vector_search = (
            VectorSearch()
        )

    def retrieve(
        self,
        question: str,
        top_k: int = 5,
    ) -> list[dict[str, Any]]:

        results = self.vector_search.search(
            question,
            top_k,
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        output = []

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances,
        ):

            output.append(
                {
                    "content": document,
                    "metadata": metadata,
                    "distance": distance,
                }
            )

        return output