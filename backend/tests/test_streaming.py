from llm.ollama_client import OllamaClient


def main():

    print("=" * 60)
    print("STREAMING RESPONSE")
    print("=" * 60)

    for token in OllamaClient.generate_stream(
        "Explain RAG in one paragraph."
    ):
        print(token, end="", flush=True)

    print()


if __name__ == "__main__":
    main()