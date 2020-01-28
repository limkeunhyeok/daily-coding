def solution(number, k):
    m = 0
    length = len(number)
    for count in range(k):
        for index in range(m, length - 1):
            if number[index] < number[index + 1]:
                number = number[:index] + number[index + 1:]
                length -= 1
                if index > 0:
                    m = index - 1
                break
        else:
            print(number)
            number = number[:length - k + count]
            break
    return "".join([str(i) for i in number])