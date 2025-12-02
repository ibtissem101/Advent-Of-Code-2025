import math

def find_invalid_ids(filename,output_file):
    total = 0
    out = open(output_file, 'w')
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            lower = int(line.split('-')[0])
            upper = int(line.split('-')[1].split(',')[0])
            print(lower, upper) 
            range_sum = 0

            for i in range(lower, upper + 1):
                n = int(math.log10(i)) + 1 
                if n % 2 != 0:
                    continue  
                h = n // 2
                divisor = 10 ** h
                first_half = i // divisor
                second_half = i % divisor
                if first_half == second_half:
                    range_sum += i
                    out.write(f"{i}\n")

            total += range_sum

    print(total)

find_invalid_ids('./2ndday/input.txt','./2ndday/output.txt')
