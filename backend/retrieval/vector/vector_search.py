from schemas.retrieval_result import RetrievalResult
from vectordb.collection_manager import CollectionManager
from schemas.chunk import Chunk

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
    
    def get_session_chunks(
        self,
        session_id: str,
    ) -> list[Chunk]:

        results = self.collection.get(
            where={
                "session_id": session_id
            }
        )

        chunks = []

        for document, metadata in zip(
            results["documents"],
            results["metadatas"],
        ):

            chunks.append(
                Chunk(
                    chunk_id=metadata["chunk_id"],
                    document_name=metadata["document_name"],
                    page_number=metadata["page"],
                    chunk_type=metadata["chunk_type"],
                    content=document,
                    metadata=metadata,
                )
            )

            print("=" * 60)
            print("Building BM25 for Session:", session_id)
            print("Chunks loaded:", len(chunks))

            documents = {
                chunk.document_name
                for chunk in chunks
            }

            print("Documents in BM25:")
            print(documents)
            print("=" * 60)

        return chunks