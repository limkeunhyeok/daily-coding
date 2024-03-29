def rank(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    maximum, minimum = 0, 0
    index = 0

    for i in range(6):
        if lottos[i] == 0:
            maximum += 1
        elif lottos[i] in win_nums:
            maximum += 1
            minimum += 1
    return [rank(maximum), rank(minimum)]