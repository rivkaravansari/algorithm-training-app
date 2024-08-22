from enums.chat_question_enums import FeedbackType
from pydantic_models.base import Base


class Feedback(Base):
    user_id: int
    chat_question_id: int
    feedback: FeedbackType
