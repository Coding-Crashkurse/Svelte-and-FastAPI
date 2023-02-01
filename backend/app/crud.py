from app.db_and_models import YouTube, YouTubeContent, Playlist, PlaylistModel
from app.session import Session
from sqlmodel import select
from fastapi import HTTPException

async def create_entry(content: YouTubeContent, db: Session):
    new_content = YouTube(
        video_id=f"https://i.ytimg.com/vi/{content.video_id}/hq720.jpg",
        title=content.title,
        link=f"https://youtu.be/{content.video_id}",
        playlist_id=content.playlist_id
    )
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return {"success": f"Eintrag mit ID {new_content.id} erstellt"}


async def create_playlist_entry(playlist: PlaylistModel, db: Session):
    playlist_db = db.exec(select(Playlist).where(Playlist.id == playlist.id)).first()
    if playlist_db:
        raise HTTPException(status_code=403, detail="Playlist muss unique sein")
    new_playlist = Playlist(id=playlist.id)
    db.add(new_playlist)
    db.commit()
    db.refresh(new_playlist)
    return {"success": "Playlist erstellt"}


async def get_videos_by_playlist(playlist_id: str, db: Session):
    playlist_db = db.exec(select(Playlist).where(Playlist.id == playlist_id)).first()
    if not playlist_db:
        raise HTTPException(status_code=404, detail="Playlist existiert nicht")
    entries = db.exec(select(YouTube).where(YouTube.playlist_id == playlist_id)).all()
    return entries

async def get_entries(db: Session):
    entries = db.query(YouTube).all()
    return entries


async def get_playlist(db: Session):
    entries = db.query(Playlist).all()
    return entries
