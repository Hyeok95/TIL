def factorial(n):
  num = 1
  for i in range(1,n+1):
    num *=i
  return num

n = int(input())
for i in range(n):
  n,m = map(int, input().split())
  bridge = factorial(m) // (factorial(m-n) * factorial(n))
  print(bridge)
