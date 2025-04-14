
from fastapi import APIRouter
from app.models.experience_points import ExperiencePointPublic, ExperiencePointCreate, ExperiencePointSummary, CulculatedExperiencePoint

router = APIRouter(prefix="/experience_points", tags=["experience_points"])



@router.post("/", response_model=ExperiencePointPublic)
async def create_experience_points(experience_point: ExperiencePointCreate):
    return experience_point

@router.post("/culculate", response_model=CulculatedExperiencePoint)
async def calculate_experience_points(description: str):
    return {"points": 100}

@router.get("/summary", response_model=ExperiencePointSummary)
async def get_experience_points_summary():
    return {"experience_points": 1000}