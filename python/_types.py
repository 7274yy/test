from enum import Enum
from pydantic import BaseModel, constr


class levels(Enum):
    IG = "IG"
    Alevel = "Alevel"
    Olevel = "Olevel"


class LevelModel(BaseModel):
    level: levels


class SubjectModel(BaseModel):
    level: levels
    subject: constr(max_length=60)


class PaperModel(BaseModel):
    level: levels
    subject: constr(max_length=60)
    year: str
