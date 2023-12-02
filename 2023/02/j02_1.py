import re


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def main():
    sum = 0
    with open("input.txt") as file:
        for line in file.read().split("\n")[:-1]:
            game_id = int(re.search(r"^Game (\d+):", line).group(1))
            game_sets = line.split(":")[1].split(";")
            for game_set in game_sets:
                for pick in game_set.split(","):
                    match = re.match(r" (\d+) (red|green|blue)", pick)
                    number = int(match.group(1))
                    color = match.group(2)
                    if color == "red" and number > MAX_RED \
                    or color == "green" and number > MAX_GREEN \
                    or color == "blue" and number > MAX_BLUE:
                        break
                else:
                    continue
                break
            else:
                sum += game_id
    print(sum)


if __name__ == "__main__":
    main()