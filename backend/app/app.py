from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.crud import create_entry, get_entries
from app.db_and_models import YouTubeContent
from app.session import Session, create_db_and_tables, get_session


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/create_entry")
async def entry(entry: YouTubeContent, db: Session = Depends(get_session)):
    return await create_entry(content=entry, db=db)


@app.get("/entries")
async def read_entries(db: Session = Depends(get_session)):
    return await get_entries(db)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
