from collections import defaultdict
from itertools import combinations

def solution(infos, queries):
    answer = []
    cases = defaultdict(list)
    
    for info in infos:
        info = info.split(' ')
        keyList = info[:-1]
        score = int(info[-1])
        
        for i in range(5):
            for c in combinations(keyList, i):
                key = ''.join(c)
                cases[key].append(score)

    for key in cases.keys():
        cases[key].sort()
     
    for query in queries:
        q = []
        query = query.split(' ')
        
        for word in query:
            if word != 'and' and word != '-':
                q.append(word)
        
        key = ''.join(q[:-1])
        score = int(q[-1])
        count=0
        
        if key in cases.keys():
            value = cases[key]
            start,end = 0, len(value)
            
            while start <= end and start < len(value):
                mid = (start + end) // 2
                
                if value[mid] < score:
                    start = mid + 1
                else:
                    end = mid - 1
            
            count = len(value) - start
        
        answer.append(count)
    return answer