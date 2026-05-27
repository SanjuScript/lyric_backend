import os
from fastapi import APIRouter, Query, HTTPException, Header
from app.services.lyrics_service import fetch_lyrics

router = APIRouter()
API_KEY = os.getenv("API_KEY", "a3f8c2e1b4d6e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4")


@router.get("/")
def get_lyrics(
    query: str = Query(..., description="Song title and/or artist, e.g. 'Blinding Lights The Weeknd'"),
    synced_only: bool = Query(False, description="Only return time-synced LRC lyrics"),
    plain_only: bool = Query(False, description="Only return plain text lyrics"),
    lang: str = Query(None, description="ISO 639-1 language code for translation, e.g. 'en', 'ta', 'hi'"),
    enhanced: bool = Query(False, description="Request word-level karaoke synced lyrics if available"),
    x_api_key: str = Header(...)
):
    """
    Fetch synced or plain lyrics for a given song.

    - Defaults to returning synced lyrics, falling back to plain if unavailable.
    - Use `synced_only=true` to strictly require LRC format.
    - Use `lang` for translated lyrics alongside the original.
    """
    if x_api_key != API_KEY:  
        raise HTTPException(status_code=401, detail="Unauthorized")
        
    if synced_only and plain_only:
        raise HTTPException(
            status_code=400,
            detail="Cannot use both synced_only and plain_only at the same time."
        )

    lyrics = fetch_lyrics(
        query=query,
        synced_only=synced_only,
        plain_only=plain_only,
        lang=lang,
        enhanced=enhanced,
    )

    if not lyrics:
        raise HTTPException(
            status_code=404,
            detail=f"No lyrics found for '{query}'. Try a different search term or provider."
        )

    return {
        "query": query,
        "lang": lang,
        "synced_only": synced_only,
        "plain_only": plain_only,
        "enhanced": enhanced,
        "lyrics": lyrics,
    }