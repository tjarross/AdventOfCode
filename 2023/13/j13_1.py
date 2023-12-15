List = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]


def sublist(lst1, lst2):
   ls1 = [element for element in lst1 if element in lst2]
   ls2 = [element for element in lst2 if element in lst1]
   return ls1 == ls2


def get_symmetry_index(pattern):
    for i, (line1, line2) in enumerate(zip(pattern[:-1], pattern[1:])):
        if line1 == line2:
            symmetry = i + 1
            if sublist(pattern[symmetry - 1::-1], pattern[symmetry:]) \
            or sublist(pattern[symmetry:], pattern[symmetry - 1::-1]):
                return symmetry
    return 0


def get_pattern_value(pattern1, pattern2):
    horizontal_simmetry = get_symmetry_index(pattern2)
    vertical_simmetry = 0
    # print(horizontal_simmetry)
    last_column = [pattern1[0][x] for x in range(len(pattern1[0]))]
    # print(last_column)
    for x in range(len(pattern1[0][1:])):
        column = [pattern1[y][x] for y in range(len(pattern1))]
        if column == last_column:
            vertical_simmetry = x
            break
        last_column = column
        # print("".join(column))
    # print(vertical_simmetry)
    return horizontal_simmetry * 100 + vertical_simmetry


def main():
    with open("input.txt") as file:
        lines = List#file.read().split("\n")[:-1]

    patterns = [[]]
    for line in lines:
        if line == "":
            patterns.append([])
        else:
            patterns[-1].append(line)

    print(sum([get_pattern_value(pattern1, pattern2) for pattern1, pattern2 in zip(patterns[:-1], patterns[1:])]))

if __name__ == "__main__":
    main()