import datetime
import time

List = [
    # "???.### 1,1,3",
    # ".??..??...?##. 1,1,3",
    # "?#?#?#?#?#?#?#? 1,3,1,6",
    # "????.#...#... 4,1,1",
    # "????.######..#####. 1,6,5",
    # "?###???????? 3,2,1",
    "????#????.???????????????#????.?????????? 1,4,2,1,7,1,4,2,1,7"
]


def count_groups(springs: str):
    return [len(word) for word in springs.split(".") if len(word) != 0]


def guess(springs, damaged_groups):
    i = springs.find("?")
    if i != -1:
        print(springs)
        return guess(f"{springs[:i]}#{springs[i + 1:]}", damaged_groups) + guess(f"{springs[:i]}.{springs[i + 1:]}", damaged_groups)
    # print(springs, damaged_groups, count_groups(springs))
    return count_groups(springs) == damaged_groups


def get_new_springs(springs: str, damaged_groups: str):
    return f"{springs}?{springs}", f"{damaged_groups},{damaged_groups}"


def main():
    with open("input.txt") as file:
        lines = List#sorted(file.readlines(), key=lambda x: x.count("?"), reverse=True)

    sum = 0
    start = time.time()
    for i, line in enumerate(lines):
        springs, damaged_groups = line.split()
        first_pattern = guess(springs, list(map(int, damaged_groups.split(","))))
        springs, damaged_groups = get_new_springs(*line.split())
        second_pattern = guess(springs, list(map(int, damaged_groups.split(","))))
        sum += first_pattern * pow(second_pattern // first_pattern, 4)
        end = time.time() - start
        # print(f"{i + 1} {len(lines)} -- {int(end // 3600)}:{int(end // 60)}:{end % 60:.2f} -- {springs}")
    print(sum)


if __name__ == "__main__":
    main()