from indexing.indexing_service import IndexingService
from retrieval.hybrid.hybrid_search import HybridSearch
from retrieval.reranker.cross_encoder import (
    CrossEncoderReranker,
)


def main():

    service = IndexingService()

    chunks = service.process_document(
        "uploads/pdf/sample.pdf"
    )

    hybrid = HybridSearch()

    hybrid.build_keyword_index(chunks)

    retrieved = hybrid.search(
        "What is machine learning?",
        top_k=10,
    )

    reranker = CrossEncoderReranker()

    results = reranker.rerank(
        "What is the revenue in 2024?",
        retrieved,
        top_k=5,
    )

    print("=" * 80)
    print("RERANKED RESULTS")
    print("=" * 80)

    for result in results:

        print()

        print("Score:", result.score)

        print("Source:", result.source)

        print(result.content[:250])

        print("-" * 80)

    for result in retrieved:

        print(result.chunk_id)

        print(result.source)

        print(result.content[:80])

        print("-" * 40)


if __name__ == "__main__":
    main()