def solution(num_list):
    add = []
    even = []

    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            add.append(num_list[i])
        else:
            even.append(num_list[i])
    
    answer = [len(even), len(add)]
    
    return answer
