#중복조합
from itertools import combinations_with_replacement

n,m = map(int, input().split())

n = [x for x in range(1,n+1)]
array = list(combinations_with_replacement(n,m))

for i in array:
  for j in i:
    print(j, end=" ")
  print()
