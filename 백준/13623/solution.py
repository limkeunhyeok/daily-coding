if __name__ == "__main__":
    A, B, C = map(int, input().split(" "))
    arr = [A, B, C]
    total = sum(arr)
    person = ["A", "B", "C"]
    
    if total == 0:
        print("*")
    elif total == 3:
        print("*")
    elif total == 1:
        index = arr.index(1)
        print(person[index])
    elif total == 2:
        index = arr.index(0)
        print(person[index])
