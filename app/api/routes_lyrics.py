from fastapi import APIRouter, Query, HTTPException
from app.services.lyrics_service import fetch_lyrics

router = APIRouter()


@router.get("/")
def get_lyrics(
    query: str = Query(..., description="Song title and/or artist, e.g. 'Blinding Lights The Weeknd'"),
    synced_only: bool = Query(False, description="Only return time-synced LRC lyrics"),
    plain_only: bool = Query(False, description="Only return plain text lyrics"),
    lang: str = Query(None, description="ISO 639-1 language code for translation, e.g. 'en', 'ta', 'hi'"),
    enhanced: bool = Query(False, description="Request word-level karaoke synced lyrics if available"),
):
    """
    Fetch synced or plain lyrics for a given song.

    - Defaults to returning synced lyrics, falling back to plain if unavailable.
    - Use `synced_only=true` to strictly require LRC format.
    - Use `lang` for translated lyrics alongside the original.
    """
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