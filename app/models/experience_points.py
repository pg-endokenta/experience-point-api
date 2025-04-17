from sqlmodel import Field, SQLModel
import uuid
from pydantic import BaseModel
from datetime import datetime

class ExperiencePointBase(SQLModel):
    points: int = Field(default=0, nullable=False)
    description: str = Field(default="", nullable=False)

class ExperiencePoint(ExperiencePointBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)

class ExperiencePointCreate(ExperiencePointBase):
    pass

class ExperiencePointPublic(ExperiencePointBase):
    id: uuid.UUID
    created_at: datetime


class ExperiencePointSummary(BaseModel):
    today_experience: int
    difference_from_yesterday: int
    total_experience: int

class CulculatedExperiencePoint(BaseModel):
    points: int