
from fastapi import APIRouter, Depends
from app.api.deps import get_token_header
from app.ai.culculate import get_experience_point_by_text
from app.models.experience_points import (
    ExperiencePoint,
    ExperiencePointPublic, 
    ExperiencePointCreate, 
    ExperiencePointSummary, 
    CulculatedExperiencePoint
)

from app.api.deps import SessionDep
from sqlmodel import Session, select
from sqlalchemy import func

from sqlalchemy.sql import text


router = APIRouter(
    prefix="/experience_points",
    tags=["experience_points"],
)

@router.post("/", response_model=ExperiencePointPublic, dependencies=[Depends(get_token_header)])
async def create_experience_points(experience_point_create: ExperiencePointCreate, session: SessionDep):

    db_experience_point = ExperiencePoint.model_validate(experience_point_create)
    session.add(db_experience_point)
    session.commit()
    session.refresh(db_experience_point)
    public_experience_point = ExperiencePointPublic.model_validate(db_experience_point)
    return public_experience_point


@router.post("/culculate/", response_model=CulculatedExperiencePoint, dependencies=[Depends(get_token_header)])
async def calculate_experience_points(description: str):



    return {
        "points": get_experience_point_by_text(description)
    }

@router.post("/summary/", response_model=ExperiencePointSummary, dependencies=[Depends(get_token_header)])
async def get_experience_points_summary(session: SessionDep):
    return {
        "today_experience" : get_today_experience(session),
        "difference_from_yesterday" : get_difference_from_yesterday(session),
        "total_experience" : get_total_experience(session)
    }


def get_today_experience(session: Session) -> int:
    statement = select(func.coalesce(func.sum(ExperiencePoint.points), 0)).where(
        ExperiencePoint.created_at >= func.current_date(),
        ExperiencePoint.created_at < func.current_date() + text("INTERVAL '1 DAY'")
    )
    return session.exec(statement).one()  # SQLModelのSessionでクエリ実行


def get_yesterday_experience(session: Session) -> int:
    statement = select(func.coalesce(func.sum(ExperiencePoint.points), 0)).where(
        ExperiencePoint.created_at >= func.current_date() - text("INTERVAL '1 DAY'"),
        ExperiencePoint.created_at < func.current_date()
    )
    return session.exec(statement).one()


def get_difference_from_yesterday(session: Session) -> int:
    today_experience = get_today_experience(session)
    yesterday_experience = get_yesterday_experience(session)
    return today_experience - yesterday_experience

def get_total_experience(session: Session) -> int:
    total_experience = session.query(ExperiencePoint).all()
    return sum([experience.points for experience in total_experience])
