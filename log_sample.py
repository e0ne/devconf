import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

streamHandler = logging.StreamHandler()

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(LOG_FORMAT)
streamHandler.setFormatter(formatter)

logger.addHandler(streamHandler)


def log_call(func):
    def wrapper(*args, **kwargs):
        log_entry = 'Function "{0}" called with params args={1}, kwargs={2}'\
            .format(func.func_name, args, kwargs)
        logger.debug(log_entry)
        func(*args, **kwargs)
    return wrapper


@log_call
def main(*args):
    logger.info('started')
    print('Hello DevConf')

if __name__ == '__main__':
    main(sys.argv)
