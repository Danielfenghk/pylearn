from contextlib import contextmanager
import logging


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


if __name__ == '__main__':
    with log_level(logging.DEBUG, 'my-logger') as logger:
        logger.error('hello, world')
        logging.debug('hello from logging')
    logger = logging.getLogger('my-logger')
    logger.debug('hello')
    logger.error('oh-noooo')
