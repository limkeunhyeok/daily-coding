def solution(person):
    answer = []
    person.sort()
    cnt = 0
    
    for p in person:
        cnt += p
        answer.append(cnt)
        
    return sum(answer)

n = int(input())
person = list(map(int, input().split()))
print(solution(person))