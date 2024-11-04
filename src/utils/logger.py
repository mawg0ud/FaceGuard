import logging

def setup_logger(log_file: str):
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")
    return logging.getLogger()
