import os

from sqlmodel import Session, SQLModel, create_engine

# engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

async def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)