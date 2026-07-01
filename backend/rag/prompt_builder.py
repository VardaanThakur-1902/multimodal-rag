class PromptBuilder:

    SYSTEM_PROMPT = """
You are a helpful AI assistant that answers questions ONLY using the provided context.

Rules:

1. Use only the information in the context.
2. Do not make up facts.
3. If the answer is not present in the context, reply:
   "I could not find that information in the uploaded documents."
4. If the context contains tables, interpret them accurately.
5. If multiple sources contain the answer, combine the information naturally.
6. Answer clearly and concisely.
"""

    @classmethod
    def build(
        cls,
        question: str,
        context: str,
    ) -> str:

        return f"""
{cls.SYSTEM_PROMPT}

======================
CONTEXT
======================

{context}

======================
QUESTION
======================

{question}

======================
ANSWER
======================
"""