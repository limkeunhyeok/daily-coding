import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    for i in range(len(scoville)):
        try:
            first = heapq.heappop(heap)
            if first < K:
                second = heapq.heappop(heap)
                new = first + (second * 2)
                heapq.heappush(heap, new)
                answer += 1
        except IndexError:
            return -1
    return answer

'''
내풀이 시간초과
def solution(scoville, K):
    answer = 0
    temp = sorted(scoville)
    for i in range(len(temp)):
        try:
            first = temp.pop(0)
            if first < K:
                second = temp.pop(0)
                new = first + (second * 2)
                temp.append(new)
                temp = sorted(temp)
                answer += 1
        except IndexError:
            return -1
    return answer
'''