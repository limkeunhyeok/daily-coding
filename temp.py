def solution(phone_number):
    answer = ''
    cnt = len(phone_number) - 4
    for i in range(len(phone_number)):
        if i >= cnt:
            answer += phone_number[i]
        else:
            answer += '*'
    return answer