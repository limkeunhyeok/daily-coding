def solution(n, s):
    if n > s:
        return [-1]
    small = s // n
    largeValue = s - (small * n)
    return [small] * (n - largeValue) + [small + 1] * largeValue