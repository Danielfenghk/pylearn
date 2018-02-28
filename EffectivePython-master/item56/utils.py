def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode()
    else:
        raise TypeError('Must supply str or bytes, '
                        'found: %r' % data)
