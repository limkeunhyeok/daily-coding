def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for c in new_id:
        if c.isalnum() or c in '-_.':
            answer += c
            
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    answer = 'a' if answer == '' else answer
    
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    elif len(answer) <= 2:
        answer = answer + answer[-1] * (3-len(answer))
    return answer
