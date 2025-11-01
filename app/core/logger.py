import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()]
    )
    return logging.getLogger("syncedlyrics")

def get_logger():
    return logging.getLogger("syncedlyrics")
