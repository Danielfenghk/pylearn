import json


class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args
        })


registry = {}


def register_class(target_class):
    name = target_class.__name__
    registry[name] = target_class


def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class RegisterSerializable(Serializable, metaclass=Meta):
    pass


class Point3D(RegisterSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Point3D(%d, %d, %d)' % (self.x, self.y, self.z)


if __name__ == '__main__':
    point = Point3D(1, 2, 3)
    data = point.serialize()
    print(data)
    point2 = deserialize(data)
    print(point2)
