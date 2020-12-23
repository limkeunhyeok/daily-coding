class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
     def __init__(self):
        self.head = None
    
    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            
            while node.next:
                node = node.next
                
            temp = Node(data)
            node.next = temp
            temp.prev = node
    
    def descend(self):
        node = self.head
        
        while node:
            print(node.data)
            node = node.next
    
    def delete(self, data):
        if self.head == None:
            return False
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
        
        else:
            node = self.head

            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    
                    if node.next == None:
                        pass
                    else:
                        node.next.prev = node
                    
                    del temp
                
                else:
                    node = node.next