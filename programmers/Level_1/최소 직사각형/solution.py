def getMaxLength(sizes):
    w, h = 0, 0
    for size in sizes:
        size.sort()
        if size[0] > w: w = size[0]
        if size[1] > h: h = size[1]
    return w, h

def solution(sizes):
    w, h = getMaxLength(sizes)
    answer = w * h
    return answer