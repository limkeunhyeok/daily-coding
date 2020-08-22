def check(string):
    for c in string:
        if not c.isalpha():
            return False
    return True

def strThrow(string):
    res = []
    for i in range(0, len(string) - 1):
        if check(string[i : i + 2]):
            res.append(string[i : i + 2].lower())
    return res
        

def solution(str1, str2):
    answer = 0
    str1 = strThrow(str1)
    str2 = strThrow(str2)
    
    if len(str1) == len(str2) == 0:
        return 65536
    
    intersection = set(str1) & set(str2)
    union = set(str1) | set(str2)
    
    molecule = 0
    denominator = 0
    
    for word in intersection:
        molecule += min(str1.count(word), str2.count(word))
    
    for word in union:
        denominator += max(str1.count(word), str2.count(word))

    answer = (molecule / denominator) * 65536
    return int(answer)