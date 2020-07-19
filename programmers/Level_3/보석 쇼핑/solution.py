def solution(gems):
    l =  len(set(gems))
    answer = [0, len(gems)]
    start, end = 0, 0
    gemList = {gems[0]: 1}
    
    while start < len(gems) and end < len(gems):
        if len(gemList) == l:
            if answer[1] - answer[0] > end - start:
                answer[0] = start
                answer[1] = end
                
            if gemList[gems[start]] == 1:
                del gemList[gems[start]]
            else:
                gemList[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            else:
                if gemList.get(gems[end]) is None:
                    gemList[gems[end]] = 1
                else:
                    gemList[gems[end]] += 1
    return [answer[0] + 1, answer[1] + 1]