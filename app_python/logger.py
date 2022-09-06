import logging
import os


# Initializes and returns the application logger
def init_logger():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('logs/app.log', mode="a")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )

    logger.addHandler(fh)
    return logger
