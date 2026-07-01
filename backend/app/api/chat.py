from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import ai_service

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = ai_service.chat(request.message)

    return ChatResponse(response=reply)