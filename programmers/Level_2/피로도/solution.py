import itertools

def getDungeonsPermutations(dungeons):
    return list(map(list, itertools.permutations(dungeons)))

def getCount(k, dungeons):
    count = 0
    acc = k
    for dungeon in dungeons:
        if dungeon[0] <= acc:
            count += 1
            acc -= dungeon[1]
    return count

def getExplore(k, dungeons):
    answer = 0
    maxCount = len(dungeons)
    dungeonsPemutations = getDungeonsPermutations(dungeons)
    for dungeons in dungeonsPemutations:
        count = getCount(k, dungeons)
        if count == maxCount:
            return count
        if answer < count:
            answer = count
    return answer
    

def solution(k, dungeons):
    answer = getExplore(k, dungeons)
    return answer