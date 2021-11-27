if __name__ == "__main__":
    A, B = map(int, input().split(" "))
    array = []
    for i in range(B):
        array += [i + 1] * (i + 1)
        if len(array) >= B:
            break
    print(sum(array[A - 1:B]))