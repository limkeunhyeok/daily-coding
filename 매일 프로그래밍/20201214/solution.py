# L0→L1→…→Ln-1→Ln 의 단일 연결 리스트가 주어지면 순서를 다음과 같이 바꾸시오: L0→Ln→L1→Ln-1→L2→Ln-2→…

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
    
    def pop(self):
        if self.head is None:
            return 'empty'
        else:
            current = self.head
            previous = current
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            return current.data
    
    def getLength(self):
        answer = 0
        current = self.head
        while current is not None:
            answer += 1
            current = current.next
        return answer
    
    def toList(self):
        answer = []
        current = self.head
        while current is not None:
            answer.append(current.data)
            current = current.next
        return answer
    
    def show(self):
        if self.head is None:
            print('empty')
        else:
            answer = ''
            current = self.head
            while current is not None:
                answer += str(current.data) + ' => '
                current = current.next
            print(answer)
    
    def solution(self):
        toList = self.toList()
        length = self.getLength()
        newLinkedList = LinkedList()
        for i in range(length // 2):
            if i != length - i:
                newLinkedList.push(toList[i])
                newLinkedList.push(toList[length - i - 1])
            else:
                newLinkedList.push(toList[i])
        if length % 2 == 1:
            newLinkedList.push(toList[length // 2])
        self.head = newLinkedList.head

if __name__ == "__main__":
    t1 = LinkedList()
    t2 = LinkedList()

    t1.push(1)
    t1.push(2)
    t1.push(3)
    t1.push(4)
    t2.push(1)
    t2.push(2)
    t2.push(3)

    t1.show()
    t2.show()

    t1.solution()
    t2.solution()

    t1.show()
    t2.show()