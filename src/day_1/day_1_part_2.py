def _calculate_fuel(mass: int) -> int:
    """Calculate fuel needed for a module based on its mass."""
    if mass <= 0:
        return 0
    return (mass // 3) - 2

def calculate_total_fuel() -> int:
    """Calculate total fuel required for all modules, including recursive fuel."""
    with open("src/day_1/data/validation_input.txt", "r") as f:
        masses = [int(line.strip()) for line in f.readlines()]
    
    total_fuel = sum(_calculate_fuel(mass) + _calculate_fuel(_calculate_fuel(mass)) 
                    for mass in masses)
    return total_fuel

if __name__ == "__main__":
    print(f"Total fuel required: {calculate_total_fuel()}")
