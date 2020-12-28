# 정수 배열이 주어졌을 때, 중복된 값이 들어 있지 않고 연속된 정수로 구성된 가장 긴 부분 배열을 구하시오.

def solution(arr):
    answer = []
    start, end = 0, 0
    
    while end != len(arr) and start <= end:
        if end - start + 1 == len(set(arr[start:end + 1])):
            end += 1
        else:
            if len(answer) < len(set(arr[start:end])):
                answer = arr[start:end]
            start += 1
    return answer