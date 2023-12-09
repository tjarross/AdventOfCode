def extrapolate_list(values):
    subsequences = [values]
    while set(subsequences[-1]) != {0}:
        subsequences.append([v2 - v1 for v1, v2 in zip(subsequences[-1][:-1], subsequences[-1][1:])])
    return sum(int(subsequence[-1]) for subsequence in subsequences)

def main():
    with open("input.txt") as file:
        print(sum(extrapolate_list(list(map(int, line.split()))[::-1]) for line in file.read().split("\n")[:-1]))

if __name__ == "__main__":
    main()