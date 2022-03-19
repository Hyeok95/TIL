a = int(input())
b = int(input())

nums = []
for num in range(a, b+1):
  if num != 1:
    for i in range(2, num):
      if num % i == 0:
        break
    else:
      nums.append(num)

if len(nums) > 0:
  print(sum(nums))
  print(min(nums))
else:
  print(-1)
