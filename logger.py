import os
import logging
from logging.handlers import WatchedFileHandler

logger = logging.getLogger()

if 'LOG_LEVEL' in os.environ:
    # Expects integer value log level env variable (ie. 10 for debug, 20 for info, etc...)
    logger.setLevel(int(os.environ['LOG_LEVEL']))
else:
    logger.setLevel(logging.INFO)

try:
    ch = WatchedFileHandler('logs/application.log')
except FileNotFoundError:
    print("Logging to console")
    ch = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)7s-%(levelname)s-%(funcName)s():%(lineno)i-%(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
