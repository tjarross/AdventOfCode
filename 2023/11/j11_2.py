def get_empty_columns(lines):
    empty_columns = []
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if lines[y][x] == "#":
                break
        else:
            empty_columns.append(x)
    return empty_columns


def get_empty_lines(lines):
    empty_lines = []
    for y in range(len(lines)):
        if lines[y].count("#") == 0:
            empty_lines.append(y)
    return empty_lines


def get_galaxies_coords(lines, empty_lines_coords, empty_columns_coords):
    galaxies_coords = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                galaxy_x = x + 999_999 * len([n for n in empty_columns_coords if n < x])
                galaxy_y = y + 999_999 * len([n for n in empty_lines_coords if n < y])
                galaxies_coords.append([galaxy_x, galaxy_y])
    return galaxies_coords


def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
    empty_lines_coords = get_empty_lines(lines)
    empty_columns_coords = get_empty_columns(lines)
    galaxies_coords = get_galaxies_coords(lines, empty_lines_coords, empty_columns_coords)

    count = 0
    for i, coord1 in enumerate(galaxies_coords):
        for coord2 in galaxies_coords[i + 1:]:
            count += sum([abs(a - b) for a, b in zip(coord1, coord2)])
    print(count)


if __name__ == "__main__":
    main()