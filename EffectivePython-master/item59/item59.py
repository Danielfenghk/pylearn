import gc

found_objects = gc.get_objects()
print(len(found_objects))
x = list(range(10**8))
found_objects = gc.get_objects()
print(len(found_objects))
