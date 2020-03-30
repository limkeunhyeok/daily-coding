# 문자열 배열(string array)이 주어지면, 제일 긴 공통된 접두사(prefix)의 길이를 찾으시오.

def solution(words):
    sorted(words)
    words = words[::-1]
    prefix = ''
    for i in range(len(words[0])):
        prefix += words[0][i]
        for j in range(1, len(words)):
            if words[j].startswith(prefix):
                continue
            else:
                prefix = prefix[:-1]
    return len(prefix)