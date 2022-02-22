import sys
import math

def mergeSort(data) :

    if len(data) <= 1:
        return data
    
    mid = len(data)//2
    
    #왼쪽기준 정렬
    left = mergeSort(data[:mid])
    #오른쪽기준 정렬
    right = mergeSort(data[mid:])
    
    leftPtr = 0
    rightPtr = 0
    result = []
    
    while leftPtr < len(left) or rightPtr < len(right):
        leftValue = left[leftPtr] if leftPtr < len(left) else math.inf
        rightValue = right[rightPtr] if rightPtr < len(right) else math.inf
        
        if leftValue < rightValue:
            result.append(leftValue)
            leftPtr +=1
        else:
            result.append(rightValue)
            rightPtr +=1
            
    return result
    

data = [int(x) for x in input().split()]

print(*mergeSort(data))
