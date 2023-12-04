import re


def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        lines_sum = [1] * len(lines)
        for line in lines:
            card_number = int(re.match(r"Card\s+(\d+)", line).group(1))
            winning_cards = line.split(":")[1].split("|")[0].split()
            my_cards = line.split(":")[1].split("|")[1].split()

            matches = set(winning_cards).intersection(my_cards)
            for i in range(card_number, card_number + len(matches)):
                lines_sum[i] += lines_sum[card_number - 1]
        print(sum(lines_sum))


if __name__ == "__main__":
    main()