import chromadb

from config.settings import (
    CHROMA_PATH,
    COLLECTION_NAME,
)


class CollectionManager:

    _client = chromadb.PersistentClient(
        path=str(CHROMA_PATH)
    )

    @classmethod
    def get_collection(cls):

        return cls._client.get_or_create_collection(
            name=COLLECTION_NAME
        )