#백준10816
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

count = {}
for i in a:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1

for j in b:
  result = count.get(j)
  if result == None:
    print(0, end=" ")
  else:
    print(result, end=" ")
