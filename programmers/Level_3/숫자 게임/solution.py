def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    while A:
        data = A[0]
        if data >= B[0]:
            A.pop(0)
        else:
            answer += 1
            A.pop(0)
            B.pop(0)
    return answer