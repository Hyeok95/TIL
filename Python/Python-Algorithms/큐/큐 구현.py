class Queue:
    def __init__(self) :
        '''
        큐 myQueue을 만듭니다.
        '''
        self.myQueue = []

    def push(self, n) :
        '''
        queue에 정수 n을 넣습니다.
        '''
        self.myQueue.append(n)

    def pop(self) :
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.empty() == 1:
            return
        else:
            self.myQueue.pop(0)


    def size(self) :
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return len(self.myQueue)

    def empty(self) :
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.size == 0:
            return 1
        else:
            return 0


    def front(self) :
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1:
            return -1
        else:
            return self.myQueue[0]


    def back(self) :
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1:
            return -1
        else:
            return self.myQueue[-1]  
