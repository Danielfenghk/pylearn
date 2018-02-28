# -*- coding: utf-8 -*-

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))

print('Red: ', my_values.get('red'))
print('Green: ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

red = int(my_values.get('green')[0] or 0)


# define helper functions
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found)
    else:
        found = default
    return found

green = get_first_int(my_values, 'green', 0)
print(green)