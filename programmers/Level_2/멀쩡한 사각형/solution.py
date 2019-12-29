def solution(w,h):
    answer = 1
    d = gcd(w,h)
    unit = (w // d) + (h // d) - 1
    return w * h - unit * d

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a