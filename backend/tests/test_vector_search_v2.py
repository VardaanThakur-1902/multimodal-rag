from retrieval.vector.vector_search import (
    VectorSearch,
)


def main():

    search = VectorSearch()

    results = search.search(
        "What is the revenue in 2024?"
    )

    print("=" * 80)

    print("VECTOR SEARCH")

    print("=" * 80)

    for result in results:

        print()

        print("Chunk:", result.chunk_id)

        print("Score:", result.score)

        print("Source:", result.source)

        print("Page:", result.metadata["page"])

        print()

        print(result.content[:400])

        print("-" * 80)


if __name__ == "__main__":
    main()