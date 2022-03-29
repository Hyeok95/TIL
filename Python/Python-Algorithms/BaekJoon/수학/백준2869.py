a,b,v = map(int, input().split())

# 시간초과 코드
# count = 0
# height = 0
# while True:
#   height += a
#   count += 1

#   if height == v:
#     break
#   height -=b
  
# print(count)

import math

a,b,v = map(int, input().split())
day = (v-b) /(a-b)
print(math.ceil(day))
