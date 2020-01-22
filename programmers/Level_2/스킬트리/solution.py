def solution(skill, skill_trees):
    answer = 0
    for word in skill_trees:
        if skillTree(word, skill):
            answer += 1
    return answer

def skillTree(word, skill):
    temp = ''
    for c in word:
        if c in skill:
            temp += c

    if not temp or (skill[0] == temp[0] and temp in skill):
        return True
    return False