# -*- coding: utf-8 -*-


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


if __name__ == '__main__':
    s = 'hello'
    b = b'hello'
    print(type(s))
    print(type(b))
    print(to_bytes(s))
    print(to_str(b))