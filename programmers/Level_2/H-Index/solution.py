def solution(c):
    for i,x in enumerate(sorted(c)):
        if x >= len(c) - i:
            return len(c) - i
    return 0