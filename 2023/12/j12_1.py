import re


def count_groups(springs):
    last_char = springs[0]
    count = [1] if springs[0] == "#" else []
    for c in springs[1:]:
        if last_char in [".", "?"] and c == "#":
            last_char = "#"
            count.append(1)
        elif last_char == "#" and c == "#":
            count[-1] += 1
        if c in [".", "?"]:
            last_char = "."
    return count


def guess(springs: str, damaged_groups: str):
    if damaged_groups == count_groups(springs):
        return 1
    for i in range(len(springs)):
        if springs[i] == "?":
            return guess(f"{springs[:i]}.{springs[i + 1:]}", damaged_groups) + guess(f"{springs[:i]}#{springs[i + 1:]}", damaged_groups)
    return 0


def main():
    with open("input.txt") as file:
        lines = file.readlines()
    arrangements = []
    for line in lines:
        match = re.match(r"([?.#]+)\s([0-9,]+)", line).groups()
        arrangements.append(guess(match[0], list(map(int, match[1].split(",")))))
    print(sum(arrangements))


if __name__ == "__main__":
    main()