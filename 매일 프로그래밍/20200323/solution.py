# 정수 배열(int array)과 정수 N이 주어지면, N번째로 큰 배열 원소를 찾으시오.

# 정렬을 이용한 방법
# def solution(numbers, n):
#     numbers = sorted(numbers, reverse=True)
#     return numbers[n - 1]

def solution(numbers, n):
    for i in range(n - 1):
        numbers.remove(max(numbers))
    return max(numbers)