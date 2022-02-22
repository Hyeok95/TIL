def getPower(m, n):
    
    if n == 0:
        return 1
    elif n % 2 ==0:
        temp = getPower(m, n//2)
        return (temp*temp)%LIMIT_NUMBER
    else:
        temp = getPower(m, (n-1)//2)
        return (temp*temp*m)%LIMIT_NUMBER
    
myList = [int(v) for v in input().split()]
print(getPower(myList[0], myList[1]))
