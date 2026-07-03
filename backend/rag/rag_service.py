from llm.ollama_client import OllamaClient
from rag.context_builder import ContextBuilder
from rag.prompt_builder import PromptBuilder
from retrieval.retrieval_service import RetrievalService
from rag.citation_service import CitationService
from services.message_service import MessageService
from query_rewriting.query_rewriter import QueryRewriter

class RAGService:

    def __init__(self):

        self.retriever = RetrievalService()

    def answer(
        self,
        question: str,
        session_id: str,
        session,
        top_k: int = 5,
    ):

        history = MessageService.recent_history(
            session,
            session_id,
        )

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

        MessageService.add(
            session=session,
            session_id=session_id,
            role="user",
            content=question,
        )

        answer = OllamaClient.generate(
            prompt
        )

        MessageService.add(
            session=session,
            session_id=session_id,
            role="user",
            content=question,
        )

        MessageService.add(
            session=session,
            session_id=session_id,
            role="assistant",
            content=answer,
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
        session_id: str,
        session,
        top_k: int = 5,
    ):

        history = MessageService.recent_history(
            session,
            session_id,
        )

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
            
            MessageService.add(
                session=session,
                session_id=session_id,
                role="user",
                content=question,
            )

            MessageService.add(
                session=session,
                session_id=session_id,
                role="assistant",
                content=answer,
            )

            answer += token

            yield token

        