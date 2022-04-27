#백준11659

n,m = map(int, input().split())
array = list(map(int, input().split()))
num_sum = [0]

temp = 0
for arr in array:
  temp += arr
  num_sum.append(temp)

for k in range(m):
  i, j = map(int, input().split())
  print(num_sum[j] - num_sum[i-1])
