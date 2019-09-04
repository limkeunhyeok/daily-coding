from itertools import combinations

# 내가 작성한 코드, 18, 19, 20, 22, 25 테스트 케이스 실패
class mysolution: 
    
    # 유일성 만족 체크
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


# 다른 사람이 작성한 코드
def other_solution(relation):
    answer = 0
    all = list()
    uniqeIndex = []
    
    if len(relation) > 0:
        cols = len(relation[0])
        rows = len(relation)
        
        for i in range(1, cols + 1):
            all.extend([set(k) for k in combinations([j for j in range(cols)], i)])

        for comb in all:
            vaildSet = set()
            for row in range(rows):
                temp = ''
                for col in comb:
                    temp += relation[row][col]
                vaildSet.add(temp)

            if len(vaildSet) == rows:
                uniqeIndex.append(comb)

    delSet = set()

    for stdMinElem in uniqeIndex:
        for idx, compMinElem in enumerate(uniqeIndex):
            if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
                delSet.add(uniqeIndex.index(compMinElem))
    answer = len(uniqeIndex)-len(delSet)
    return answer


# 예제 테스트
relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

print(mysolution.solution(relation))
print(other_solution(relation))