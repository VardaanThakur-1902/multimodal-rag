from rag.citation_service import CitationService
from retrieval.retrieval_service import RetrievalService


def main():

    retriever = RetrievalService()

    chunks = retriever.retrieve(
        "What is machine learning?"
    )

    citations = CitationService.build(
        chunks
    )

    print("=" * 80)
    print("CITATIONS")
    print("=" * 80)

    for citation in citations:
        print(citation)


if __name__ == "__main__":
    main()