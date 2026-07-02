from llm.ollama_client import OllamaClient


class QueryRewriter:

    @staticmethod
    def rewrite(
        question: str,
        history: list,
    ) -> str:

        if not history:
            return question

        history_text = ""

        for message in history[-6:]:

            history_text += (
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n"
            )

        prompt = f"""
You rewrite follow-up questions so they become complete standalone questions.

Conversation:

{history_text}

Current Question:
{question}

Return ONLY the rewritten question.

If the current question is already complete,
return it unchanged.
"""

        rewritten = OllamaClient.generate(
            prompt
        )

        return rewritten.strip()