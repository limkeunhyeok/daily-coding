from itertools import combinations

def isUnique(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True
    
# 2차원 배열 column 가져오기
def getColumn(arr_2d, comb):
    arr_1d = []
    for i in range(len(arr_2d)):
        temp = ''
        for j in range(len(comb)):
            temp += str(arr_2d[i][comb[j]])
        arr_1d.append(temp)
    return arr_1d
    
# 최소성을 만족하는 key의 갯수
def getMin(keys):
    arr = []
    check = []
    for i in range(len(keys)):
        s = ''
        for j in range(len(keys[i])):
            s += str(keys[i][j])
        arr.append(s)
        
    for i in range(len(arr)):
        check.append(True)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] in arr[j]:
                check[j] = False
    
    cnt = 0
    for i in check:
        if i == True:
            cnt += 1
    return cnt
                    
    
def solution(relation):
    element = 1
    rows = len(relation[0])
    keys = []
    while element <= rows:
        check_cols = list(combinations(range(rows),element))
        for i in range(len(check_cols)):
            cols = getColumn(relation,check_cols[i])
            if isUnique(cols):
                keys.append(check_cols[i])
        element += 1
    cnt = getMin(keys)
    return cnt