n = int(input())

for i in range(n):
    a, word = input().split()
    temp = ''
    for j in word:
        temp += int(a)*j
    print(temp)
