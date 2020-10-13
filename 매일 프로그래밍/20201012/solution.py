class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def solution(node):
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return solution(node.left) + solution(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(solution(root)) # 3

root.right.left = Node(6)
root.right.right = Node(7)
print(solution(root)) # 4