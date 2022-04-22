#백준2164

from collections import deque

n = int(input())
q = deque([i for i in range(1, n+1)])

while (len(q) > 1):
  q.popleft()
  a = q.popleft()
  q.append(a)

print(q[0])
