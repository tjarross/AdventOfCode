def main():
    with open("input.txt") as file:
        line = file.readlines()[0]
    count = 0
    for i, c in enumerate(line):
        if c == "(":
            count += 1
        if c == ")":
            count -= 1
        if count == -1:
            print(i + 1)
            break


if __name__ == "__main__":
    main()