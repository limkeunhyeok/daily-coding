# 이진탐색트리안에 X보다 크고 Y보다 작은 모든 노드 값을 프린트 하시오.
# 20
# 8 22
# 4 12

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def solution(root, x, y):
    if root is None:
        return
    
    if x < root.data:
        solution(root.left, x, y)
        
    if x <= root.data and y >= root.data:
        print(root.data, end=" ")
    
    if y > root.data:
        solution(root.right, x, y)

        
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)

solution(root, 12, 25)
# 12 20 22