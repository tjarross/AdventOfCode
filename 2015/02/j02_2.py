import functools


def main():
    with open("input.txt") as file:
        lines = file.readlines()
    ribbon_length = 0
    for line in lines:
        l, w, h = map(int, line.split("x"))
        ribbon_length += 2 * sum(sorted([l, w, h])[:2]) + functools.reduce(lambda x, y: x * y, [l, w, h])
    print(ribbon_length)


if __name__ == "__main__":
    main()