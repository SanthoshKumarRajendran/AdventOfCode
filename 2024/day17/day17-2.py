REGISTER_A = None
REGISTER_B = None
REGISTER_C = None
PROGRAM = None

with open('input.txt', 'r') as f:
    for line in f:
        if 'Register A' in line:
            REGISTER_A = int(line.strip().split(': ')[-1])
        if 'Register B' in line:
            REGISTER_B = int(line.strip().split(': ')[-1])
        if 'Register C' in line:
            REGISTER_C = int(line.strip().split(': ')[-1])
        if 'Program' in line:
            PROGRAM = [int(x) for x in line.strip().split(': ')[-1].split(',')]

############################################################

OUTPUT = []

def get_combo_operand_value(operand_val):
    if operand_val == 4:
        return REGISTER_A
    if operand_val == 5:
        return REGISTER_B
    if operand_val == 6:
        return REGISTER_C    
    # if operand_val == 7:
    #     raise Exception("Invalid Operand Value of 7 detected")
    return operand_val

def adv_instruction(operand_val):
    global REGISTER_A
    numerator = REGISTER_A
    denominator = 2 ** get_combo_operand_value(operand_val)
    REGISTER_A = int(numerator/denominator)

def bxl_instruction(operand_val):
    global REGISTER_B
    REGISTER_B = REGISTER_B ^ operand_val

def bst_instruction(operand_val):
    global REGISTER_B
    REGISTER_B = get_combo_operand_value(operand_val) % 8

# THIS IS HANDLED INLINE
# def jnz_instruction(operand_val):
#     pass

def bxc_instruction(operand_val):
    global REGISTER_B
    REGISTER_B = REGISTER_B ^ REGISTER_C

def out_instruction(operand_val):
    OUTPUT.append(get_combo_operand_value(operand_val) % 8)

def bdv_instruction(operand_val):
    global REGISTER_B
    numerator = REGISTER_A
    denominator = 2 ** get_combo_operand_value(operand_val)
    REGISTER_B = int(numerator/denominator)

def cdv_instruction(operand_val):
    global REGISTER_C
    numerator = REGISTER_A
    denominator = 2 ** get_combo_operand_value(operand_val)
    REGISTER_C = int(numerator/denominator)

instruction_set_map = {
    0: adv_instruction,
    1: bxl_instruction,
    2: bst_instruction,
    # 3: jnz_instruction,  Handled inline
    4: bxc_instruction,
    5: out_instruction,
    6: bdv_instruction,
    7: cdv_instruction
}

def get_output(reg_a_val):
    global REGISTER_A, PROGRAM, OUTPUT
    REGISTER_A, OUTPUT = reg_a_val, []

    i = 0
    while i < len(PROGRAM):
        instruction, operand = PROGRAM[i], PROGRAM[i+1]
        # print(f"Processing instruction: {instruction} operand: {operand}")

        if instruction == 3:
            if REGISTER_A:        
                i = operand - 2
        else:
            instruction_set_map[instruction](operand)

        i += 2

    return OUTPUT

register_a_candidate = 0
program_len = len(PROGRAM)
for x in range(program_len):
    register_a_candidate = register_a_candidate * 8

    while PROGRAM[program_len-x-1:] != get_output(register_a_candidate):
        register_a_candidate += 1

    print(register_a_candidate)

print(register_a_candidate)
