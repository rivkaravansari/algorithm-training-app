from pydantic_models.base import Base


class ChatQuestion(Base):
    prompt: str
