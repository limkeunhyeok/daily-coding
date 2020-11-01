from collections import defaultdict

def solution(tickets):
    d = defaultdict(list)
    tickets.sort()
    for ticket in tickets:
        d[ticket[0]].append(ticket[1])
    
    answer = []
    temp = ['ICN']
    while temp:
        if temp[-1] not in d.keys() or len(d[temp[-1]]) == 0:
            answer.append(temp.pop())
        else:
            temp.append(d[temp[-1]].pop(0))
    return answer[::-1]