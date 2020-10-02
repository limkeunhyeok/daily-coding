"""
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    while n != 0:
        maxIndex = works.index(max(works))
        works[maxIndex] -= 1
        n -= 1
    
    for i in works:
        answer += i ** 2
    return answer
"""

import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [num * (-1) for num in works]
    
    heapq.heapify(works)
    for i in range(n):
        work = heapq.heappop(works)
        work += 1
        heapq.heappush(works, work)
    
    answer = 0
    while len(works) > 0:
        work = heapq.heappop(works)
        answer += work ** 2
    return answer