people = []

for T in range(int(input())):
    w, h = map(int, input().split(' '))
    people.append((w, h))

for i in people:
    cnt = 1
    for j in people:
        if i[0] != j[0] and i[1] != j[0]:
            if i[0] < j[0] and i[1] < j[1]:
                cnt += 1
    print(cnt, end = ' ')