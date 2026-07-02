from indexing.indexing_service import IndexingService
from retrieval.keyword.bm25 import BM25Retriever


def main():

    service = IndexingService()

    chunks = service.process_document(
        "uploads/pdf/sample.pdf"
    )

    bm25 = BM25Retriever()

    bm25.build(chunks)

    results = bm25.search(
        "revenue 2024"
    )

    print("=" * 80)
    print("BM25 RESULTS")
    print("=" * 80)

    for result in results:

        print()

        print("Chunk ID:", result.chunk_id)
        print("Score:", result.score)
        print("Source:", result.source)

        print()

        print(result.content[:300])

        print("-" * 80)


if __name__ == "__main__":
    main()