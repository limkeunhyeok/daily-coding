# 주어진 정수를 2진법으로 나타내었을때 1의 갯수를 리턴하시오.
# 시간 복잡도: O(log n)

def solution(n):
    answer = 0
    
    while n != 1:
        n, m = divmod(n, 2)
        if m == 1:
            answer += 1
    return answer + 1

def anotherSolution(n):
    answer = 0
    while n:
        answer += n & 1
        n >>= 1
    return answer