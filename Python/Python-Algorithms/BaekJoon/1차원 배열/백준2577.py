from collections import Counter

a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c)

count = Counter(mul)
for i in range(10):
  if str(i) in count.keys():
    print(count[str(i)])
  else:
    print(0)
