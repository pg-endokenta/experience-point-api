from typing import Annotated

from fastapi import Header, HTTPException
from sqlmodel import Session
from app.core.db import engine
from fastapi import Depends
from app.core.config import settings


async def get_token_header(access_token: Annotated[str, Header()]):
    if access_token != str(settings.ACCESS_TOKEN):
        raise HTTPException(status_code=400, detail="Access Token header invalid")

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
