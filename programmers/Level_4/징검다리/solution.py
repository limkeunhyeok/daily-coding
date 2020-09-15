def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left = 0
    right = distance
    
    while left <= right:
        prev = 0
        temp = 987654321
        removed = 0
        mid = (left + right) // 2
        
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                removed += 1
            else:
                temp = min(temp, rocks[i] - prev)
                prev = rocks[i]
        
        if removed > n:
            right = mid - 1
        else:
            answer = temp
            left = mid + 1
    return answer