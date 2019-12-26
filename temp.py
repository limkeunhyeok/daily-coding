def solution(numbers):
    temp = list(map(str, numbers))
    temp.sort(key=lambda x:3*x, reverse = True)
    return str(int(''.join(temp)))