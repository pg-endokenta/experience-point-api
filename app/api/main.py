from fastapi import APIRouter

from app.api.routes import experience_points

api_router = APIRouter()
api_router.include_router(experience_points.router)
