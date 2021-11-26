if __name__ == "__main__":
    N, kim, lim = map(int, input().split(" "))
    gameRound = 0
    while kim != lim:
        kim -= kim // 2
        lim -= lim // 2
        gameRound += 1
    print(gameRound)