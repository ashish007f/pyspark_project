import logging

def get_logger(name):
    """
    Get a logger with the specified name.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(name)