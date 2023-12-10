def main():
    with open("input.txt") as file:
        line = file.readlines()[0]
    print(line.count("(") - line.count(")"))


if __name__ == "__main__":
    main()