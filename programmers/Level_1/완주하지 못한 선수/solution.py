def solution(participant, completion):
    answer = {}
    for i in participant:
        if i in answer:
            answer[i] += 1
        else: 
            answer[i] = 1
        
    for j in completion:
        if j in answer:
            answer[j] -= 1
    for i in answer:
        if answer[i] > 0:
            return i