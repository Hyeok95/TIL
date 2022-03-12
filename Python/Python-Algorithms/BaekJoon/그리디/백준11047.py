n, value = map(int, input().split())

money = [int(input()) for i in range(n)]
money = sorted(money, reverse=True)

count = 0
for i in range(n):
  count += value // money[i]
  value = value % money[i]

print(count)
