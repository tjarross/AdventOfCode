import re


network = {}

def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        instructions = lines[0]
        for line in lines[2:]:
            node1, node2, node3 = re.findall(r"[A-Z]{3}", line)
            network[node1] = {"L": node2, "R": node3}
        
        current_node = "AAA"
        i = 0
        while True:
            current_node = network[current_node][instructions[i % len(instructions)]]
            if current_node == "ZZZ":
                break
            i += 1
        print(i + 1)
            


if __name__ == "__main__":
    main()