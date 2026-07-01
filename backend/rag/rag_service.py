from llm.ollama_client import OllamaClient
from rag.context_builder import ContextBuilder
from rag.prompt_builder import PromptBuilder
from retriever.retrieval_service import RetrievalService


class RAGService:

    def __init__(self):

        self.retriever = RetrievalService()

    def answer(
        self,
        question: str,
        top_k: int = 5,
    ):

        retrieved_chunks = self.retriever.retrieve(
            question,
            top_k,
        )

        context = ContextBuilder.build(
            retrieved_chunks
        )

        prompt = PromptBuilder.build(
            question=question,
            context=context,
        )

        answer = OllamaClient.generate(
            prompt
        )

        return {
            "answer": answer,
            "sources": [
                chunk["metadata"]
                for chunk in retrieved_chunks
            ],
        }