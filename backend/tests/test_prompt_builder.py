from rag.context_builder import ContextBuilder
from rag.prompt_builder import PromptBuilder
from retriever.retrieval_service import RetrievalService


def main():

    retriever = RetrievalService()

    results = retriever.retrieve(
        "What is the revenue in 2024?"
    )

    context = ContextBuilder.build(results)

    prompt = PromptBuilder.build(
        question="What is the revenue in 2024?",
        context=context,
    )

    print("=" * 80)
    print("PROMPT")
    print("=" * 80)

    print(prompt)


if __name__ == "__main__":
    main()