# 단방향 연결 리스트(Singly linked list)가 주어지면 O(n log n) 시간복잡도로 정렬하시오.

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
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode
    
    def sortedMerge(self, a, b): 
        result = None
        
        if a == None: 
            return b 
        if b == None: 
            return a 
              
        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result 

    def getMiddle(self, head): 
        if (head == None): 
            return head 
  
        slow = head 
        fast = head 
  
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
              
        return slow
      
    def mergeSort(self, h): 
        if h == None or h.next == None: 
            return h 
  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
  
        middle.next = None
        left = self.mergeSort(h) 
          
        right = self.mergeSort(nexttomiddle) 
  
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist 
        
def printList(head): 
	if head is None: 
		print(' ') 
		return
	curr_node = head 
	while curr_node: 
		print(curr_node.data, end = " ") 
		curr_node = curr_node.next
	print(' ') 

if __name__ == '__main__':
    l = LinkedList()
    l.append(3)
    l.append(1)
    l.append(5)
    l.append(2)
    l.append(7)
    printList(l.head)
    
    l.head = l.mergeSort(l.head)
    printList(l.head)
