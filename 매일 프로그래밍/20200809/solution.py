class Queue:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []
        
    def enqueue(self, data):
        self.__s1.append(data)
    
    def dequeue(self):
        if len(self.__s1) == 0:
            print('empty')
            return
        while len(self.__s1) != 0:
            self.__s2.append(self.__s1.pop())
        
        data = self.__s2.pop()
        while len(self.__s2) != 0:
            self.__s1.append(self.__s2.pop())
        return data


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3
print(q.dequeue()) # 4
print(q.dequeue()) # 5