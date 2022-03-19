#백준1978

n = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
  if num != 1:
    for i in range(2, num):
      if num % i == 0:
        break
    else:
      count +=1
print(count)
