# 다른 사람 풀이 참고함
def solution(food_times, k):
    # 같은 사이즈의 음식끼리 묶기
    length = len(food_times)
    cnt = 0
    food_size = {}
    for index, time in enumerate(food_times):
        if time in food_size:
            food_size[time].append(index)
        else:
            food_size[time] = [index]
            
    # 오름차순으로 나타내어 k에서 n바퀴씩 빼기
    for time in sorted(food_size):
        if k - (length*(time-cnt)) >= 0:
            k -= length*(time-cnt)
            length -= len(food_size[time])
            cnt += time - cnt
            
        # k를 남은 음식의 갯수로 나눈 나머지만큼 이동하여 결과를 반환
        else:
            k %= length 
            
            # n바퀴씩 돌고난 후, 첫번째 인덱스
            for find in food_size:
                if find >= time:
                    index = food_size[find][0]
                    break
            
            # 남은 음식들만 순환
            for i in range(index, len(food_times)):
                if food_times[i] >= time:
                    if k == 0:
                        return i+1
                    k -= 1
    return -1 # 더 섭취할 음식이 없을 경우