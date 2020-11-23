# 이진 트리가 주어지면 루트 노드부터 레벨별로 프린트 하시오. 프린트 방식은 홀수 레벨은 왼쪽에서 오른쪽으로, 짝수 레벨은 오른쪽에서 왼쪽으로 프린트 하시오. 

from collections import defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = 1
        
class BST:
    def __init__(self):
        self.root = None
        self.d = defaultdict(list)
    
    def insert(self, data):
        newNode = Node(data)
        
        if self.root is None:
            self.root = newNode
            self.d[newNode.level].append(newNode.data)
        else:
            current = self.root
            while True:
                if data > current.data:
                    if current.right is None:
                        newNode.level += 1
                        current.right = newNode
                        self.d[newNode.level].append(newNode.data)
                        break
                    else:
                        current = current.right
                        newNode.level += 1
                else:
                    if current.left is None:
                        newNode.level += 1
                        current.left = newNode
                        self.d[newNode.level].append(newNode.data)
                        break
                    else:
                        current = current.left
                        newNode.level += 1


t = BST()
t.insert(7)
t.insert(5)
t.insert(10)
t.insert(3)
t.insert(6)
t.insert(8)
t.insert(12)
# 7
# 5 10
# 3 6 8 12

d = t.d
answer = []
for key in d.keys():
    if key % 2 == 1:
        answer += d[key]
    else:
        answer += sorted(d[key], reverse = True)
        
print(answer)