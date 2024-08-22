from enums.exercise_enums import ExerciseLevel
from pydantic_models.base import Base


class Exercise(Base):
    algorithm_id: int
    text: str
    level: ExerciseLevel
