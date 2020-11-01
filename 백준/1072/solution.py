def solution(x, y):
    z = (100 * y) // x
    if z >= 99:
        return -1
    
    start = 0
    end = 1000000000
    while start <= end:
        mid = (start + end) // 2
        if ((y + mid) * 100) // (x + mid) > z:
            end = mid - 1
        else:
            start = mid + 1
    return end + 1

x, y = map(int, input().split(' '))
print(solution(x, y))

"""
수학적 접근 풀이
x, y = map(int, input().split(' '))

z = (100 * y) // x
if z >= 99:
    print(-1)
else:
    n, m = divmod((x * (z + 1)) - (100 * y), (99 - z))
    if m != 0:
        n += 1
    print(n)
"""