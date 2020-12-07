# 랜덤한 정수 배열이 주어지면 중복된 원소의 값을 모두 프린트 하시오.
# 단, 공간복잡도 O(1)이여야 합니다.

def solution(arr):
    temp = []
    answer = set()

    for n in arr:
        if n not in temp:
            temp.append(n)
        else:
            answer.add(n)
    return list(answer)