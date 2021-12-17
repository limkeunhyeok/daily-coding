if __name__ == "__main__":
    N = input()
    F = int(input())
    div = int(N[:-2] + "00")
    
    while True:
        if div % F == 0:
            break
        div += 1
    
    answer = str(div)[-2:]
    print(answer)
