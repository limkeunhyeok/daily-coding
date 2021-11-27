def play(array):
    result = sum(array)
    if result == 4:
        print("E")
    elif result == 3:
        print("A")
    elif result == 2:
        print("B")
    elif result == 1:
        print("C")
    elif result == 0:
        print("D")

if __name__ == "__main__":
    for _ in range(3):
        array = list(map(int, input().split(" ")))
        play(array)   