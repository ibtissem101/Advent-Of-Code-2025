def find_best_left_digit(n):
    s = str(n)
    i = 0
    while i < len(s) - 1:
        jump = False
        for j in range(i + 1, len(s)-1):
            if s[i] < s[j]:
                i = j
                jump = True
                break
        if not jump:
            break
    return i  


def find_best_joltage(n):
    s = str(n)
    left_index = find_best_left_digit(n)
    left_digit = s[left_index]
    best_joltage = -1
    for i in range(left_index + 1, len(s)):
        combination = int(left_digit + s[i])
        if combination > best_joltage:
            best_joltage = combination

    return best_joltage


def total_output_joltage(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  
            joltage_sum = 0

            joltage_sum = find_best_joltage(int(line))
            total += joltage_sum
    print(f"\nTotal sum: {total}")

    return total

total_output_joltage('./3rdday/input.txt')