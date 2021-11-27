from itertools import permutations

if __name__ == "__main__":
    N = int(input())
    array = [str(i + 1) for i in range(N)]
    allPermutations = list(map(list, permutations(array, N)))
    for p in allPermutations:
        print(" ".join(p))
