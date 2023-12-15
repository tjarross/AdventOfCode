def hash(pattern):
    h = 0 
    for c in pattern:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def main():
    with open("input.txt") as file:
        line = file.read().split("\n")[0]

    patterns = []
    for pattern in line.split(","):
            patterns.append(pattern)

    boxes = {}
    for pattern in patterns:
        if "=" in pattern:
            key, value = pattern.split("=")
            boxes.setdefault(hash(key), [])
            for i in range(len(boxes[hash(key)])):
                if key in boxes[hash(key)][i]:
                    boxes[hash(key)][i][key] = value
                    break
            else:
                boxes[hash(key)].append({key: value})
        if "-" in pattern:
            key = pattern[:-1]
            for box_key in boxes:
                for i in range(len(boxes[box_key])):
                    if key in boxes[box_key][i]:
                        del boxes[box_key][i][key]
    
    filtered_boxes = {}
    for box_key in boxes:
        for i in range(len(boxes[box_key])):
            if boxes[box_key][i] != {}:
                filtered_boxes.setdefault(box_key, [])
                filtered_boxes[box_key].append(boxes[box_key][i])
    sum = 0
    for box_key in filtered_boxes:
        for i, pattern in enumerate(filtered_boxes[box_key]):
            sum += (box_key + 1) * (i + 1) * int(list(pattern.values())[0])
    print(sum)


if __name__ == "__main__":
    main()