import re


def get_number_from_index(line: list, x: int) -> int:
    start_index = x - re.search(r"[^0-9]", line[:x][::-1]).start()
    return int(re.match(r"(\d+)", line[start_index:]).group(1))


def main():
    sum = 0
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        lines.insert(0, "." * len(lines[0]))
        lines.insert(len(lines), "." * len(lines[0]))

        for i in range(len(lines)):
            lines[i] = f".{lines[i]}."

        for i in range(len(lines)):
            for j, c in enumerate(lines[i]):
                if c == "*":
                    nb_numbers = 0
                    numbers = []

                    if lines[i][j - 1].isdigit():
                        numbers.append(get_number_from_index(lines[i], j - 1))
                        nb_numbers += 1
                    if lines[i][j + 1].isdigit():
                        numbers.append(get_number_from_index(lines[i], j + 1))
                        nb_numbers += 1

                    if None != re.match(r"\d\.\d", lines[i - 1][j - 1:j + 2]):
                        numbers.append(get_number_from_index(lines[i - 1], j - 1))
                        numbers.append(get_number_from_index(lines[i - 1], j + 1))
                        nb_numbers += 2
                    else:
                        match = re.search(r"\d", lines[i - 1][j - 1:j + 2])
                        if match is not None:
                            numbers.append(get_number_from_index(lines[i - 1], j - 1 + match.start()))
                            nb_numbers += 1

                    if None != re.match(r"\d\.\d", lines[i + 1][j - 1:j + 2]):
                        numbers.append(get_number_from_index(lines[i + 1], j - 1))
                        numbers.append(get_number_from_index(lines[i + 1], j + 1))
                        nb_numbers += 2
                    else:
                        match = re.search(r"\d", lines[i + 1][j - 1:j + 2])
                        if match is not None:
                            numbers.append(get_number_from_index(lines[i + 1], j - 1 + match.start()))
                            nb_numbers += 1

                    if nb_numbers == 2:
                        sum += numbers[0] * numbers[1]
                
    print(sum)


if __name__ == "__main__":
    main()