#실버2 백준18870

n = int(input())
lst = list(map(int, input().split()))
lst2 = sorted(list(set(lst)))

dic = {lst2[x] : x for x in range(len(lst2))}
for i in lst:
  print(dic[i], end=" ")
