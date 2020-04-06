# 링크드 리스트(linked list)의 머리 노드(head node)와 정수 N이 주어지면,
# 끝에서 N번째 노드(node)를 제거하고 머리 노드(head node)를 리턴하시오.
# 단, 리스트를 한번만 돌면서 풀어야합니다. N은 리스트 길이보다 크지 않습니다.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # 노드 추가
    def addNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            previous = current
            while current.next is not None:
                previous = current
                current = current.next
            current.next = newNode
    
    # 뒤에서 N번째 노드 삭제
    def deleteAtIndex(self, N):
        if self.head is None:
            return False
        else:
            first = self.head
            second = self.head
            for i in range(N):
                first = first.next
            if first is None:
                self.head = self.head.next
            else:
                while first.next is not None:
                    first = first.next
                    second = second.next
                second.next = second.next.next
    
    # 전체 리스트 출력
    def show(self):
        if self.head is None:
            return False
        string = ''
        current = self.head
        while current.next is not None:
            string += str(current.data) + '->'
            current = current.next
        string += str(current.data)
        return string
        

def solution(inputString, N):
    arr = inputString.split('->')
    l = LinkedList()
    for data in arr:
        l.addNode(data)
    l.deleteAtIndex(N)
    if not l.show():
        return 'Null'
    return l.show()


solution('1->2->3->4->5', 2)
solution('1->2->3', 3)
solution('1', 1)