# 반복문 이용

import sys
import math

def getSubsum(data) :

    #모든 경우를 구하고, 가장 큰 값 출력.
    
    result= -math.inf
    
    for start in range(len(data)):
        for end in range(start, len(data)):
            temp = 0 #매 반복마다 새로운 값을 구해주어야 하므로 초기화
            for i in range(start, end+1):
                temp += data[i]
            result = max(result, temp)
    
    return result


data = [int(x) for x in input().split()]
print(getSubsum(data))
