def _calculate_single_fuel(mass: int) -> int:
    """Calculate initial fuel needed for a module based on its mass."""
    return max(0, (mass // 3) - 2)

def _calculate_recursive_fuel(mass: int) -> int:
    """Recursively calculate total fuel including fuel for the fuel itself."""
    fuel = _calculate_single_fuel(mass)
    if fuel > 0:
        return fuel + _calculate_recursive_fuel(fuel)
    return fuel

def calculate_total_fuel() -> int:
    """Calculate total fuel required for all modules, including recursive fuel."""
    with open("src/day_1/data/validation_input.txt", "r") as f:
        masses = [int(line.strip()) for line in f.readlines()]
    
    total_fuel = sum(_calculate_recursive_fuel(mass) for mass in masses)
    return total_fuel

if __name__ == "__main__":
    print(f"Total fuel required: {calculate_total_fuel()}")
