def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    connected = [0] * n
    connected[0] = 1

    while sum(connected) != n:
        for cost in costs:
            s, e, c = cost
            if connected[s] or connected[e]:
                if connected[s] and connected[e]:
                    continue
                else:
                    connected[s] = 1
                    connected[e] = 1
                    answer += c
                    break
    return answer