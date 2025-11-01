# app/api/routes_lyrics.py
from fastapi import APIRouter, Query
from app.services.lyrics_service import fetch_lyrics

router = APIRouter()

@router.get("/")
def get_lyrics(
    query: str = Query(..., description="Song title and/or artist"),
    synced_only: bool = Query(True, description="Only get synced (LRC) lyrics"),
    lang: str = Query(None, description="Lyrics language, e.g. 'en', 'ta', 'hi'")
):
    """
    Fetch synced or plain lyrics for a given song.
    """
    lyrics = fetch_lyrics(query, synced_only=synced_only, lang=lang)

    if not lyrics:
        return {"error": f"No lyrics found for '{query}'"}

    return {"query": query, "lyrics": lyrics}
