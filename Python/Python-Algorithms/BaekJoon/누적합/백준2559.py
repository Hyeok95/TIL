#백준2559
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
array = list(map(int, input().split()))

result = []
result.append(sum(array[:k]))

for i in range(n-k):
  result.append(result[i] - array[i] + array[k+i])

print(max(result))
