def solution(numbers):
    answer = []

    for n in numbers:
        binary = list(bin(n)[2:])
        binary = ['0'] + binary
        index = ''.join(binary).rfind('0')
        binary[index] = '1'
        
        if n % 2 == 1:
            binary[index + 1] = '0'
        answer.append(int(''.join(binary), 2))
    return answer
