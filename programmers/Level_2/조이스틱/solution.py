def solution(name):
    answer = 0
    name = list(name)
    base = ["A"] * len(name)
    index = 0

    while(True):
        rightIndex = 1
        leftIndex = 1
        # 문자 변경
        if name[index] != "A":
            answer += min(ord(name[index])-ord("A"), 26-(ord(name[index])-ord("A")))
            name[index] = "A"
        
        if name == base:
            break
        
        # 좌우 커서 이동 결정
        else:
            for i in range(1, len(name)):
                if name[index + i] == "A":
                    rightIndex += 1
                else:
                    break
                if name[index-i] == "A":
                    leftIndex += 1
                else:
                    break
            
            if rightIndex > leftIndex:
                answer += leftIndex
                index -= leftIndex
            else:
                answer += rightIndex
                index += rightIndex
    return answer
