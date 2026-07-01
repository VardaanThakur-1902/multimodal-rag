from schemas.chunk import Chunk

from embeddings.ollama_embeddings import (
    OllamaEmbeddings,
)


class EmbeddingService:

    @staticmethod
    def generate(chunk: Chunk):

        return OllamaEmbeddings.embed(
            chunk.content
        )

    @staticmethod
    def generate_batch(
        chunks: list[Chunk],
    ):

        texts = [
            chunk.content
            for chunk in chunks
        ]

        return OllamaEmbeddings.embed_batch(
            texts
        )
    
    @staticmethod
    def generate_text(
        text: str,
    ):

        return OllamaEmbeddings.embed(
            text
        )