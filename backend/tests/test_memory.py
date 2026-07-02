from memory.conversation_memory import (
    ConversationMemory,
)


def main():

    memory = ConversationMemory()

    memory.add(
        "user",
        "What is RAG?"
    )

    memory.add(
        "assistant",
        "RAG stands for Retrieval-Augmented Generation."
    )

    memory.add(
        "user",
        "Who invented it?"
    )

    print(memory.get_history())


if __name__ == "__main__":
    main()