from retriever.retrieval_service import RetrievalService


def main():

    retriever = RetrievalService()

    results = retriever.retrieve(
        "What is multimodal RAG?"
    )

    print("=" * 80)
    print("RETRIEVAL RESULTS")
    print("=" * 80)

    for i, result in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("-" * 40)

        print("Distance:", result["distance"])
        print("Metadata:", result["metadata"])

        print("\nContent:\n")

        print(result["content"][:500])

        print("\n" + "=" * 80)


if __name__ == "__main__":
    main()