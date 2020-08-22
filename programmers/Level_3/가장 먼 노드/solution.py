from collections import defaultdict, deque

def bfs(graph):
    q = deque()
    q.append((1, 0))
    visited = set()
    dist = defaultdict(lambda: 0)
    
    while q:
        node, cnt = q.popleft()
        visited.add(node)
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                dist[cnt + 1] += 1
                q.append((n, cnt + 1))
    return dist[cnt]

def solution(n, edge):
    answer = 0
    g = defaultdict(set)
    
    for node1, node2 in edge:
        g[node1].add(node2)
        g[node2].add(node1)
    
    answer = bfs(g)
    return answer