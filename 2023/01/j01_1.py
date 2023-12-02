import re

def main():
    sum = 0
    with open("input.txt") as file:
        for line in file.read().split("\n")[:-1]:
            line = re.sub("\D", "", line)
            sum += int(line[0]) * 10 + int(line[-1])
    print(sum)

if __name__ == "__main__":
    main()