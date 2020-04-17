def solution(triangle):
    answer = 0
    arr = triangle[0]
    for i in range(1, len(triangle)):
        newArr = triangle[i].copy()
        for j in range(len(arr)):
            newArr[j] = max(triangle[i][j] + arr[j], newArr[j])
            newArr[j + 1] = max(triangle[i][j + 1] + arr[j], newArr[j + 1])
        arr = newArr
    answer = max(arr)
    return answer