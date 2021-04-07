def solution(arr):
    d = {}
    for idx, num in enumerate(sorted(set(arr))):
        d[num] = idx
    
    answer = []
    for n in arr:
        answer.append(d[n])
    return answer

n = int(input())
arr = list(map(int, input().split()))
answer = solution(arr)
print(*answer)
