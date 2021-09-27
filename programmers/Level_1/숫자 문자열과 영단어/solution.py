"""
내 풀이
def solution(s):
    word = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    answer = ""
    
    temp = ""
    for c in s:
        if c.isdigit():
            answer += c
        else:
            temp += c
            if temp in word:
                answer += word[temp]
                temp = ""
    return int(answer)
"""

def solution(s):
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    answer = s
    for key, value in num_dict.items():
        answer = answer.replace(key, value)
    return int(answer)