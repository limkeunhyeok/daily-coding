def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    length = len(A)
    
    for i in range(length):
        answer += A[i] * B[length - 1 - i]
    return answer