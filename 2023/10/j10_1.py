INITIAL_X = 0
INITIAL_Y = 0


def main():
    global INITIAL_X, INITIAL_Y
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
    lines.insert(0, "*" * len(lines[0]))
    lines.insert(len(lines), lines[0])
    for i, line in enumerate(lines):
        lines[i] = f"*{lines[i]}*"
        # print(lines[i])
    for i, line in enumerate(lines):
        if "S" in line:
            INITIAL_X, INITIAL_Y = [line.index("S"), i]
            break

    loop_coords = [INITIAL_X, INITIAL_Y, INITIAL_X + 1, INITIAL_Y]
    last_move = [INITIAL_X, INITIAL_Y]
    x, y = INITIAL_X + 1, INITIAL_Y
    steps = 1
    while True:
        if lines[y][x] == "7":
            if last_move == [x - 1, y]:
                y += 1
                last_move = [x, y - 1]
            else:
                x -= 1
                last_move = [x + 1, y]
        elif lines[y][x] == "F":
            if last_move == [x + 1, y]:
                y += 1
                last_move = [x, y - 1]
            else:
                x += 1
                last_move = [x - 1, y]
        elif lines[y][x] == "J":
            if last_move == [x - 1, y]:
                y -= 1
                last_move = [x, y + 1]
            else:
                x -= 1
                last_move = [x + 1, y]
        elif lines[y][x] == "L":
            if last_move == [x + 1, y]:
                y -= 1
                last_move = [x, y + 1]
            else:
                x += 1
                last_move = [x - 1, y]
        elif lines[y][x] == "-":
            while lines[y][x] == "-":
                if last_move == [x - 1, y]:
                    x += 1 
                    last_move = [x - 1, y]
                else:
                    x -= 1 
                    last_move = [x + 1, y]
                loop_coords.append([x, y])
                steps += 1
            continue
        elif lines[y][x] == "|":
            while lines[y][x] == "|":
                if last_move == [x, y - 1]:
                    y += 1
                    last_move = [x, y - 1]
                else:
                    y -= 1
                    last_move = [x, y + 1]
                    loop_coords.append([x, y])
                steps += 1
            continue
        elif lines[y][x] == "S":
            break

        loop_coords.append([x, y])
        steps += 1
        if [x, y] == [INITIAL_X, INITIAL_Y]:
            break
    print(steps // 2)


if __name__ == "__main__":
    main()