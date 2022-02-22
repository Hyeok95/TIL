#배열

class ListPipe:
    def __init__(self) :
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        self.myPipe = []
        
    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        self.myPipe.insert(0, n)

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        self.myPipe.append(n)

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        return self.myPipe


def processBeads(myInput) :
    myPipe = ListPipe()
    
    for bead, direction in myInput:
        if direction == 0:
            myPipe.addLeft(bead)
        else:
            myPipe.addRight(bead)
    
    result = myPipe.getBeads()
    
    return result

n = int(input())

myList = []

for i in range(n) :
    myList.append([int(v) for v in input().split()])

print(*processBeads(myList))
