def solution(dirs):
    d = {
            'U': [0, 1],
            'D': [0, -1],
            'R': [1, 0],
            'L': [-1, 0]
        }
    
    p = [0, 0]
    visited = []
    for c in dirs:
        if p[0] + d[c][0] > 5 or p[0] + d[c][0] < -5 or p[1] + d[c][1] > 5 or p[1] + d[c][1] < -5:
            continue
        else: 
            if p + [c] not in visited:
                visited.append(p + [c])
            p[0] += d[c][0]
            p[1] += d[c][1]
            
            if p[0] > 5:
                p[0] = 5
            elif p[0] < -5:
                p[0] = -5
                
            if p[1] > 5:
                p[1] = 5
            elif p[1] < -5:
                p[1] = -5
            
            if c == 'U':
                if p + ['D'] not in visited:
                    visited.append(p + ['D'])
                    
            if c == 'D':
                if p + ['U'] not in visited:
                    visited.append(p + ['U'])
            
            if c == 'L':
                if p + ['R'] not in visited:
                    visited.append(p + ['R'])
                    
            if c == 'R':
                if p + ['L'] not in visited:
                    visited.append(p + ['L'])
    return len(visited) // 2