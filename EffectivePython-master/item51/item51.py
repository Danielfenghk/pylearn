import mymodule


try:
    weight = mymodule.determine_weight(10, -1)
except mymodule.InvalidDensityError as e:
    print(e)
except mymodule.Error as e:
    print(e)