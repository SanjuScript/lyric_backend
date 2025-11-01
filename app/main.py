from fastapi import FastAPI
from app.api import routes_lyrics
from app.core import logger

logger = logger.setup_logger()

app = FastAPI(title="Synced Lyrics API", version="1.0")

app.include_router(routes_lyrics.router, prefix="/lyrics", tags=["Lyrics"])

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Synced Lyrics API is running 🚀"}
