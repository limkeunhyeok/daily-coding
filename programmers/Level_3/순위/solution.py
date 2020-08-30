def solution(n, results):
    answer = 0
    wins_dict = {}
    loses_dict = {}
    
    for i in range(n):
        wins_dict[i + 1] = set()
        loses_dict[i + 1] = set()
    
    for player in range(1, n + 1):
        for res in results:
            if res[0] == player:
                wins_dict[player].add(res[1])
            if res[1] == player:
                loses_dict[player].add(res[0])
        for w in loses_dict[player]:
            wins_dict[w].update(wins_dict[player])
        for l in wins_dict[player]:
            loses_dict[l].update(loses_dict[player])
            
    for player in range(1, n + 1):
        if len(wins_dict[player]) + len(loses_dict[player]) == n - 1:
            answer += 1
    return answer