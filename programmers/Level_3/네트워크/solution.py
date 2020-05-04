def solution(n, computers):
    connected = []
    for i in range(n):
        connected.append({i})

    for n1 in range(0, n):
        for n2 in range(n1+1, n):
            if computers[n1][n2]:
                for i in range(len(connected)):
                    if n1 in connected[i]:
                        index1 = i
                    if n2 in connected[i]:
                        index2 = i
                        
                if index1 != index2:
                    union = connected[index1] | connected[index2]
                    connected.pop(max(index1,index2))
                    connected.pop(min(index1,index2))
                    connected.append(union)
    return len(connected)