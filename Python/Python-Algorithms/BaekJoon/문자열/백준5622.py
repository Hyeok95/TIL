a = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'NMO', 'PQRS', 'TUV', 'WXYZ']
num = 0

for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            num += dial.index(j)+3
print(num)
            
