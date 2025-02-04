from collections import defaultdict

def read_input() -> list[int]:
    with open("src/day_2/data/input.txt", "r") as f:
        return list(map(int, f.readline().split(',')))

def main() -> int:
    data_list = read_input()
    
    # Initialize memory with default values
    memory = defaultdict(int)
    for index, value in enumerate(data_list):
        memory[index] = value
    
    # Replace position 1 and 2 as specified
    memory[1] = 12
    memory[2] = 2
    
    index = 0
    while True:
        opcode = memory[index]
        if opcode == 99:
            break
        elif opcode == 1:
            pos1 = memory[index + 1]
            pos2 = memory[index + 2]
            result_pos = memory[index + 3]
            memory[result_pos] = memory[pos1] + memory[pos2]
            index += 4
        elif opcode == 2:
            pos1 = memory[index + 1]
            pos2 = memory[index + 2]
            result_pos = memory[index + 3]
            memory[result_pos] = memory[pos1] * memory[pos2]
            index += 4
        else:
            raise ValueError(f"Unknown opcode {opcode}")
    
    return memory[0]

if __name__ == "__main__":
    print(main())
