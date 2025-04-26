from pydantic import BaseModel


class ConversationTurn(BaseModel):
    role: str
    content: str


class Conversation(BaseModel):
    conversation: list[ConversationTurn]
