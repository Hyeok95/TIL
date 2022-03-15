#실버5 백준11651

n = int(input())

answer = []
for i in range(n):
  x,y = map(int, input().split())
  answer.append((x,y))

answer.sort(key= lambda x: (x[1], x[0]))

for j in range(n):
  print(answer[j][0], answer[j][1])
