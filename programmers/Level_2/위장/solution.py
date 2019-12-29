def solution(clothes):
    answer = 1
    dict = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in dict:
            dict[clothes[i][1]] = [clothes[i][0]]
        else:
            dict[clothes[i][1]].append(clothes[i][0])
    for key in dict.keys():
        answer *= (len(dict[key]) + 1)
    return answer - 1