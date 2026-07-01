from rag.context_builder import ContextBuilder
from retriever.retrieval_service import RetrievalService


def main():

    retriever = RetrievalService()

    results = retriever.retrieve(
        "What is the revenue in 2024?"
    )

    context = ContextBuilder.build(
        results
    )

    print("=" * 80)
    print("CONTEXT")
    print("=" * 80)

    print(context)


if __name__ == "__main__":
    main()