#백준 3009

num_a = []
num_b = []
for i in range(3):
  a,b = map(int, input().split())
  num_a.append(a)
  num_b.append(b)

for i in range(3):
  if num_a.count(num_a[i]) == 1:
    a4 = num_a[i]
  if num_b.count(num_b[i]) == 1:
    b4 = num_b[i]

print(a4, b4)
