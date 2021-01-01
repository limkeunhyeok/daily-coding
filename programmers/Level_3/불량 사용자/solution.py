import re
from itertools import product

def solution(user_id, banned_id):
    res = matched(user_id, banned_id)
    answer = check(product(*res), len(banned_id))
    return answer

def matched(user_id, banned_id):
    answer = []
    for banned in banned_id:
        temp = []
        wildcard = '^' + banned.replace('*', '.') + '$'
        for user in user_id:
            if re.search(wildcard, user):
                temp.append(user)
        answer.append(temp)                
    return answer

def check(bannedList, count):
    converted = []
    answer = 0
    for t in bannedList:
        temp = sorted(set(t))
        if len(temp) == count:
            converted.append(temp)
            answer += 1
    answer = set([tuple(set(item)) for item in converted])
    return len(answer)