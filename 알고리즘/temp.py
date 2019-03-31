def solution(n):
    value = cnt(binary_number(n))
    answer = n + 1
    ck = cnt(binary_number(answer))
    while(value != ck):
        answer += 1
        ck = cnt(binary_number(answer))
    print(answer)
    return answer

# 2진법으로 변환하는 함수 (기존 bin이라는 함수가 있음)
def binary_number(num):
    trans_num = ''
    while(num // 2 != 0):
        trans_num += str(num % 2)
        num = num // 2
        if num // 2 == 0:
            trans_num += str(num % 2)
    trans_num = trans_num[::-1]
    return trans_num

# 1의 갯수를 세는 함수 (기존 count라는 함수가 있음)
def cnt(trans_num):
    res = 0
    for i in range(len(trans_num)):
        if trans_num[i] == '1':
            res += 1
    return res

# 기존 함수 사용한 코드
def simple(n):
    num = bin(n).count('1')
    while True:
        n += 1
        if num == bin(n).count('1'):
            break
    return n