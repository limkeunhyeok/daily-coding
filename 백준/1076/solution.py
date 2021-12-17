def getValue(color):
    if color == "black":
        return "0"
    elif color == "brown":
        return "1"
    elif color == "red":
        return "2"
    elif color == "orange":
        return "3"
    elif color == "yellow":
        return "4"
    elif color == "green":
        return "5"
    elif color == "blue":
        return "6"
    elif color == "violet":
        return "7"
    elif color == "grey":
        return "8"
    elif color == "white":
        return "9"

def getMultiNumber(color):
    if color == "black":
        return 1
    elif color == "brown":
        return 10
    elif color == "red":
        return 100
    elif color == "orange":
        return 1000
    elif color == "yellow":
        return 10000
    elif color == "green":
        return 100000
    elif color == "blue":
        return 1000000
    elif color == "violet":
        return 10000000
    elif color == "grey":
        return 100000000
    elif color == "white":
        return 1000000000
    
    

if __name__ == "__main__":
    colors = []
    for _ in range(3):
        color = input()
        colors.append(color)
    r = int(getValue(colors[0]) + getValue(colors[1]))
    r *= getMultiNumber(colors[2])
    print(r)
