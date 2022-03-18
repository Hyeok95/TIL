a, b = map(int, input().split())
nums = list(map(int, input().split()))

for num in nums:
  if num < b:
    print(num, end=" ")
