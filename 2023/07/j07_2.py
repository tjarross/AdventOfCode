cards = [
    "J",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
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


def get_highest_hand_type(strength: list, nb_J: int):
    if nb_J == 0:
        return strength
    if strength[0] != nb_J:
        if strength == hand_types[2]:
            return hand_types[5] if nb_J == 2 else hand_types[4]
    if strength == hand_types[0]:
        return hand_types[1]
    if strength == hand_types[1]:
        return hand_types[3]
    if strength in hand_types[2:4]:
        return hand_types[5]
    elif strength in hand_types[4:7]:
        return hand_types[6]

def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        draw_strength = []
        for line in lines:
            draw, bid = line.split()
            strength = [n for n in sorted([draw.count(card) for card in cards], reverse=True) if n != 0]
            jocker_strength = get_highest_hand_type(strength, draw.count('J'))
            draw_strength.append({"draw": draw, "strength": jocker_strength, "bid": bid})

        draw_strength.sort(key=lambda x: [hand_types.index(x['strength'])] + [cards.index(c) for c in x['draw']])

        print(sum([int(ds["bid"]) * (i + 1) for i, ds in enumerate(draw_strength)]))


if __name__ == "__main__":
    main()