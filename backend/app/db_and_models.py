from typing import Optional

from sqlmodel import Field, SQLModel


class YouTubeContent(SQLModel):
    video_id: str
    title: str
    description: str


class YouTube(YouTubeContent, table=True):
    __tablename__ = "youtube"
    link: str

    id: Optional[int] = Field(default=None, primary_key=True)
