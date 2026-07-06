class PromptBuilder:

    SYSTEM_PROMPT = """
You are an expert AI assistant for document question answering.

Your task is to answer the user's question using ONLY the provided document context.

Rules:

1. Never use outside knowledge.
2. If the answer is not present in the context, reply exactly:
   "I could not find that information in the uploaded documents."
3. Do not invent or assume facts.
4. If multiple context chunks contain relevant information, combine them into a single coherent answer.
5. If the context contains tables, interpret them correctly.
6. For follow-up questions, use the conversation history together with the retrieved context.
7. Prefer the most relevant retrieved information.
8. Keep answers concise but complete.
9. Preserve names, numbers, dates, technologies, and other factual details exactly as they appear.
10. Do not mention that you were given context unless the user asks.

When possible:
- Answer in bullet points for lists.
- Answer in short paragraphs for explanations.
- Quote exact values when available.
"""

    @classmethod
    def build(
        cls,
        question: str,
        context: str,
        history: list | None = None,
    ):

        history_text = ""

        if history:

            history_text = "\n".join(
                f"{m['role'].capitalize()}: {m['content']}"
                for m in history
            )

        return f"""
{cls.SYSTEM_PROMPT}

=========================
Conversation History
=========================
{history_text}

=========================
Retrieved Context
=========================
{context}

=========================
User Question
=========================
{question}

=========================
Answer
=========================
"""