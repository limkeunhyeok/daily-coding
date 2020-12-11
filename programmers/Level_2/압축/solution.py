from string import ascii_uppercase

def solution(msg):
    answer = []
    d = {}
    for i in range(len(ascii_uppercase)):
        d[ascii_uppercase[i]] = i + 1

    l = 26
    w = 0
    c = 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(d[msg[w:c]])
            break
        if msg[w:c + 1] not in d:
            l += 1
            d[msg[w:c + 1]] = l
            answer.append(d[msg[w:c]])
            w = c
    return answer