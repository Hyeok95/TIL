#실버5 백준11650

n = int(input())

answer = []
for i in range(n):
  x,y = map(int, input().split())
  answer.append((x,y))

answer.sort()

for j in range(n):
  print(answer[j][0], answer[j][1])
