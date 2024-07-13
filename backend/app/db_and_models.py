from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime


class PlaylistModel(SQLModel):
    id: Optional[str] = Field(default=None, primary_key=True)


class Playlist(PlaylistModel, table=True):
    __tablename__ = "playlist"
    playlist_ids: list["YouTube"] = Relationship(back_populates="playlist")


class YouTubeContent(SQLModel):
    video_id: str
    title: str
    link: str
    playlist_id: Optional[str] = Field(default=None, foreign_key="playlist.id")


class YouTube(YouTubeContent, table=True):
    __tablename__ = "youtube"
    id: Optional[int] = Field(default=None, primary_key=True)
    playlist: Optional[Playlist] = Relationship(back_populates="playlist_ids")


class UdemyContent(SQLModel):
    title: str
    video: str
    link: str
    description: str
    active_promotion: bool
    promo_until: Optional[datetime] = None


class Udemy(UdemyContent, table=True):
    __tablename__ = "udemy"
    id: Optional[int] = Field(default=None, primary_key=True)
