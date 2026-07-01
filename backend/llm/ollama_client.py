import requests

from config.settings import CHAT_MODEL
from config.settings import OLLAMA_URL


class OllamaClient:

    @staticmethod
    def generate(prompt: str) -> str:

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": CHAT_MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()["response"]