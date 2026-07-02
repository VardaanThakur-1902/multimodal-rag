from indexing.indexing_service import IndexingService


def main():

    service = IndexingService()

    service.index_document(
        "uploads/pdf/sample.pdf"
    )

    from retriever.bm25_search import BM25Search

    search = BM25Search()

    results = search.search(
        "revenue 2024"
    )

    print("=" * 80)

    print("BM25 RESULTS")

    print("=" * 80)

    for result in results:

        print()

        print(result["metadata"])

        print()

        print(result["content"][:400])

        print("-" * 80)


if __name__ == "__main__":
    main()