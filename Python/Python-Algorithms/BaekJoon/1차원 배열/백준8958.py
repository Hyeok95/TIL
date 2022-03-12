n = int(input())
for i in range(n):
  a = list(input())
  sum_score = 0
  score = 0
  for i in a:
    if i == "O":
      score +=1
      sum_score += score
    else:
      score = 0

  print(sum_score)
