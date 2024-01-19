#####################################################################
# 로깅 모듈
#####################################################################

from utils.config import config
from logging import handlers
import logging

# config 
log_config = config.get_config("LOG")

# log settings
logFormatter = logging.Formatter('%(asctime)s,%(message)s')

# 로그 경로 세팅
log_path = log_config["LOG_PATH"]

# handler settings
log_handler = handlers.TimedRotatingFileHandler(log_path, when='midnight', interval=1, encoding='utf-8')
log_handler.setFormatter(logFormatter)
log_handler.suffix = log_config["SUFFIX"] 

# logger set
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)