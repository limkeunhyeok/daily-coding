# 두개의 정렬된(sorted) 정수 링크드리스트(linked list)가 주어지면, 두 리스트를 합친 정렬된 링크드리스트를 만드시오.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        
    def show(self):
        if self.head is None:
            return False
        string = ''
        current = self.head
        while current.next is not None:
            string += str(current.value) + '->'
            current = current.next
        string += str(current.value)
        return string

def createLinkedList(string):
    newLinkedList = LinkedList()
    arr = string.split('->')
    for value in arr:
        newLinkedList.addNode(value)
    return newLinkedList
    
def solution(str1, str2):
    list1 = createLinkedList(str1)
    list2 = createLinkedList(str2)
    answer = LinkedList()
    data1 = list1.head
    data2 = list2.head
    
    while True:
        if data1 is not None and data2 is not None:
            if data1.value >= data2.value:
                answer.addNode(data2.value)
                if data2.next is None:
                    data2 = None
                else:
                    data2 = data2.next
            else:
                answer.addNode(data1.value)
                if data1.next is None:
                    data1 = None
                else:
                    data1 = data1.next
        elif data1 is None and data2 is not None:
            answer.addNode(data2.value)
            if data2 is not None and data2.next is None:
                data2 = None
            else:
                data2 = data2.next
        elif data2 is None and data1 is not None:
            answer.addNode(data1.value)
            if data1 is not None and data1.next is None:
                data1 = None
            else:
                data1 = data1.next
        else:
            break
    return answer.show()