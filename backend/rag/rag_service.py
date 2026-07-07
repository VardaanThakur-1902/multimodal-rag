from llm.ollama_client import OllamaClient
from rag.context_builder import ContextBuilder
from rag.prompt_builder import PromptBuilder
from retrieval.retrieval_service import RetrievalService
from rag.citation_service import CitationService
from services.message_service import MessageService
from query_rewriting.query_rewriter import QueryRewriter
import json

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

        from services.session_document_service import (
            SessionDocumentService,
        )

        document_ids = SessionDocumentService.get_document_ids(
            session=session,
            session_id=session_id,
        )

        print("=" * 60)
        print("DOCUMENT IDS")
        print(document_ids)
        print("=" * 60)

        rewritten_question = QueryRewriter.rewrite(
            question,
            history,
        )

        from services.session_document_service import SessionDocumentService

        document_ids = SessionDocumentService.get_document_ids(
            session=session,
            session_id=session_id,
        )

        print(document_ids)

        retrieved_chunks = self.retriever.retrieve(
            question=rewritten_question,
            document_ids=document_ids,
            top_k=top_k,
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

        citations = CitationService.build(
            retrieved_chunks
        )

        MessageService.add(
            session=session,
            session_id=session_id,
            role="assistant",
            content=answer,
            sources=json.dumps(citations),
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

        from services.session_document_service import (
            SessionDocumentService,
        )

        document_ids = SessionDocumentService.get_document_ids(
            session=session,
            session_id=session_id,
        )

        print("=" * 60)
        print("DOCUMENT IDS")
        print(document_ids)
        print("=" * 60)

        retrieved_chunks = self.retriever.retrieve(
            question=rewritten_question,
            document_ids=document_ids,
            top_k=top_k,
        )

        print("=" * 50)
        print("Retrieved chunks:", len(retrieved_chunks))

        for chunk in retrieved_chunks:
            print(chunk.source)
            print(chunk.metadata)
            print(chunk.content[:100])

        print("=" * 50)

        context = ContextBuilder.build(
            retrieved_chunks
        )

        prompt = PromptBuilder.build(
            question=rewritten_question,
            context=context,
            history=history,
        )

        # Save user message once
        MessageService.add(
            session=session,
            session_id=session_id,
            role="user",
            content=question,
        )

        answer = ""

        for token in OllamaClient.generate_stream(
            prompt
        ):

            answer += token

            yield (
                f"event: token\n"
                f"data: {json.dumps(token)}\n\n"
            )

        # Save assistant message once
        citations = CitationService.build(
            retrieved_chunks
        )

        MessageService.add(
            session=session,
            session_id=session_id,
            role="assistant",
            content=answer,
            sources=json.dumps(citations),
        )

        # Send sources event
        yield (
            "event: sources\n"
            f"data: {json.dumps(citations)}\n\n"
        )

        # Tell frontend streaming is complete
        yield (
            "event: done\n"
            "data: {}\n\n"
        )