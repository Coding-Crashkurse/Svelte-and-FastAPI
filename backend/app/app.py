from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os

from app.crud import (
    create_youtube_entry,
    create_udemy_entry,
    update_udemy_entry,
    delete_udemy_entry,
    get_playlist,
    get_youtube_entries,
    get_udemy_entries,
    create_playlist_entry,
    get_videos_by_playlist,
)
from app.db_and_models import YouTubeContent, UdemyContent, PlaylistModel
from app.session import Session, create_db_and_tables, get_session

app = FastAPI()

# Single user credentials from environment variables
USERNAME = os.getenv("AUTH_USERNAME", "user")
PASSWORD = os.getenv("AUTH_PASSWORD", "password")

security = HTTPBasic()


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/create_youtube_entry")
async def create_youtube(
    content: YouTubeContent,
    db: Session = Depends(get_session),
    username: str = Depends(authenticate),
):
    return await create_youtube_entry(content=content, db=db)


@app.post("/create_udemy_entry")
async def create_udemy(
    content: UdemyContent,
    db: Session = Depends(get_session),
    username: str = Depends(authenticate),
):
    return await create_udemy_entry(content=content, db=db)


@app.put("/update_udemy_entry/{entry_id}")
async def update_udemy(
    entry_id: int,
    content: UdemyContent,
    db: Session = Depends(get_session),
    username: str = Depends(authenticate),
):
    return await update_udemy_entry(entry_id=entry_id, content=content, db=db)


@app.delete("/delete_udemy_entry/{entry_id}")
async def delete_udemy(
    entry_id: int,
    db: Session = Depends(get_session),
    username: str = Depends(authenticate),
):
    return await delete_udemy_entry(entry_id=entry_id, db=db)


@app.post("/create_playlist")
async def create_playlist(
    playlist: PlaylistModel,
    db: Session = Depends(get_session),
    username: str = Depends(authenticate),
):
    return await create_playlist_entry(playlist=playlist, db=db)


@app.get("/get_playlists")
async def playlist(
    db: Session = Depends(get_session), username: str = Depends(authenticate)
):
    return await get_playlist(db=db)


@app.get("/get_youtube_entries")
async def youtube_entries(
    db: Session = Depends(get_session), username: str = Depends(authenticate)
):
    return await get_youtube_entries(db=db)


@app.get("/get_udemy_entries")
async def udemy_entries(
    db: Session = Depends(get_session), username: str = Depends(authenticate)
):
    return await get_udemy_entries(db=db)


@app.get("/get_videos_of_playlist/{playlist_id}")
async def videos_by_playlist(
    playlist_id: str,
    db: Session = Depends(get_session),
    username: str = Depends(authenticate),
):
    return await get_videos_by_playlist(playlist_id=playlist_id, db=db)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
