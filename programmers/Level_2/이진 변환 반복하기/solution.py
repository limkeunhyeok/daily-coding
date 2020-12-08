def solution(s):
    removed = 0
    converted = 0
    while s != '1':
        removed += s.count('0')
        s = ''.join(s.split('0'))
        s = bin(len(s))[2:]
        converted += 1
    return [converted, removed]