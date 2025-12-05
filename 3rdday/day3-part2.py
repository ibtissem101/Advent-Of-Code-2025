def find_best_digit(s, positions_remaining):
    """
    Find the index of the best left digit in string s,
    using the hop-based greedy algorithm.
    """
    i = 0
    while i < len(s):
        jumped = False
        for j in range(i + 1, len(s)):
            remaining_after = len(s) - j  # digits including s[j]
            if s[j] > s[i] and remaining_after >= positions_remaining:
                i = j  # hop to bigger digit
                jumped = True
                break
        if not jumped:
            break
    return i  # index of chosen digit


def find_best_joltage(n, total_digits=12):
    """
    Build the largest possible `total_digits`-digit number
    from n using the hop-based greedy algorithm.
    """
    s = str(n)
    result = ""
    positions_remaining = total_digits

    while positions_remaining > 0:
        best_index = find_best_digit(s, positions_remaining)
        result += s[best_index]
        # remove everything up to and including the chosen digit
        s = s[best_index + 1:]
        positions_remaining -= 1

    return int(result)


def total_output_joltage(filename):
    """
    Compute the total sum of best joltages for each line in a file.
    """
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            joltage_sum = find_best_joltage(int(line))
            total += joltage_sum

    print(f"\nTotal sum: {total}")
    return total


total_output_joltage('./3rdday/input.txt')