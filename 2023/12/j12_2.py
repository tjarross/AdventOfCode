saved = {}


def count_groups(springs: str):
    return [len(word) for word in springs.split(".") if len(word) != 0]


def try_pattern(pattern: str, springs: str):
    if len(pattern) > len(springs):
        return False
    if len(pattern) == len(springs):
        if springs.count('.') != 0:
            return False
        return True
    if '.' in springs[:len(pattern)] or springs[len(pattern)] == '#':
        return False
    return True


def guess(springs: str, damaged_groups: list):
    repr_damaged_groups = repr(damaged_groups)
    if springs + repr_damaged_groups in list(saved):
        return saved[springs + repr_damaged_groups]

    if len(springs) == 0 and len(damaged_groups) != 0:
        saved[springs + repr_damaged_groups] = 0
        return 0
    if len(damaged_groups) == 0:
        if '#' not in springs:
            saved[springs + repr_damaged_groups] = 1
            return 1
        saved[springs + repr_damaged_groups] = 0
        return 0

    res = 0
    if try_pattern(f"{'#' * damaged_groups[0]}", springs) == True:
        res += guess(springs[damaged_groups[0] + 1:], damaged_groups[1:])

    if springs[0] == '#':
        saved[springs + repr_damaged_groups] = res
        return res
    saved[springs + repr_damaged_groups] = res + guess(springs[1:], damaged_groups)
    return saved[springs + repr_damaged_groups]


def get_new_springs(springs: str, damaged_groups: str):
    return f"{springs}?{springs}?{springs}?{springs}?{springs}", f"{damaged_groups},{damaged_groups},{damaged_groups},{damaged_groups},{damaged_groups}"


def main():
    with open("input.txt") as file:
        lines = file.read().split('\n')[:-1]

    sum = 0
    for i, line in enumerate(lines):
        springs, damaged_groups = get_new_springs(*line.split())
        sum += guess(springs, list(map(int, damaged_groups.split(","))))
    print(sum)


if __name__ == "__main__":
    main()