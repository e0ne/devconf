import logging
import logging.config
import sys

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)


def log_call(func):
    def wrapper(*args, **kwargs):
        log_entry = 'Function "{0}" called with params args={1},' \
                    ' kwargs={2}'\
            .format(func.func_name, args, kwargs)
        logger.debug(log_entry)
        func(*args, **kwargs)
    return wrapper


def log_method_call(method):
    def wrapper(self, *args, **kwargs):
        logger.debug('Called method: {0}'.format(method))
        retval = getattr(self, '_logged_%s' % method)(*args, **kwargs)
        return retval
    return wrapper


class MetaLogger(type):
    def __new__(cls, classname, bases, classdict):
        for attr, item in classdict.items():
            if callable(item):
                classdict['_logged_%s' % attr] = item
                classdict[attr] = log_method_call(attr)

        return super(MetaLogger, cls).__new__(cls, classname, bases,
                                              classdict)


class VeryImportantClass(object):
    __metaclass__ = MetaLogger

    def output(self, message):
        print('Very important output: {0}'.format(message))


@log_call
def main(*args):
    logger.info('started')
    print('Hello DevConf')

    vic = VeryImportantClass()
    vic.output(':)')


if __name__ == '__main__':
    main(sys.argv)
