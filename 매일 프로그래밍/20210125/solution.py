# 정수 배열이 주어졌을 때, 부분 배열(sub-array)의 합이 0이 될 수 있는지 확인하시오.
# 부분 배열은 배열 내의 연속된 원소들의 집합입니다.

def solution(arr):
    answer = []
    length = len(arr)
    
    for i in range(length):
        temp = i
        for j in range(length - i):
            if sum(arr[j:temp + j + 1]) == 0:
                answer.append(arr[j:temp + j + 1])
    return answer