import heapq

def solution(operations):
    answer = []
    
    for text in operations:
        command = text.split(' ')
        if command[0] == 'I':
            heapq.heappush(answer, int(command[1]))
        else:
            if answer:
                if command[1] == '1':
                    answer.pop()
                else:
                    heapq.heappop(answer)
            else:
                continue
                
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]