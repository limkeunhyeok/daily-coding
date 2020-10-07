for T in range(int(input())):
    k = int(input())
    n = int(input())
    apart = [[i for i in range(n + 1)]]
    for i in range(1, k + 1):
        temp = [0]
        for j in range(2, n + 2):
            temp.append(sum(apart[i - 1][:j]))
        apart.append(temp)
    print(apart[-1][-1])