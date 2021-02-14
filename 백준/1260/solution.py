from collections import deque

def dfs(g, v):
    visited = []
    s = [v]
    
    while s:
        node = s.pop()
        if node not in visited:
            visited.append(node)
            s.extend(sorted(g[node], reverse = True))
    return visited

def bfs(g, v):
    visited = []
    q = deque([v])
    
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(sorted(g[node]))
    return visited



n, m, v = map(int, input().split(' '))
g = [set([]) for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split(' '))
    g[v1].add(v2)
    g[v2].add(v1)

print(*dfs(g, v))
print(*bfs(g, v))