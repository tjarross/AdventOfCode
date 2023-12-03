import re


def main():
    sum = 0
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        lines.insert(0, "." * len(lines[0]))
        lines.insert(len(lines), "." * len(lines[0]))
        for i in range(len(lines)):
            lines[i] = f".{lines[i]}."

        for line_cpt, line in enumerate(lines):
            for char_cpt in range(len(line)):
                if line[char_cpt].isdigit():
                    match = re.search(r"^([0-9]+)", line[char_cpt:])
                    number_len = len(match.group(1))

                    if None != re.search(f"[^\.]", lines[line_cpt - 1][char_cpt - 1:char_cpt + number_len + 1]) \
                    or None != re.search(f"[^\.]", lines[line_cpt + 1][char_cpt - 1:char_cpt + number_len + 1]) \
                    or line[char_cpt - 1] != "." or line[char_cpt + number_len] != ".":
                        sum += int(match.group(1))

                    line = line[:char_cpt] + "." * number_len + line[char_cpt + number_len:]
    print(sum)


if __name__ == "__main__":
    main()