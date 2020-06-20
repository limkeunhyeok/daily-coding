def solution(routes):
    routes.sort()
    l = len(routes)
    answer = 0
    camera = [0] * l
    current = 0
    
    for i in range(l - 1, -1, -1):
        if camera[i] == 0:
            current = routes[i][0]
            answer += 1
        for j in range(i, -1, -1):
            if camera[j] == 0 and routes[j][1] >= current:
                camera[j] = 1
    return answer
