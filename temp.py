def solution(N, stages):
    user = len(stages) # 총 도전자 수
    fail = [] # 실패율
    answer = []
    
    # 실패율 체크
    for i in range(N):
        user_stage = 0 # 클리어하지 못한 도전자 수
        for j in range(len(stages)):
            if stages[j] == i + 1:
                user_stage += 1
        if user == 0:
            fail.append(0)
            continue
        fail.append(user_stage / user)
        user -= user_stage

    # 스테이지와 실패율 매핑
    dict = {}
    for i in range(len(fail)):
        dict[i+1] = fail[i]
    
   # 스테이지 내림차순
    while N != len(answer):
        temp = 0
        keys = list(dict.keys())
        for i in keys:
            if dict[i] > temp:
               temp = dict[i]
        for i in keys:
            if dict[i] == temp:
                answer.append(i)
                del dict[i]
                break
    return answer