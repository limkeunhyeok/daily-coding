if __name__ == "__main__":
    x, y = input().split(" ")
    try:
        print(int(x) - int(y))
    except:
        print("NaN")