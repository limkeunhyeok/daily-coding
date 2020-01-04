def solution(n, m):
    d = gcd(n, m)
    value = d * (n // d) * (m // d)
    return [d, value]
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a