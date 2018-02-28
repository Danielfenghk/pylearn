class RevealAccess(object):
    def __init__(self, initial=None, name='var'):
        self._val = initial
        self._name = name

    def __set__(self, instance, value):
        print('Updating ', self._name)
        self._val = value

    def __get__(self, instance, owner):
        print('Retriving ', self._name)
        return self._val


class Myclass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5


if __name__ == '__main__':
    m = Myclass()
    m.x
    m.x = 10
    m.x
    type(m).__dict__['x'].__get__(m, type(m))
    Myclass.__dict__['x'].__get__(None, Myclass)
    
