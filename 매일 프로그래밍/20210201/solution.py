# 정수 배열이 주어졌을때, 합이 0이 되는 모든 부분 배열을 출력하시오.
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
