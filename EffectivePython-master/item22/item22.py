from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items())

s = 'missispi'
d = defaultdict(int)
for k in s:
    d[k] += 1

print(d)

def constant_function(value):
    return lambda : value

d = defaultdict(constant_function('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)
print(d['go'])

print(d.get('non_exist'))
norm_d = dict()
print(norm_d.get('non_exist'))