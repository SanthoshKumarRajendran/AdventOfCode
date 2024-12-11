f = open('input.txt', 'r')

# operator
# 0 : Add
# 1 : Multiply
# 2 : Concatenate

def perform_operation(current, rest, operation, i):
    if len(rest) == 1:
        if operation == 2: # Concatenate
            return int(str(rest[0]) + str(current))
        elif operation == 1: # Multiply
            return current * rest[0]
        else: # Add
            return current + rest[0]

    if operation == 2: # Concatenate
        return int(str(perform_operation(rest[0], rest[1:], i % 3, int(i/3))) + str(current))
    if operation == 1: # Multiply
        return current * perform_operation(rest[0], rest[1:], i % 3, int(i/3))
    else: # Add
        return current + perform_operation(rest[0], rest[1:], i % 3, int(i/3))

total_calibration_result = 0

for line in f:
    target_total_str, num_str_parts = line.strip().split(': ')
    target_total = int(target_total_str)
    numbers = [int(num) for num in num_str_parts.split()][::-1]

    for i in range(3 ** (len(numbers) - 1)):
        total = perform_operation(numbers[0], numbers[1:], i % 3, int(i/3))
        if target_total == total:
            total_calibration_result += target_total
            break

print(total_calibration_result)
