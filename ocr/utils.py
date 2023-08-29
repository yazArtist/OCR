import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
def log_info(message):
    logging.info(message)

def log_empty_line():
    logging.info("")