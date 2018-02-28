class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, item):
        value = 'value for %s' % item
        setattr(self, item, value)
        return value


class LoggingLazyDB(LazyDB):
    def __getattr__(self, item):
        print('Called __getattr__(%s)' % item)
        return super().__getattr__(item)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, item):
        print('calling __getattribute__(%s)' % item)
        try:
            return super().__getattribute__(item)
        except AttributeError:
            value = 'value for %s' % item
            setattr(self, item, value)
            return value


class MissingPropertyDB(object):
    def __getattr__(self, item):
        if item == 'baditem':
            raise AttributeError('%s is missing' % item)


class SavingDB(object):
    def __setattr__(self, key, value):
        super().__setattr__(key, value)


class LoggingSavingDB(SavingDB):
    def __setattr__(self, key, value):
        print('Called __setattr__(%s, %r)' % (key, value))
        super().__setattr__(key, value)


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        data_dict = super().__getattribute__('_data')
        return data_dict[item]


if __name__ == '__main__':
    # data = LoggingLazyDB()
    data = MissingPropertyDB()
    print('exist', data.exists)
    print('foo:', data.foo)
    print('after:', data.foo)
    # print('baditem:', data.baditem)

    db = LoggingLazyDB()
    print('foo exists: ', hasattr(db, 'foo'))
    print('foo exists: ', hasattr(db, 'foo'))

    db = LoggingSavingDB()
    db.key = 5
    db.foo = 10

    db = DictionaryDB({'app': 2, 'good': 3})
    print(db.good)
    db.fuck