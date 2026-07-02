from indexing.indexing_service import IndexingService
from retrieval.hybrid.hybrid_search import HybridSearch


def main():

    service = IndexingService()

    chunks = service.process_document(
        "uploads/pdf/sample.pdf"
    )

    hybrid = HybridSearch()

    hybrid.build_keyword_index(chunks)

    results = hybrid.search(
        "revenue 2024"
    )

    print("=" * 80)
    print("HYBRID SEARCH")
    print("=" * 80)

    for result in results:

        print()

        print("Chunk:", result.chunk_id)
        print("Score:", result.score)
        print("Source:", result.source)
        print("Page:", result.metadata.get("page"))

        print()

        print(result.content[:300])

        print("-" * 80)


if __name__ == "__main__":
    main()