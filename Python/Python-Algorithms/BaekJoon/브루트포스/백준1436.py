n = int(input())
six_n = 666
count = 0

while True:
    if '666' in str(six_n):   #1 n번째 수에 '666'이 포함되어 있다면(str이 아니면 무조건 1의자리부터 시작하니까)
        count+=1               #2 카운트를 올려라
    if count == n:          #4 카운트랑 n번째 수가 같다면 
        print(six_n)           #5 nth를 출력하고
        break               #6 while문을 종료해라
    six_n+=1  
