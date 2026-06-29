from fastapi import APIRouter
from pydantic import BaseModel

from llm.ollama import generate_response

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: ChatRequest):

    answer = generate_response(request.question)

    return {
        "answer": answer
    }