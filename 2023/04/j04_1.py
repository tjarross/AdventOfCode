def main():
    sum = 0
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        for line in lines:
            winning_cards = line.split(":")[1].split("|")[0].split()
            my_cards = line.split(":")[1].split("|")[1].split()

            points = int(pow(2, len(set(winning_cards).intersection(my_cards)) - 1))
            sum += points
    print(sum)


if __name__ == "__main__":
    main()