import logging

def test_log(file_path, message, level):
    logging.basicConfig(filename=file_path, format='[%(asctime)s] [%(levelname)s] %(message)s', level=logging.DEBUG)
    if level == "INFO":
        logging.info(message)
    elif level == "WARNING":
        logging.warning(message)
    elif level == "ERROR":
        logging.error(message)
    elif level == "CRITICAL":
        logging.critical(message)
    else:
        logging.debug(message)
