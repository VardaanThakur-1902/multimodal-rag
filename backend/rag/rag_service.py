from llm.ollama_client import OllamaClient
from rag.context_builder import ContextBuilder
from rag.prompt_builder import PromptBuilder
from retrieval.retrieval_service import RetrievalService
from rag.citation_service import CitationService
from memory.history_manager import HistoryManager
from query_rewriting.query_rewriter import QueryRewriter

class RAGService:

    def __init__(self):

        self.retriever = RetrievalService()

    def answer(
        self,
        question: str,
        top_k: int = 5,
    ):

        history = HistoryManager.history()

        rewritten_question = QueryRewriter.rewrite(
            question,
            history,
        )

        retrieved_chunks = self.retriever.retrieve(
            rewritten_question,
            top_k,
        )

        context = ContextBuilder.build(
            retrieved_chunks
        )

        history = HistoryManager.history()

        prompt = PromptBuilder.build(
            question=rewritten_question,
            context=context,
            history=history,
        )

        answer = OllamaClient.generate(
            prompt
        )

        HistoryManager.add(
            "user",
            question,
        )

        HistoryManager.add(
            "assistant",
            answer,
        )

        citations = CitationService.build(
            retrieved_chunks
        )

        return {
            "answer": answer,
            "sources": citations,
        }

    def answer_stream(
        self,
        question: str,
        top_k: int = 5,
    ):

        history = HistoryManager.history()

        rewritten_question = QueryRewriter.rewrite(
            question,
            history,
        )

        retrieved_chunks = self.retriever.retrieve(
            rewritten_question,
            top_k,
        )

        context = ContextBuilder.build(
            retrieved_chunks
        )

        prompt = PromptBuilder.build(
            question=rewritten_question,
            context=context,
            history=history,
        )

        answer = ""

        for token in OllamaClient.generate_stream(
            prompt
        ):

            answer += token

            yield token

        HistoryManager.add(
            "user",
            question,
        )

        HistoryManager.add(
            "assistant",
            answer,
        )