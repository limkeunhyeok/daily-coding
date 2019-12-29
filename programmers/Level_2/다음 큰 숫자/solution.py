def solution(n):
    value = cnt(binary_number(n))
    answer = n + 1
    ck = cnt(binary_number(answer))
    while(value != ck):
        answer += 1
        ck = cnt(binary_number(answer))
    print(answer)
    return answer

def binary_number(num):
    trans_num = ''
    while(num // 2 != 0):
        trans_num += str(num % 2)
        num = num // 2
        if num // 2 == 0:
            trans_num += str(num % 2)
    trans_num = trans_num[::-1]
    return trans_num

def cnt(trans_num):
    res = 0
    for i in range(len(trans_num)):
        if trans_num[i] == '1':
            res += 1
    return res