from schemas.chunk import Chunk

from vectordb.collection_manager import (
    CollectionManager,
)

from embeddings.embedding_service import (
    EmbeddingService,
)

from typing import Any

class ChromaManager:

    def __init__(self):

        self.collection = (
            CollectionManager.get_collection()
        )

    def add_chunks(
        self,
        chunks: list[Any],
    ):

        ids = []

        documents = []

        embeddings = []

        metadatas = []

        for chunk in chunks:

            ids.append(chunk.chunk_id)

            text = getattr(chunk, "content", None)

            if text is None:
                text = chunk.caption

            documents.append(text)

            embeddings.append(
                EmbeddingService.generate(text)
            )

            metadata = dict(chunk.metadata)

            metadata["chunk_id"] = chunk.chunk_id

            metadatas.append(metadata)

            

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def delete_chunks(
        self,
        chunk_ids: list[str],
    ):

        self.collection.delete(
            ids=chunk_ids
        )

    def count(self):

        return self.collection.count()