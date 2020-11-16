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
