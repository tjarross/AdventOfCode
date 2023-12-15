def hash(pattern):
    h = 0 
    for c in pattern:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def main():
    with open("input.txt") as file:
        line = file.read().split("\n")[0]

    sum = 0
    for pattern in line.split(","):
         sum += hash(pattern)
    print(sum)


if __name__ == "__main__":
    main()