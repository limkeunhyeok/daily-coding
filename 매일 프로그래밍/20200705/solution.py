# 정렬된 양수(positive integer) 배열이 주어지면, 배열 원소들의 합으로 만들수 없는 가장 작은 양수를 구하시오.
# 단, 시간복잡도는 O(n) 이여야 합니다.

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        if arr[i] <= answer:
            answer += arr[i]
        else:
            break
    return answer