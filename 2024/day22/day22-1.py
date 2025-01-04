INITIAL_SECRET_NUMS = []
with open('input.txt', 'r') as f:
    for line in f:
        INITIAL_SECRET_NUMS.append(int(line.strip()))

# print(INITIAL_SECRET_NUMS)

#################################################################

def step_1(input):
    return ((input << 6) ^ input) % 16777216

def step_2(input):
    return ((input >> 5) ^ input) % 16777216

def step_3(input):
    return ((input << 11) ^ input) % 16777216

SUM_SECRET = 0
for num in INITIAL_SECRET_NUMS:
    step_num = num
    for _ in range(2000):
        step_1_output = step_1(step_num)
        step_2_output = step_2(step_1_output)
        step_num = step_3(step_2_output)
    SUM_SECRET += step_num
    # print(step_num)

print(SUM_SECRET)
