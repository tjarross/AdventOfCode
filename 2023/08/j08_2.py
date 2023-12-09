import re
import math


network = {}

def main():
    with open("input.txt") as file:
        lines = file.read().split("\n")[:-1]
        instructions = lines[0]
        for line in lines[2:]:
            node1, node2, node3 = re.findall(r"[A-Z]{3}", line)
            network[node1] = {"L": node2, "R": node3}
        
        current_nodes = [node for node in network if node[-1] == "A"]
        first_z_values = [0] * len(current_nodes)
        i = 0
        while True:
            current_nodes = [network[current_node][instructions[i % len(instructions)]] for current_node in current_nodes]
            for j, node in enumerate(current_nodes):
                if node[-1] == "Z" and first_z_values[j] == 0:
                    first_z_values[j] = i + 1
            if 0 not in first_z_values:
                break
            i += 1

        print(math.lcm(*first_z_values))


if __name__ == "__main__":
    main()