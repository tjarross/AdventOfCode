digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def get_occurrence(string, digits):
    for i, _ in enumerate(string):
        for digit, digit_name in enumerate(digits):
            try:
                if string.index(str(digit)) == i:
                    return digit
            except:
                pass
            try:
                if string.index(digit_name) == i:
                    return digit
            except:
                pass
    return 0


def main():
    sum = 0
    with open("input.txt") as file:
        for line in file.read().split("\n")[:-1]:
            first_number = get_occurrence(line, digits)
            last_number = get_occurrence(line[::-1], [d[::-1] for d in digits])
            sum += first_number * 10 + last_number
    print(sum)

if __name__ == "__main__":
    main()