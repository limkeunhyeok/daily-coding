def solution(bag, k):
    answer = [0] * (k + 1)
    for i in range(len(bag)):
        for j in range(k, 1, -1):
            if bag[i][0] <= j:
                answer[j] = max(answer[j], answer[j - bag[i][0]] + bag[i][1])
    return answer[-1]

n, k = map(int, input().split())
bag = []
for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))

print(solution(bag, k))
