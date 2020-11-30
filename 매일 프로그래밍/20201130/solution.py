# 연결 리스트로 표현된 두 정수 A 와 B 가 있습니다.
# A 와 B 를 더한 결과를 연결 리스트로 리턴하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, data):
        num = list(map(int, str(data)[::-1]))
        self.head = Node(num.pop(0))
        current = self.head
        while num:
            newNode = Node(num.pop(0))
            current.next = newNode
            current = current.next
    
    def convert(self):
        if self.head is None:
            return 0
        else:
            answer = ''
            current = self.head
            while current.next is not None:
                answer += str(current.data)
                current = current.next
            answer += str(current.data)
            return int(answer[::-1])
    
    def show(self):
        if self.head is None:
            print('empty')
        else:
            answer = ''
            current = self.head
            while current.next is not None:
                answer += str(current.data) + '->'
                current = current.next
            answer += str(current.data)
            print(answer)
        
        
        
first = LinkedList()
first.add(651)
first.show()

second = LinkedList()
second.add(400)
second.show()

res = LinkedList()
res.add(first.convert() + second.convert())
res.show()