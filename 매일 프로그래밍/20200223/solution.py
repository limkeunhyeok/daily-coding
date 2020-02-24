# 정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오.
# 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.
# lazy evaluation

def solution(arr):
    answer = []
    for num in generator(arr):
        answer.append(num)
    answer.extend([0 for _ in range(len(answer), len(arr))])
    return answer

def generator(arr):
    for num in arr:
        if num != 0:
            yield num