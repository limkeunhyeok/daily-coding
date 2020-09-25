# 단방향 연결 리스트(singly linked list)가 주어지면 총 합이 0으로 되는 연결된 노드들을 뺀 뒤 남은 노드의 값을 프린트 하시오.

def check(arr):
    for n in arr:
        if n < 0:
            return False
    return True

def solution(linkedList):
    temp = []
    cnt = len(linkedList) + 1
    
    if check(linkedList):
        return linkedList
    
    while True:
        cnt -= 1
        for i in range(len(linkedList) - cnt + 1):
            if sum(linkedList[i:i + cnt]) == 0:
                temp = linkedList[:i] + linkedList[i + cnt:]
                linkedList = temp
                cnt = len(linkedList) + 1
                break
        if check(linkedList):
            break
    return linkedList