from functools import cache

INITIAL_SECRET_NUMS = []

with open('input.txt', 'r') as f:
    for line in f:
        INITIAL_SECRET_NUMS.append(int(line.strip()))

# print(INITIAL_SECRET_NUMS)

#################################################################

@cache
def generate_secret(input):
    step_1_output = ((input << 6) ^ input) % 16777216
    step_2_output = ((step_1_output >> 5) ^ step_1_output) % 16777216
    return ((step_2_output << 11) ^ step_2_output) % 16777216

SECRET_SEQUENCE_DICT = {}
SEQUENCE_DICT_STATS = {}

for num in INITIAL_SECRET_NUMS:
    secret = num
    seq_found = set([])
    SECRET_SEQUENCE_DICT[num] = {
        'cost': [],
        'sequence': [],
    }

    for i in range(2000):
        new_secret = generate_secret(secret)
        SECRET_SEQUENCE_DICT[num]['cost'].append(new_secret % 10)
        SECRET_SEQUENCE_DICT[num]['sequence'].append(new_secret % 10 - secret % 10)
        if i >= 4:
            seq = tuple(SECRET_SEQUENCE_DICT[num]['sequence'][i-3:i+1])
            if seq not in seq_found:
                seq_found.add(seq)
                if seq not in SEQUENCE_DICT_STATS:
                    SEQUENCE_DICT_STATS[seq] = new_secret % 10
                else:
                    SEQUENCE_DICT_STATS[seq] += new_secret % 10
            
        secret = new_secret

# print(SECRET_SEQUENCE_DICT)
# print(SEQUENCE_DICT_STATS)

print(max(SEQUENCE_DICT_STATS.values()))
