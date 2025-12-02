def is_repeating_pattern(num):
    """Check if a number is made of a repeating pattern (e.g., 121212 = '12' repeated)"""
    s = str(num)
    length = len(s)

    for pattern_len in range(1, length):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            if pattern * (length // pattern_len) == s and length // pattern_len >= 2:
                return True
    
    return False


def check_invalid_ids(filename, output_file):
    total = 0
    out = open(output_file, 'w')
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            lower = int(line.split('-')[0])
            upper = int(line.split('-')[1].split(',')[0])
            print(f"Processing range: {lower}-{upper}")
            
            range_sum = 0
            for i in range(lower, upper + 1):
                if  is_repeating_pattern(i): 
                    out.write(f"{i}\n")
            
            print(f"  Range sum: {range_sum}")
            total += range_sum
    
    out.close()
    print(f"\nTotal sum: {total}")

check_invalid_ids('./2ndday/input.txt','./2ndday/output.txt')


