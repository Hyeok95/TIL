#백준2798
from itertools import combinations

a,b  = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
for i in combinations(nums, 3):
  sum_nums = sum(i)
  if answer < sum_nums <= b:
    answer = sum_nums

print(answer)
