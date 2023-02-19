import uvicorn
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from app.app import app

uvicorn.run(app, port=4000, host="127.0.0.1")
