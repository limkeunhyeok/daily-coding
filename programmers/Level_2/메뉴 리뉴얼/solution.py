from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    d = defaultdict(int)
    
    for order in orders:
        for i in course:
            temp = list(map("".join, combinations(sorted(order), i)))
            for j in temp:
                d[j] += 1
    
    comb = {}
    for key, value in d.items():
        if value != 1:
            comb[key] = value
    
    for c in course:
        temp = dict(filter(lambda x: len(x[0]) == c, comb.items()))
        if temp:
            mv = max(temp.values())
            for key, value in temp.items():
                if value == mv:
                    answer.append(key)
    return sorted(answer)