import logging.config

LOG_TO_STDOUT = False
handlers = ['file']
if LOG_TO_STDOUT:
    handlers.append('console')

class ContainTextFilter(logging.Filter):
    def __init__(self, text):
        self.text = text
        super().__init__()

    def filter(self, record):
        allow = self.text not in record.msg
        return allow

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'filters': {
        'stream_dispatch': {
            '()': ContainTextFilter,
            'text': 'Dispatching'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
            'filters': ['stream_dispatch'],
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/codetalk-server.log',
            'maxBytes': 10485760,  # 10 MB
            'backupCount': 128,
            'formatter': 'standard',
            'filters': ['stream_dispatch'],
        }
    },
    'loggers': {
        '': {
            'handlers': handlers,
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
