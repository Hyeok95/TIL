#재귀 이용

import sys

def getPowerSet(n,k):
    '''
    1부터 n까지의 자연수의 원소가 있을 때 k를 가장 처음으로 선택하는경우 반환

    getPowerSet(3,1)
    [[1]       [1,2][1,2,3]     [1,3]]
    temp = [[2] [2,3]]
    
    getPowerSet(3,2)
    [[2]    [2,3]]
    temp = [[3]]
    '''
    if n==k:
        return [[k]]
        
    result = [[k]]
    temp = []
    
    #if k == 1, temp = [[2],[2,3],[3]]
    for i in range(k+1, n+1):
        temp = temp + getPowerSet(n, i)
    
    #k값을 temp값위치에 더한다.
    for i in range(len(temp)):
        temp[i] = [k] + temp[i]
    
    return result + temp

def powerSet(n) :
    '''
    n개의 원소를 가지는 집합 A의 멱집합의 원소를 사전 순서대로 list로 반환하는 함수를 작성하시오.

    예를 들어, n = 3 일 경우 다음의 list를 반환한다.

    [ [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3] ]
    
    >> n=3일 때
    
    getPowerSet(3,1)+getPowerSet(3,2)+getPowerSet(3,3)
    '''
    #재귀호출
    result = []
    for i in range(1, n+1):
        result += getPowerSet(n, i)
    
    return result

n = int(input())

result = powerSet(n)
    
for line in result :
    print(*line)
