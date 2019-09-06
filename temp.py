# https://geonlee.tistory.com/71 참고

import functools
# 재귀함수 깊이 제한을 바꿈
import sys
sys.setrecursionlimit(10**6)

res_preorder = []
res_postorder = []
# 트리 노드의 구성
class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

# 전위 순회, C->L->R
def preorder(node):
    res_preorder.append(node.data[2])
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)

# 후위 순회, L->R->C
def postorder(node):
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    res_postorder.append(node.data[2])
    
# x축과 y축 구분하여 정렬
def compare(info1,info2):
    # y축 먼저 비교
    if info1[1] != info2[1]:
        return info2[1] - info1[1]
    # 같은 레벨이라면 x축 비교
    else:
        return info1[0] - info2[0]

def solution(nodeinfo):
    answer = []
    nodeinfo = [i + [idx+1] for idx, i in enumerate(nodeinfo)] # 노드 번호 매기기
    nodeinfo = sorted(nodeinfo, key=functools.cmp_to_key(compare)) # 레벨순 노드 정렬
    root = None
    
    # 트리 구성하기
    for node in nodeinfo:
        # root에 첫번째 노드 삽입
        if not root:
            root = Tree()
            root.data = node
        # 2번째 노드 부터
        else:
            x_node = node[0]
            Node = root
            # x좌표를 통해 left, right를 구분 
            while True:
                if x_node < Node.data[0]:
                    if Node.left != None:
                        Node = Node.left
                        continue
                    else:
                        Node.left = Tree()
                        Node.left.data = node
                        break
                if x_node > Node.data[0]:
                    if Node.right != None:
                        Node = Node.right
                        continue
                    else:
                        Node.right = Tree()
                        Node.right.data = node
                        break
                break
    
    preorder(root)
    postorder(root)
    answer.append(res_preorder)
    answer.append(res_postorder)
    return answer