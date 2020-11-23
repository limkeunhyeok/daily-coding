# 0, 1, 2로 이루어진 배열을 가장 효율적으로 정렬 하시오. 시간복잡도 O(n).

def solution(arr):
    sortedArr = []
    index = 0
    for n in arr:
        if n == 0:
            sortedArr.insert(0, 0)
            index += 1
        elif n == 1:
            sortedArr.insert(index, 1)
        else:
            sortedArr.append(2)
    return sortedArr
