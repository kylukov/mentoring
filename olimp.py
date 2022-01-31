from itertools import *

n = input()

array = []

for i in permutations(n):
    array.append(i)


if len(set(n)) == 1:
    print('0')
else: print(len(set(array[1:])))



