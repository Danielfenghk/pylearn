def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ValueError from e

if __name__ == '__main__':
    a, b = 3, 0
    try:
        result = divide(a, b)
    except ValueError:
        print('Invalid inputs')
    else:
        print('Result is %1.f' % result)