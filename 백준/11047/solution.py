def solution(N, K, A):
    answer = 0
    temp = 0
    
    while K > 0:
        coin = A.pop()
        answer += K // coin
        K %= coin
    return answer

N, K = map(int, input().split(' '))
A = []
for i in range(N):
    A.append(int(input()))

print(solution(N, K, A))
