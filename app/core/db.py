from sqlmodel import create_engine
from sqlmodel import SQLModel

from app.core.config import settings

engine = create_engine(str(settings.DATABASE_URL))

def create_db_and_tables():
    """Create the database and tables if they don't exist."""
    SQLModel.metadata.create_all(engine)
