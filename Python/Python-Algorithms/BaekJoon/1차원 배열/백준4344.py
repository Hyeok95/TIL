n = int(input())
for i in range(n):
  m = list(map(int, input().split()))
  avg = sum(m[1:]) / m[0]
  count = 0
  for i in range(1, len(m)):
    if m[i] > avg:
      count +=1
  rate = (count / m[0]) * 100
  print(f'{rate:.3f}%')
