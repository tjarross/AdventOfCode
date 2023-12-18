List = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1",
    # "?#????#?..#. 1,2,1",
    "????#????.???????????????#????.?????????? 1,4,2,1,7,1,4,2,1,7",
]


def count_groups(springs: str):
    return [len(word) for word in springs.split(".") if len(word) != 0]


def try_pattern(pattern: str, springs: str):
    """
    >>> try_pattern("#", "??")
    True
    >>> try_pattern("#", "???.###")
    True
    >>> try_pattern("#", "?")
    True
    >>> try_pattern("#####", "?#??#.")
    True
    >>> try_pattern("#####", "?#.?#.")
    False
    >>> try_pattern("####", "?#??##..??.")
    False
    >>> try_pattern("####", "?#??.#..??.")
    True
    >>> try_pattern("####", "?#???#..??.")
    True
    >>> try_pattern("####", ".#???#..??.")
    False
    >>> try_pattern("####", "####..??.")
    True
    >>> try_pattern("###", "###?????")
    True
    """
    # print("--->", pattern, springs, end=" ")
    if len(pattern) > len(springs):
        # print("NOK")
        return False
    if len(pattern) == len(springs):
        if springs.count('.') != 0:
            # print("NOK")
            return False
        # print("OK")
        return True
    if '.' in springs[:len(pattern)] or springs[len(pattern)] == '#':
        # print("NOK")
        return False
    # print("OK")
    return True

saved = {}

def guess(springs: str, damaged_groups: list):
    # print(saved)
    if springs + repr(damaged_groups) in list(saved):
        return saved[springs + repr(damaged_groups)]
    # print(springs, damaged_groups)
    if len(springs) == 0 and len(damaged_groups) != 0:
        saved[springs + repr(damaged_groups)] = 0
        return 0
    if len(damaged_groups) == 0:
        if '#' not in springs:
            saved[springs + repr(damaged_groups)] = 1
            return 1
        saved[springs + repr(damaged_groups)] = 0
        return 0
    t = 0
    if try_pattern(f"{'#' * damaged_groups[0]}", springs) == True:
        # print(springs, springs[damaged_groups[0] + 1:])
        t += guess(springs[damaged_groups[0] + 1:], damaged_groups[1:])
        # r = guess(springs[1:], damaged_groups)
        # return t + r
    # print("T", t)
    if springs[0] == '#':
        saved[springs + repr(damaged_groups)] = t
        return t
    r = t + guess(springs[1:], damaged_groups)
    saved[springs + repr(damaged_groups)] = r
    return r


def guess2(springs, damaged_groups):
    i = springs.find("?")
    if i != -1:
        # print(springs)
        return guess2(f"{springs[:i]}#{springs[i + 1:]}", damaged_groups) + guess2(f"{springs[:i]}.{springs[i + 1:]}", damaged_groups)
    # print(springs, damaged_groups, count_groups(springs))
    return count_groups(springs) == damaged_groups


def get_new_springs(springs: str, damaged_groups: str):
    return f"{springs}?{springs}", f"{damaged_groups},{damaged_groups}"

def get_new_springs5(springs: str, damaged_groups: str):
    return f"{springs}?{springs}?{springs}?{springs}?{springs}", f"{damaged_groups},{damaged_groups},{damaged_groups},{damaged_groups},{damaged_groups}"

def main():
    with open("input.txt") as file:
        lines = file.read().split('\n')[:-1]

    sum = 0
    for i, line in enumerate(lines):
        print(i, line)
        # springs, damaged_groups = line.split()
        # first_pattern = guess(springs, list(map(int, damaged_groups.split(","))))
        # springs, damaged_groups = get_new_springs(*line.split())
        # ttt = guess2(springs, list(map(int, damaged_groups.split(","))))
        # second_pattern = guess(springs, list(map(int, damaged_groups.split(","))))
        springs, damaged_groups = get_new_springs5(*line.split())
        # if first_pattern * pow(second_pattern // first_pattern, 4) != guess(springs, list(map(int, damaged_groups.split(",")))):
            # print(springs, damaged_groups)
        # if ttt != second_pattern:
        #     print(ttt, second_pattern, springs, damaged_groups)
        # print()
        # sum += first_pattern * pow(second_pattern // first_pattern, 4)
        sum += guess(springs, list(map(int, damaged_groups.split(","))))
    print(sum)


if __name__ == "__main__":
    main()