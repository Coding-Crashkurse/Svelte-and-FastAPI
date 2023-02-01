from typing import Optional

from sqlmodel import Field, SQLModel, Relationship


class PlaylistModel(SQLModel):
    id: Optional[str] = Field(default=None, primary_key=True)


class Playlist(PlaylistModel, table=True):
    __tablename__ = "playlist"

    playlist_ids: list["YouTube"] = Relationship(back_populates="playlist")


class YouTubeContent(SQLModel):
    video_id: str
    title: str
    playlist_id: Optional[str] = Field(default=None, foreign_key="playlist.id")


class YouTube(YouTubeContent, table=True):
    __tablename__ = "youtube"
    link: str

    id: Optional[int] = Field(default=None, primary_key=True)
    playlist: Optional[Playlist] = Relationship(back_populates="playlist_ids")

