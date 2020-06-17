def solution(n, stations, w):
    answer = 0
    dist = []
    f = 0
    for i in range(len(stations)):
        r = stations[i] - w - 1
        dist.append(r - f)
        f = stations[i] + w
        if f > n: break
        if len(stations) - 1 == i: dist.append(n - f)
        
    for num in dist:
        d, m = divmod(num, (2 * w + 1))
        if m:
            answer += d + 1
        else:
            answer += d
    return answer