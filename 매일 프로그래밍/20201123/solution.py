# 단일 연결 리스트(singly linked list)가 주어지면 리스트의 중간 노드 값을 프린트 하시오. (제일 효율적인 방법으로)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        
def findMiddle(List):
    if List.head is None:
        print('-1')
    else:
        pt1 = List.head
        pt2 = List.head
        size = 1
        while pt1.next is not None:
            pt1 = pt1.next
            size += 1
        
        cnt = size // 2
        while cnt != 0:
            pt2 = pt2.next
            cnt -= 1
        print(pt2.data)
        
l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
findMiddle(l) # 3