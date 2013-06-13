import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    logger.info('main: started')

if __name__ == '__main__':
    main()