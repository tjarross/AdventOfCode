import functools


def main():
    with open("input.txt") as file:
        lines = file.readlines()
    area = 0
    for line in lines:
        l, w, h = map(int, line.split("x"))
        area += 2 * l * w + 2 * w * h + 2 * h * l + functools.reduce(lambda x, y: x * y, sorted([l, w, h])[:2])
    print(area)


if __name__ == "__main__":
    main()