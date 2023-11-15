import logging
from pathlib import Path
from datetime import datetime

def getLogger(name):
    createFolder()
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    print_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    print_handler = logging.StreamHandler()
    print_handler.setLevel(logging.DEBUG)
    print_handler.setFormatter(print_format)
    logger.addHandler(print_handler)

    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler = logging.FileHandler('./logger/' + datetime.today().strftime('%m-%Y') + '/' + datetime.today().strftime('%d-%m-%Y') + ' Log.log')
    log_handler.setLevel(logging.DEBUG)
    log_handler.setFormatter(log_format)
    logger.addHandler(log_handler)
    
    return logger

def createFolder():
    Path("./logger/" + datetime.today().strftime('%m-%Y')).mkdir(parents=True, exist_ok=True)