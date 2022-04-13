n = int(input())

for i in range(n):
  temp = []
  c = input()
  s = list(c) 
  for i in s:
    if i == "(":
      temp.append(i)
    elif i == ")":
      if len(temp) !=0 and temp[-1] == "(":
        temp.pop()
      else:
        temp.append(")")
        break
  
  if len(temp) == 0:
    print("YES")
  else:
    print("NO")
