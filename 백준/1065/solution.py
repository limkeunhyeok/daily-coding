def solution(num):
    if num <= 99:
        return num
    answer = 99
    for n in range(100, num + 1):
        temp = list(map(int, str(n)))
        if temp[0] - temp[1] == temp[1] - temp[2]:
            answer += 1
    return answer

N = int(input())
print(solution(N))