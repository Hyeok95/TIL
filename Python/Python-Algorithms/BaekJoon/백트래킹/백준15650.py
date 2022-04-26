#순열
from itertools import permutations

n,m = map(int, input().split())

n = [x for x in range(1,n+1)]
array = list(permutations(n,m))

for i in array:
  for j in i:
    print(j, end=" ")
  print()
