class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def swap(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp

def invertBinaryTree(root):
    if root is None:
        return
    swap(root)
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)


if __name__ == '__main__':
    """ Construct below tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    preorder(root)
    print('')
    
    invertBinaryTree(root)
    preorder(root)
