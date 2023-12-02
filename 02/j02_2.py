import re


def main():
    sum = 0
    with open("input.txt") as file:
        for line in file.read().split("\n")[:-1]:
            max_red = 0
            max_green = 0
            max_blue = 0
            game_sets = line.split(":")[1].split(";")
            for game_set in game_sets:
                for pick in game_set.split(","):
                    match = re.match(r" (\d+) (red|green|blue)", pick)
                    number = int(match.group(1))
                    color = match.group(2)
                    if color == "red" and number > max_red:
                        max_red = number
                    if color == "green" and number > max_green:
                        max_green = number
                    if color == "blue" and number > max_blue:
                        max_blue = number
            sum += max_red * max_green * max_blue
    print(sum)


if __name__ == "__main__":
    main()