a,b,v = map(int, input().split())

count = 0
height = 0
while True:
  height += a
  count += 1

  if height == v:
    break
  height -=b
  
print(count)
