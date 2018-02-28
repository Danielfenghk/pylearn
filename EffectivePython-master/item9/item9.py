it = (int(x) for x in open('file.txt'))
roots = ((x, x**2) for x in it)
print(roots)
print(list(roots))