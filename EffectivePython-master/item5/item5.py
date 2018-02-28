A = list(range(10))

B = A
C = A[:]
print('B before: ', B)
print('C before: ', C)
A[2:5] = [-1, -2]
print('B after:  ', B)
print('C after:  ', C)

