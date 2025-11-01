# app/services/lyrics_service.py
import syncedlyrics
from app.core.logger import get_logger

logger = get_logger()

def fetch_lyrics(query: str, synced_only: bool = True, lang: str = None, save_path: str = None):
    """
    Fetch lyrics (synced or plain) for a given song/artist query.
    """
    try:
        logger.info(f"Searching lyrics for: {query} | lang={lang}")

        # Build correct arguments
        search_args = {
            "search_term": query,     
            "synced_only": synced_only,
            "save_path": save_path
        }

        if lang:
            search_args["lang"] = lang  

        # Call syncedlyrics properly
        lyrics = syncedlyrics.search(**search_args)

        if not lyrics:
            logger.warning(f"No lyrics found for '{query}'")
            return None

        logger.info(f"Lyrics found for: {query}")
        return lyrics

    except Exception as e:
        logger.error(f"Error fetching lyrics for {query}: {str(e)}")
        return None
