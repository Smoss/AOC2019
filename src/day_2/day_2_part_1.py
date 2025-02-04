def read_input() -> list[int]:
    with open("src/day_2/data/input.txt", "r") as f:
        return list(map(int, f.readline().split(',')))

def main() -> int:
    data = read_input()
    # Replace position 1 and 2 as specified
    data[1] = 12
    data[2] = 2
    
    index = 0
    while True:
        opcode = data[index]
        if opcode == 99:
            break
        elif opcode == 1:
            pos1 = data[index + 1]
            pos2 = data[index + 2]
            result_pos = data[index + 3]
            data[result_pos] = data[pos1] + data[pos2]
            index += 4
        elif opcode == 2:
            pos1 = data[index + 1]
            pos2 = data[index + 2]
            result_pos = data[index + 3]
            data[result_pos] = data[pos1] * data[pos2]
            index += 4
        else:
            raise ValueError(f"Unknown opcode {opcode}")
    
    return data[0]

if __name__ == "__main__":
    print(main())
