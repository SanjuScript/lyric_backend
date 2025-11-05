# app/api/routes_lyrics.py
from fastapi import APIRouter, Query
from app.services.lyrics_service import fetch_lyrics

router = APIRouter()

@router.get("/")
def get_lyrics(
    query: str = Query(..., description="Song title and/or artist"),
    lang: str = Query(None, description="Lyrics language, e.g. 'en', 'ta', 'hi'")
):
    """
    Fetch synced or plain lyrics for a given song.
    """
    lyrics = fetch_lyrics(query, synced_only=False, lang=lang)

    if not lyrics:
        return {"error": f"No lyrics found for '{query}'"}

    return {"query": query, "lyrics": lyrics}
