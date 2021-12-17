if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    number = min(numbers)
    
    while True:
        count = 0
        for i in range(5):
            if number % numbers[i] == 0:
                count += 1
        if count > 2:
            break
        number += 1
    print(number)
