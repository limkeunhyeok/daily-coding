def solution(N):
    answer = [1, 1]
    for count in range(2, N + 1):
        answer.append(answer[-1] + answer[-2])
    return (answer[N] + answer[N - 1])*2