import requests

from config.settings import (
    OLLAMA_URL,
    EMBED_MODEL,
)


class OllamaEmbeddings:

    @staticmethod
    def embed(text: str):

        response = requests.post(
            f"{OLLAMA_URL}/api/embed",
            json={
                "model": EMBED_MODEL,
                "input": text,
            },
            timeout=300,
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        return response.json()["embeddings"][0]

    @staticmethod
    def embed_batch(texts: list[str]):

        response = requests.post(
            f"{OLLAMA_URL}/api/embed",
            json={
                "model": EMBED_MODEL,
                "input": texts,
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()["embeddings"]