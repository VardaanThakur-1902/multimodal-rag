import requests

from config.settings import (
    OLLAMA_URL,
    EMBED_MODEL,
)


class OllamaEmbeddings:

    @staticmethod
    def embed(text: str):

        response = requests.post(
            f"{OLLAMA_URL}/api/embeddings",
            json={
                "model": EMBED_MODEL,
                "prompt": text,
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()["embedding"]

    @staticmethod
    def embed_batch(texts: list[str]):

        embeddings = []

        for text in texts:

            embeddings.append(
                OllamaEmbeddings.embed(text)
            )

        return embeddings