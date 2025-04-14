from sqlmodel import Field, SQLModel
from uuid import UUID
from pydantic import BaseModel




class ExperiencePointBase(SQLModel):
    points: int = Field(default=0, nullable=False)
    description: str = Field(default="", nullable=False)

class ExperiencePointCreate(ExperiencePointBase):
    pass

class ExperiencePointPublic(ExperiencePointBase):
    id: UUID
    created_at: str


class ExperiencePointSummary(BaseModel):
    today_experience: int
    difference_from_yesterday: int
    total_experience: int

class CulculatedExperiencePoint(BaseModel):
    points: int