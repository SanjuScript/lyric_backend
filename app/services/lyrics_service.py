import syncedlyrics
from app.core.logger import get_logger

logger = get_logger()


def fetch_lyrics(
    query: str,
    synced_only: bool = False,
    plain_only: bool = False,
    lang: str = None,
    save_path: str = None,
    enhanced: bool = False,
):
    """
    Fetch lyrics (synced or plain) for a given song/artist query.

    Args:
        query:       Search term e.g. "Blinding Lights The Weeknd"
        synced_only: Only return time-synced (LRC) lyrics
        plain_only:  Only return plain text lyrics
        lang:        ISO 639-1 language code for translation, e.g. "de", "ta"
        save_path:   Optional path to save the .lrc file
        enhanced:    Request word-level (karaoke) synced lyrics if available
    """
    try:
        logger.info(f"Searching lyrics for: '{query}' | synced_only={synced_only} | lang={lang}")

        # syncedlyrics.search() takes the query as the first positional argument.
        # Optional kwargs are passed only when they carry a meaningful value.
        kwargs = {
            "synced_only": synced_only,
            "plain_only": plain_only,
            "enhanced": enhanced,
        }

        # Only add lang if provided — passing lang=None causes issues
        if lang:
            kwargs["lang"] = lang

        # Only add save_path if provided
        if save_path:
            kwargs["save_path"] = save_path

        lyrics = syncedlyrics.search(query, **kwargs)  # ✅ positional, not search_term=

        if not lyrics:
            logger.warning(f"No lyrics found for '{query}'")
            return None

        logger.info(f"Lyrics found for: '{query}'")
        return lyrics

    except Exception as e:
        logger.error(f"Error fetching lyrics for '{query}': {str(e)}")
        return None