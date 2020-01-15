def solution(n, words):
    temp = []
    peoples = [0] * n
    for i in range(len(words)):
        if (words[i] in temp) or (i and words[i][0] != words[i - 1][-1]):
            return [i % n + 1, peoples[i % n] + 1]
        temp.append(words[i])
        peoples[i % n] += 1
    return [0, 0]

'''
다른 사람 풀이
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]:
            return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
'''