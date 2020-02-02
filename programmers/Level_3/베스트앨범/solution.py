def solution(genres, plays):
    playDic = {}
    for i in range(len(plays)):
        if genres[i] not in playDic:
            playDic[genres[i]] = {i:plays[i]}
        else:
            playDic[genres[i]][i] = plays[i]
    playDic = sumDic(playDic)
    keyword = sortDic(playDic)
    
    answer = []
    for key in keyword:
        temp = sorted(playDic[key].items(), key=(lambda x:x[1]), reverse=True)
        if len(temp) == 2:
            answer.append(temp[0][0])
        else:
            answer.append(temp[1][0])
            answer.append(temp[2][0])
    return answer

def sumDic(playDic):
    for key in playDic:
        playDic[key]['total'] = sum(playDic[key].values())
    return playDic

def sortDic(playDic):
    temp = {}
    for key in playDic:
        temp[key] = playDic[key]['total']
    temp = sorted(temp.items(), key=(lambda x:x[1]), reverse=True)
    answer = []
    for i in range(len(temp)):
        answer.append(temp[i][0])
    return answer