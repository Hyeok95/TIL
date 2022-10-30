def solution(n):
    answer = []
    N = list(map(int, str(n)))
    for i in range(len(N)):
        answer.append(N[i])
        
        
    return sum(answer)
