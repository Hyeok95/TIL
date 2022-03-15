#실버5 백준1427

a = map(int, input())

a2= sorted(a, reverse=True)

for i in a2:
  print(i, end='')
