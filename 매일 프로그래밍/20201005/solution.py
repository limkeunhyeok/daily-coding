class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def solution(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = solution(arr[:mid])
    root.right = solution(arr[mid + 1:])
    return root

def preOrder(root):
    if not root:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = solution(arr)
    preOrder(root)