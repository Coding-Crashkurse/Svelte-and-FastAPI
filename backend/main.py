import uvicorn

from app.app import app

uvicorn.run(app, port=4000, host="127.0.0.1")
