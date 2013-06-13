import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

streamHandler = logging.StreamHandler()
logger.addHandler(streamHandler)


def main():
    logger.info('main: started')

if __name__ == '__main__':
    main()
