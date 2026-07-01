from schemas.chunk import Chunk

from vectordb.collection_manager import (
    CollectionManager,
)

from embeddings.embedding_service import (
    EmbeddingService,
)


class ChromaManager:

    def __init__(self):

        self.collection = (
            CollectionManager.get_collection()
        )

    def add_chunks(
        self,
        chunks: list[Chunk],
    ):

        ids = []

        documents = []

        embeddings = []

        metadatas = []

        for chunk in chunks:

            ids.append(chunk.chunk_id)

            documents.append(chunk.content)

            embeddings.append(
                EmbeddingService.generate(chunk)
            )

            metadata = {
                "document_name": chunk.document_name,
                "page": chunk.page_number,
                "chunk_type": chunk.chunk_type,
            }

            metadata.update(chunk.metadata)

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