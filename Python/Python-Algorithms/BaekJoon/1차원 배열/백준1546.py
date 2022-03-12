n = int(input())
grades = list(map(int, input().split()))
Max = max(grades)

for i in range(n):
  grades[i] = grades[i] / Max *100

print("%.2f" %(sum(grades) / n))
