#실버3 백준2108
from collections import Counter

n = int(input())
nums = []
for i in range(n):
  num = int(input())
  nums.append(num)

#산술평균
a = round(sum(nums) / n)
print(int(a))

#중앙값
b1 = sorted(nums)
b2 = nums[n //2]
print(int(b2))

#최빈값
nums_s = Counter(nums).most_common() #개수가 많은 순으로 정렬
if len(nums_s) > 1:
  if nums_s[0][1] == nums_s[1][1]:
    print(nums_s[1][0])
  else:
    print(nums_s[0][0])
else:
  print(nums_s[0][0])

#범위
d = nums[-1] - nums[0]
print(d)
