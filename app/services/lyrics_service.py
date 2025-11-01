import syncedlyrics
from app.core.logger import get_logger

logger = get_logger()

def fetch_lyrics(query: str, synced_only: bool = True, save_path: str = None):
    """
    Fetch lyrics (synced or plain) for a given song/artist query.
    """
    try:
        logger.info(f"Searching lyrics for: {query}")

        # Call syncedlyrics library
        lyrics = syncedlyrics.search(
            query,
            synced_only=synced_only,
            save_path=save_path
        )

        if not lyrics:
            logger.warning(f"No lyrics found for '{query}'")
            return None

        logger.info(f"Lyrics found for: {query}")
        return lyrics

    except Exception as e:
        logger.error(f"Error fetching lyrics for {query}: {str(e)}")
        return None
