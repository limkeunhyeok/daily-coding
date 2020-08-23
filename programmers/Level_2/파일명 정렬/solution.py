import re

def solution(files):
    answer = []
    parsed = [re.split("([0-9]+)", file) for file in files]
    temp = sorted(parsed, key = lambda x: (x[0].lower(), int(x[1])))
    for s in temp:
        answer.append("".join(s))
    return answer