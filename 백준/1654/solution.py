def lineCutting(lines, length, N):
    cnt = 0
    for line in lines:
        cnt += line // length
    return cnt

def binary(lines, N):
    start, end = 1, max(lines)
    while start <= end:
        mid = (start + end) // 2
        cnt = lineCutting(lines, mid, N)
        if cnt >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

K, N = map(int, input().split())
lines = []
for _ in range(K):
    line = int(input())
    lines.append(line)

print(binary(lines, N))
