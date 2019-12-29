def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = array.copy()
        b = a[(commands[i][0] - 1):commands[i][1]]
        b.sort()
        answer.append(b[commands[i][2] - 1])
    return answer