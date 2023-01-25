from fastapi import Depends, FastAPI

from app.crud import create_entry
from app.db_and_models import YouTubeContent
from app.session import Session, create_db_and_tables, get_session

app = FastAPI()


@app.post("/create_entry")
async def entry(entry: YouTubeContent, db: Session = Depends(get_session)):
    return await create_entry(content=entry, db=db)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
