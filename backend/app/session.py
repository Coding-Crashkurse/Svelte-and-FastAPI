import os

from sqlmodel import Session, SQLModel, create_engine


async def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/mydb"
)
engine = create_engine(DATABASE_URL)
