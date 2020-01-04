def solution(s):
    answer = 1001
    if len(s)==1:
        return 1
    
    for size in range(1,int(len(s)/2)+1):
        count=0
        word = ""
        for i in range(0,len(s)+1,size):
            if word[-size:] == s[i:i+size]:
                count += 1
            else:
                if count > 1:
                    word += str(count) + s[i:i+size]
                else:
                    word += s[i:i+size]
                count=1
        if answer > len(word):
            answer = len(word)
    return answer