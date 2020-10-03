# "Look and say" sequence (보고 말하는 수열)은 다음과 같습니다.

# 1 - 1개의 1
# 11 - 2개의 1
# 21 - 1개의 2, 1개의 1
# 1211 - 1개의 1, 1개의 2, 2개의 1
# 111221 - ...

# 위와 같이 수열의 N 번째 수는 N-1번째 수의 조합을 풀어놓은 수 입니다.
# 정수 N이 주어졌을때, "Look and say" 수열의 N번째 수까지 프린트 하시오.

def solution(n):
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    
    answer = '11'
    for _ in range(3, n + 1):
        answer += '$'
        l = len(answer)
        cnt = 1
        temp = ''
        for j in range(1, l):
            if answer[j] != answer[j - 1]:
                temp += str(cnt)
                temp += answer[j - 1]
                cnt = 1
            else:
                cnt += 1
        answer = temp    
    return answer