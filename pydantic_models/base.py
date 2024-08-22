from pydantic import BaseModel, Field
import uuid


class Base(BaseModel):
    id: int = Field(default_factory=lambda: uuid.uuid4().int >> 64)

