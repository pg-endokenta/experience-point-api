from typing import Annotated

from fastapi import Header, HTTPException
from sqlmodel import Session
from app.core.db import engine
from fastapi import Depends


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
