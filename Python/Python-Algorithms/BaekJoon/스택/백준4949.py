#백준4949

while True:
  a = input()
  if a == ".":
    break
  
  stack = []
  temp = True
  for i in a:
    if i == "(" or i == "[":
      stack.append(i)
    elif i == ")":
      if not stack or stack[-1] == "[":
        temp = False
      elif stack[-1] == "(":
        stack.pop()
    elif i == "]":
      if not stack or stack[-1] == "(":
        temp = False
      elif stack[-1] == "[":
        stack.pop()
  
  if temp == True and not stack:
    print("yes")
  else:
    print("no")
