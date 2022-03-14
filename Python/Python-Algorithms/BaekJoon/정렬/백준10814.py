n = int(input())

user = []
for i in range(n):
  user.append(list(input().split()))

user.sort(key=lambda x:int(x[0]))
for i in range(n):
  print(user[i][0], user[i][1])
