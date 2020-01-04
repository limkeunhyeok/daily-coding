def solution(num):
    answer = 0
    while num != 1 and answer < 500:
        if num % 2 == 0:
            num = num / 2
            answer += 1
            continue
        else:
            num = 3 * num + 1
            answer += 1
            continue
    
    if answer == 500:
        return -1
    else:
        return answer