def solution(people,limit):
    people.sort()
    start = 0
    end = len(people)-1
    count = 0
    
    while(start < end):
        if people[start] + people[end] <= limit:
            count += 1
            start += 1
            end -= 1
        else:
            end -= 1
    return len(people) - count