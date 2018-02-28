class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)


class Myclass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3

print('before class')
class Line(Polygon):
    print('before sides')
    sides = 1
    print('after sides')
print('after class')


if __name__ == '__main__':
    t = Triangle()
