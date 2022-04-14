#백준10773
n = int(input())
stack = []

for i in range(n):
  num = int(input())
  if num != 0:
    stack.append(num)
  elif num == 0:
    stack.pop()

if len(stack) == 0:
  print(0)
else:
  print(sum(stack))
