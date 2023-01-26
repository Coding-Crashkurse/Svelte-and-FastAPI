from app.db_and_models import YouTube, YouTubeContent
from app.session import Session


async def create_entry(content: YouTubeContent, db: Session):
    new_content = YouTube(
        image_url=f"https://img.youtube.com/vi/{content.image_url}/hq720.jpg",
        title=content.title,
        description=content.description,
        link=f"https://youtu.be/{content.image_url}",
    )
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return {"success": f"Eintrag mit ID {new_content.id} erstellt"}


async def get_entries(db: Session):
    entries = db.query(YouTube).all()
    return entries
