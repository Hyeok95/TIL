#백준2751
import sys
n = int(input())

nums = []
for i in range(n):
  nums.append(int(sys.stdin.readline()))

srt_nums = sorted(nums)

for i in range(1, len(srt_nums)+1):
  print(i)
