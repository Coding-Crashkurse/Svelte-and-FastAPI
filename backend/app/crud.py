from sqlmodel import select
from fastapi import HTTPException
from datetime import datetime

from app.db_and_models import (
    YouTube,
    YouTubeContent,
    Playlist,
    PlaylistModel,
    Udemy,
    UdemyContent,
)
from app.session import Session


async def create_youtube_entry(content: YouTubeContent, db: Session):
    new_content = YouTube(
        video_id=f"https://i.ytimg.com/vi/{content.video_id}/hq720.jpg",
        title=content.title,
        link=f"https://youtu.be/{content.video_id}",
        playlist_id=content.playlist_id,
    )
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return {"success": f"Eintrag mit ID {new_content.id} erstellt"}


async def create_udemy_entry(content: UdemyContent, db: Session):
    new_content = Udemy(
        title=content.title,
        video=content.video,
        link=content.link,
        description=content.description,
        active_promotion=content.active_promotion,
        promo_until=content.promo_until,
    )
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return {"success": f"Entry with ID {new_content.id} created"}


async def update_udemy_entry(entry_id: int, content: UdemyContent, db: Session):
    existing_entry = db.get(Udemy, entry_id)
    if not existing_entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    existing_entry.title = content.title
    existing_entry.video = content.video
    existing_entry.link = content.link
    existing_entry.description = content.description
    existing_entry.active_promotion = content.active_promotion
    existing_entry.promo_until = content.promo_until

    db.commit()
    db.refresh(existing_entry)
    return {"success": f"Entry with ID {existing_entry.id} updated"}


async def delete_udemy_entry(entry_id: int, db: Session):
    existing_entry = db.get(Udemy, entry_id)
    if not existing_entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    db.delete(existing_entry)
    db.commit()
    return {"success": f"Entry with ID {entry_id} deleted"}


async def create_playlist_entry(playlist: PlaylistModel, db: Session):
    playlist_db = db.exec(select(Playlist).where(Playlist.id == playlist.id)).first()
    if playlist_db:
        raise HTTPException(status_code=403, detail="Playlist must be unique")
    new_playlist = Playlist(id=playlist.id)
    db.add(new_playlist)
    db.commit()
    db.refresh(new_playlist)
    return {"success": "Playlist created"}


async def get_videos_by_playlist(playlist_id: str, db: Session):
    playlist_db = db.exec(select(Playlist).where(Playlist.id == playlist_id)).first()
    if not playlist_db:
        raise HTTPException(status_code=404, detail="Playlist does not exist")
    entries = db.exec(select(YouTube).where(YouTube.playlist_id == playlist_id)).all()
    return entries


async def get_youtube_entries(db: Session):
    entries = db.query(YouTube).all()
    return entries


async def get_udemy_entries(db: Session):
    entries = db.query(Udemy).all()
    return entries


async def get_playlist(db: Session):
    entries = db.query(Playlist).all()
    return entries
