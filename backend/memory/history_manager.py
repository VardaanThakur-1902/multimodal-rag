from memory.conversation_memory import (
    ConversationMemory,
)


class HistoryManager:

    _memory = ConversationMemory()

    @classmethod
    def add(
        cls,
        role: str,
        content: str,
    ):

        cls._memory.add(
            role,
            content,
        )

    @classmethod
    def history(cls):

        return cls._memory.get_history()

    @classmethod
    def clear(cls):

        cls._memory.clear()