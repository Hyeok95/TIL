a1,a2 = map(int, input().split())
a = []

for i in range(a1):
  a.append(list(map(int, input().split())))

b1,b2 = map(int, input().split())
b = []

for i in range(b1):
  b.append(list(map(int, input().split())))

for n in range(a1):
  result = []
  for k in range(b2):
    temp = 0
    for m in range(a2):
      temp += a[n][m] * b[m][k]
    result.append(temp)
  print(*result)
  
# a[0][0] * b[0][0] + a[0][1] * b[1][0] / a[0][0] * b[0][1] + a[0][1] * b[1][1]
# a[2][0] * b[0][2] + a[2][1] * b[1][2]
