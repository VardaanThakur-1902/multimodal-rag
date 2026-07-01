from rag.rag_service import RAGService


def main():

    rag = RAGService()

    result = rag.answer(
        "What is the revenue in 2024?"
    )

    print("=" * 80)
    print("ANSWER")
    print("=" * 80)

    print(result["answer"])

    print()

    print("=" * 80)
    print("SOURCES")
    print("=" * 80)

    for source in result["sources"]:

        print(source)


if __name__ == "__main__":
    main()