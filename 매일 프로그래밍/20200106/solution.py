# 정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라
def solution(N):
    fibo = [0, 1]
    result = []
    while True:
        if fibo[-1] < N:
            fibo.append(fibo[-1] + fibo[-2])
            if fibo[-1] % 2 == 0:
                result.append(fibo[-1])
        else:
            break
    return sum(result)