from datetime import datetime
from time import sleep
import json


def log(message, when=None):
    """Log a message with a timestamp
    
    Args:
        message: Message to print
        when: date time of when the message is occured.
        Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))


def decode(data, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


if __name__ == '__main__':
    log('hello')
    sleep(2)
    log('world')

    foo = decode('bad data')
    foo['stuff'] = 22
    bar = decode('bad again')
    bar['zoo'] = 33
    print(foo)
    print(bar)