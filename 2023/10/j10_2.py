def replace_s(lines, s_coord, first_loop_coord, last_loop_coord):
    relative_first = [a - b for a, b in zip(first_loop_coord, s_coord)]
    relative_last = [a - b for a, b in zip(last_loop_coord, s_coord)]
    s = None
    if relative_first == [0, 1]:
        if relative_last == [-1, 0]:
            s = "7"
        elif relative_last == [0, -1]:
            s = "|"
        elif relative_last == [1, 0]:
            s = "F"
    elif relative_first == [-1, 0]:
        if relative_last == [0, 1]:
            s = "7"
        elif relative_last == [1, 0]:
            s = "-"
        elif relative_last == [-1, 0]:
            s = "J"
    elif relative_first == [0, -1]:
        if relative_last == [1, 0]:
            s = "L"
        elif relative_last == [0, 1]:
            s = "|"
        elif relative_last == [-1, 0]:
            s = "J"
    elif relative_first == [1, 0]:
        if relative_last == [0, 1]:
            s = "F"
        elif relative_last == [-1, 0]:
            s = "-"
        elif relative_last == [0, -1]:
            s = "L"

    for i in range(len(lines)):
        if "S" in lines[i]:
            lines[i] = lines[i].replace("S", s)
    return lines


def get_all_coords(lines):
    all_coords = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            all_coords.append([x, y])
    return all_coords


def get_loop_coords(lines):
    initial_x, initial_y = 0, 0
    for i, line in enumerate(lines):
        if "S" in line:
            initial_x, initial_y = [line.index("S"), i]
            break
    
    loop_coords = [[initial_x, initial_y], [initial_x + 1, initial_y]]
    last_move = [initial_x, initial_y]
    x, y = initial_x + 1, initial_y
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
        if [x, y] == [initial_x, initial_y]:
            break
    return loop_coords


def get_points_inside_loop(lines, coords, loop_coords):
    line_length = len(lines[0])
    points = 0
    for coord in coords:
        i = 0
        intersections = 0
        while coord[0] + i < line_length:
            if lines[coord[1]][coord[0] + i] in ["J", "L", "|"] and [coord[0] + i, coord[1]] in loop_coords:
                intersections += 1
            i += 1
        if intersections % 2 != 0:
            points += 1
    return points


def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
    lines.insert(0, "*" * len(lines[0]))
    lines.insert(len(lines), lines[0])
    for i in range(len(lines)):
        lines[i] = f"*{lines[i]}*"
    loop_coords = get_loop_coords(lines)
    all_coords = get_all_coords(lines)
    lines = replace_s(lines, loop_coords[0], loop_coords[1], loop_coords[-2])
    non_loop_coords = [coord for coord in all_coords if coord not in loop_coords]
    print(get_points_inside_loop(lines, non_loop_coords, loop_coords))


if __name__ == "__main__":
    main()