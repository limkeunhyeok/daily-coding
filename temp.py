def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings = sorted(strings)
    for i in strings:
        answer.append(i[1:])
    return answer