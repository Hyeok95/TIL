nums = [int(input()) for i in range(10)]

temp = []
for num in nums:
  temp.append(num % 42)

temp = set(temp)
print(len(temp))
