# 1~9까지 가능한 모든 임의의 숫자와 테스트 답안을 비교하여, 가능한 모든 답을 찾는다.

import itertools

# 임의의 숫자와 테스트 숫자를 비교
def check(expected, baseball):
    strike_count = 0
    ball_count = 0
    
    for i in range(3):
        if expected[i] in baseball[0]:
            if baseball[0].find(expected[i]) == i:
                strike_count += 1
            else:
                ball_count += 1
        else:
            continue
        
    if baseball[1] == strike_count and baseball[2] == ball_count:
        return True
    else:
        return False

def solution(baseball):
    ans = []
    arr = list(map(''.join,itertools.permutations(['1','2','3','4','5','6','7','8','9'], 3))) # 가능한 모든 임의의 숫자 배열
    
    # 테스트 숫자를 str로 바꿔주기
    for i in range(len(baseball)):
        baseball[i][0] = str(baseball[i][0])
    
    for i in range(len(arr)):
        count = 0
        for case in baseball:
            if check(arr[i], case):
                count += 1
                continue
            else:
                break
        # 임의의 숫자가 모든 테스트를 통과한다면 answer에 추가
        if len(baseball) == count:
            ans.append(arr[i])
    return len(ans)