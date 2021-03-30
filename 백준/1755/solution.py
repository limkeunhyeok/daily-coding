def solution(n, m):
    numberWord = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    arr = []
    for i in range(n, m + 1):
        temp = ''
        for j in str(i):
            temp += numberWord[int(j)] + ' '
        arr.append(temp[:-1])
        
    arr.sort()
    answer = []
    
    for i in arr:
        temp = ''
        for j in i.split(' '):
            temp += str(numberWord.index(j))
        answer.append(int(temp))
    return answer

n, m = map(int, input().split())
answer = solution(n, m)

for i in range(len(answer)):
    if (i + 1) % 10 == 0:
        print(answer[i])
    else:
        print(answer[i], end = ' ')