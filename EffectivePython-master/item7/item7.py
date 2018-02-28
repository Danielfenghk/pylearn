a = list(range(10))
squares = [x**2 for x in a if x % 2 == 0]
print(squares)
chile_tanks = {'apple': 1, 'juice': 2, 'cattie': 3}
revert_tanks = {rank: name for name, rank in chile_tanks.items()}
print(revert_tanks)
print({len(name) for name in revert_tanks.values()})