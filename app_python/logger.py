import logging

def init_logger():    
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('app.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )

    logger.addHandler(fh)
    return logger
