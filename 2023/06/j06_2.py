import re


def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        time = "".join(re.match(r"Time:\s+((\d+\s*)+)", lines[0]).group(1).split())
        distance = "".join(re.match(r"Distance:\s+((\d+\s*)+)", lines[1]).group(1).split())

        win = 0
        for t in range(int(time)):
            if t * (int(time) - t) > int(distance):
                win += 1
        print(win)


if __name__ == "__main__":
    main()