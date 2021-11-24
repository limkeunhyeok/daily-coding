import itertools

def multiArray(arr):
    answer = 1
    for n in arr:
        answer *= n
    return answer

if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    primeList = list(map(int, input().split(" ")))
    answer = 0
    c = 0
    for i in range(1, N + 1):
        combi = list(itertools.combinations(primeList, i))
        for c in combi:
            multi = multiArray(c)
            if i % 2 == 1:
                answer += int(M / multi)
            else:
                answer -= int(M / multi)
    print(answer)