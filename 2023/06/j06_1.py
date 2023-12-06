import re
from functools import reduce


def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        times = re.match(r"Time:\s+((\d+\s*)+)", lines[0]).group(1).split()
        distances = re.match(r"Distance:\s+((\d+\s*)+)", lines[1]).group(1).split()

        races_win = []
        for distance, time in zip(distances, times):
            win = 0
            for t in range(int(time)):
                if t * (int(time) - t) > int(distance):
                    win += 1
            races_win.append(win)
        print(reduce(lambda x, y: x * y, races_win))


if __name__ == "__main__":
    main()