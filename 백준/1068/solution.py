"""
반례
n = 2, node = [-1, 0], remove_node = 1
출력 1
"""

def tree(n, node):
    answer = {}
    for i in range(n):
        answer[i] = []

    for i, v in enumerate(node):
        if v == -1:
            continue
        answer[v].append(i)
    return answer

def solution(tree, remove_node):
    q = [remove_node]
    while q:
        node = q.pop(0)
        if node in tree:
            q += tree[node]
            del tree[node]
    
    # 반례때문에 추가한 코드    
    for key in tree.keys():
        for node in tree[key]:
            if node not in tree:
                tree[key].remove(node)
    answer = 0
    for key in tree.keys():
        if len(tree[key]) == 0:
            answer += 1
    return answer

n = int(input())
node = list(map(int, input().split(' ')))
remove_node = int(input())

tree = tree(n, node)
print(solution(tree, remove_node))