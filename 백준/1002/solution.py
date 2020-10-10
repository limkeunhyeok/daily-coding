for T in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
        continue
    else:
        l = 0
        l += (x2 - x1) ** 2
        l += (y2 - y1) ** 2
        l = l ** (1 / 2)
        rs = r1 + r2
        rm = abs(r1 - r2)
        if l == rs or l == rm:
            print(1)
        elif l < rs and l > rm:
            print(2)
        else:
            print(0)