from itertools import combinations #조합 함수

def solution(n, s):
    answer = 100
    peoples = [i for i in range(n)]
    teams = []
    
    for team in list(combinations(peoples, n // 2)):
        teams.append(team)
        
    for i in range(len(teams) // 2):
        team = teams[i]
        start = 0
        for j in range(n // 2):
            p = team[j]
            for k in team:
                start += s[p][k]
        
        team = teams[-i - 1]
        link = 0
        for j in range(n // 2):
            p = team[j]
            for k in team:
                link += s[p][k]
        
        answer = min(answer, abs(start - link))
    return answer

n = int(input())
s = []
for _ in range(n):
    temp = list(map(int, input().split(' ')))
    s.append(temp)
print(solution(n, s))