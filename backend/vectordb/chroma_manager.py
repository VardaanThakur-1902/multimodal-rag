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

            print("=" * 50)
            print("Adding to Chroma")
            print("Type:", metadata.get("chunk_type"))
            print("Text:")
            print(text)
            print("=" * 50)

            metadata["chunk_id"] = chunk.chunk_id

            metadatas.append(metadata)

        from collections import Counter

        counter = Counter()

        for m in metadatas:
            counter[m.get("document_name")] += 1

        print("Document names being indexed:")
        print(counter)

            

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )
        from collections import Counter

        docs = self.collection.get(include=["metadatas"])

        counter = Counter(
            meta.get("document_name", "UNKNOWN")
            for meta in docs["metadatas"]
        )

        print("=" * 60)
        print("Documents in Chroma:")
        print(counter)
        print("Total vectors:", self.collection.count())
        print("=" * 60)
        print(metadata)

    def delete_chunks(
        self,
        chunk_ids: list[str],
    ):

        self.collection.delete(
            ids=chunk_ids
        )

    def count(self):

        return self.collection.count()
    
    def delete_document(
        self,
        document_name: str,
    ):

        from collections import Counter

        print("=" * 60)
        print("Deleting:", document_name)

        # Check what exists BEFORE delete
        docs = self.collection.get(include=["metadatas"])

        counter = Counter(
            meta.get("document_name", "UNKNOWN")
            for meta in docs["metadatas"]
        )

        print("Before delete:")
        print(counter)
        print("Total:", self.collection.count())

        # Delete
        self.collection.delete(
            where={
                "document_name": document_name
            }
        )

        # Check AFTER delete
        docs = self.collection.get(include=["metadatas"])

        counter = Counter(
            meta.get("document_name", "UNKNOWN")
            for meta in docs["metadatas"]
        )

        print("After delete:")
        print(counter)
        print("Total:", self.collection.count())
        print("=" * 60)

def get_chunks_by_session(
    self,
    session_id: str,
):

    return self.collection.get(
        where={
            "session_id": session_id
        }
    )