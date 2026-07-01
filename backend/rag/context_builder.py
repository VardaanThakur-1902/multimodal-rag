from typing import Any


class ContextBuilder:

    @staticmethod
    def build(
        retrieved_chunks: list[dict[str, Any]]
    ) -> str:

        context_parts = []

        for chunk in retrieved_chunks:

            metadata = chunk["metadata"]

            section = f"""
Source: {metadata.get("document_name", "Unknown")}
Page: {metadata.get("page", "Unknown")}
Type: {metadata.get("chunk_type", "Unknown")}

{chunk["content"]}
"""

            context_parts.append(
                section.strip()
            )

        return "\n\n" + "-" * 80 + "\n\n".join(context_parts)