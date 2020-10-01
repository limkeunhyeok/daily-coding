def solution(a):
    if len(a) == 1:
        return 1
    if len(a) == 2:
        return 2

    length = len(a)
    left, right = [a[0]], [a[-1]]
    for i in range(len(a)):
        if left[-1] >= a[i]:
            left.append(a[i])
        if right[-1] >= a[length - i - 1]:
            right.append(a[length - i - 1])

    return len(left) + len(right) - 3