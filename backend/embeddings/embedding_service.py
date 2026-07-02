from schemas.chunk import Chunk

from embeddings.ollama_embeddings import (
    OllamaEmbeddings,
)


class EmbeddingService:

    @staticmethod
    def generate(text: str):

        return OllamaEmbeddings.embed(text)

    @staticmethod
    def generate_batch(
        chunks: list[Chunk],
    ):

        texts = [
            chunk.content
            for chunk in chunks
        ]

        return OllamaEmbeddings.embed_batch(texts)