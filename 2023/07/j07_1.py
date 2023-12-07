cards = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
]

hand_types = [
    [1, 1, 1, 1, 1],
    [2, 1, 1, 1],
    [2, 2, 1],
    [3, 1, 1],
    [3, 2],
    [4, 1],
    [5],
]


def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        draw_strength = []
        for line in lines:
            draw, bid = line.split()
            strength = [n for n in sorted([draw.count(card) for card in cards], reverse=True) if n != 0]
            draw_strength.append({"draw": draw, "strength": strength, "bid": bid})

        draw_strength.sort(key=lambda x: [hand_types.index(x['strength'])] + [cards.index(c) for c in x['draw']])

        print(sum([int(ds["bid"]) * (i + 1) for i, ds in enumerate(draw_strength)]))


if __name__ == "__main__":
    main()