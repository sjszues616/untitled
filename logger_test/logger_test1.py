import logging
import os
import sys

import logger_test
from logger_test import setting

BasePath =os.path.dirname(os.getcwd())
print(BasePath)
sys.path.insert(0,BasePath)
# logging.basicConfig(filename='example.log',level=logging.WARN)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

#
# logger = logging.getLogger('__name__')
# logger.setLevel(logging.DEBUG)
#
# log_path = os.getcwd() +'/logs/'
# log_name = log_path + 'log.log'
# logfile = log_name
# file_hander = logging.FileHandler(logfile,mode='a+')
# file_hander.setLevel(logging.ERROR)
#
# formatter = logging.Formatter(("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))
# f
# ile_hander.setFormatter(formatter)
# logger.addHandler(file_hander)
#
# print_handler = logging.StreamHandler()
# print_handler.setFormatter(formatter)
# logger.addHandler(print_handler)

DEBUG = True
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s,%(process)d,%(name)s,%(levelname)s,%(filename)s:%(lineno)d,%(message)s'
#         },
#     },
#     'filters': {
#     },
#     'handlers': {
#         'default': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(os.path.curdir, 'all.log'),
#             'maxBytes': 1024 * 1024 * 50,  # 50 MB
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'console': {
#             'level': 'ERROR',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default', 'console'] if DEBUG else ["default"],
#             'level': 'ERROR',
#             'propagate': False
#         },
#         '': {
#             'handlers': ['default', 'console'] if DEBUG else ["default"],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#     }
# }
# logger.info('info')
import logging.config
logging.config.dictConfig(setting.LOGGING)
logger12 = logging.getLogger('django')
logger_other = logging.getLogger('test2')



try:
    raise ValueError
except Exception as e:
    logger12.error('234')
    logger_other.error('orther')
