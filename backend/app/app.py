from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.crud import create_entry, get_playlist, get_entries, create_playlist_entry, get_videos_by_playlist
from app.db_and_models import YouTubeContent, PlaylistModel
from app.session import Session, create_db_and_tables, get_session

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/create_entry")
async def entry(entry: YouTubeContent, db: Session = Depends(get_session)):
    return await create_entry(content=entry, db=db)


@app.post("/create_playlist")
async def create_playlist(playlist: PlaylistModel, db: Session = Depends(get_session)):
    return await create_playlist_entry(playlist=playlist, db=db)


@app.get("/get_playlists")
async def playlist(db: Session = Depends(get_session)):
    return await get_playlist(db=db)


@app.get("/get_entries")
async def entry(db: Session = Depends(get_session)):
    return await get_entries(db=db)

@app.get("/get_videos_of_playlist/{playlist_id}")
async def videos_by_playlist(playlist_id: str, db: Session = Depends(get_session)):
    return await get_videos_by_playlist(playlist_id=playlist_id, db=db)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
