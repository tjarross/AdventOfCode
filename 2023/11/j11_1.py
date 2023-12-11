def expand_empty_columns(lines):
    new_lines = [""] * len(lines)
    for x in range(len(lines[0])):
        column = [lines[y][x] for y in range(len(lines))]
        if column.count("#") == 0:
            for y in range(len(lines)):
                new_lines[y] += column[y]
        for y in range(len(lines)):
            new_lines[y] += column[y]
    return new_lines


def expand_empty_lines(lines):
    new_lines = []
    for i in range(len(lines)):
        if lines[i].count("#") == 0:
            new_lines.append(lines[i])
        new_lines.append(lines[i])
    return new_lines


def get_galaxies_coords(lines):
    return [[x, y] for x in range(len(lines[0])) for y in range(len(lines)) if lines[y][x] == "#"]


def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
    lines = expand_empty_lines(lines)
    lines = expand_empty_columns(lines)
    galaxies_coords = get_galaxies_coords(lines)

    count = 0
    for i, coord1 in enumerate(galaxies_coords):
        for coord2 in galaxies_coords[i + 1:]:
            count += sum([abs(a - b) for a, b in zip(coord1, coord2)])
    print(count)


if __name__ == "__main__":
    main()