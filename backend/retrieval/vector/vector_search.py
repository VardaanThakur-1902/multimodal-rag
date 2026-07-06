from schemas.retrieval_result import RetrievalResult
from vectordb.collection_manager import CollectionManager

from embeddings.embedding_service import (
    EmbeddingService,
)


class VectorSearch:

    def __init__(self):

        self.collection = (
            CollectionManager.get_collection()
        )

    def search(
        self,
        query: str,
        session_id: str,
        top_k: int = 5,
    ) -> list[RetrievalResult]:

        embedding = (
            EmbeddingService.generate(
                query
            )
        )

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            where={
                "session_id": session_id
            }
        )

        print("=" * 50)
        print(results)
        print("=" * 50)

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

                RetrievalResult(

                    chunk_id=metadata[
                        "chunk_id"
                    ],

                    content=document,

                    score=float(distance),

                    metadata=metadata,

                    source=metadata.get(
                        "document_name",
                        "Unknown",
                    ),
                )

            )

            print("\n========== VECTOR SEARCH ==========")

            for result in output:
                print("Type:", result.metadata.get("chunk_type"))
                print("Page:", result.metadata.get("page"))
                print(result.content[:200])
                print("----------------------------------")

        return output