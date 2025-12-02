"""
Advent of Code - Safe Dial Puzzle
The dial starts at 50 and has numbers 0-99 in a circle.
We need to count how many times the dial lands on 0 after rotations.
"""

def solve_safe_dial(filename):
    position = 50
    count_zeros = 0
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])
            
            if direction == 'L':
                for _ in range(distance):
                    position = (position - 1) % 100
                    if position == 0:
                        count_zeros += 1
                
            else:  # R
                for _ in range(distance):
                    position = (position + 1) % 100
                    if position == 0:
                        count_zeros += 1

    return count_zeros


if __name__ == "__main__":
    # Test with the example first
    print("=" * 50)
    print("Testing with example:")
    print("=" * 50)
    example_rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    
    position = 50
    count = 0
    print(f"Start: position = {position}")
    
    for rotation in example_rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        
        if position == 0:
            count += 1
            print(f"{rotation}: position = {position} ★ (count = {count})")
        else:
            print(f"{rotation}: position = {position}")
    
    print(f"\nExample answer: {count} (expected: 3)")
    
    # Now solve the actual puzzle
    print("\n" + "=" * 50)
    print("Solving actual puzzle:")
    print("=" * 50)
    
    answer = solve_safe_dial('input.txt')
    
    print("\n" + "=" * 50)
    print(f"\n THE PASSWORD IS: {answer}")
    print("=" * 50)
