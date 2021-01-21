# 정렬되지 않은 정수 배열과 정수 S가 주어졌을 때, 합이 S가 되는 정수 배열 내의 두 수를 찾으시오.

def solution(arr, s):
    answer = []
    length = len(arr)
    
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] + arr[j] == s:
                answer.append([arr[i], arr[j]])
    return answer