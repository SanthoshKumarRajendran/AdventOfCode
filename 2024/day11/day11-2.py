stones_dict = {}
with open('input.txt', 'r') as f:
    for x in f.read().strip().split():
        stones_dict[int(x)] = 1

############################################

blink_count = 75

def implement_rules(num):
    num_str = str(num)
    num_str_len = len(num_str)

    if num == 0:
        return 1
    elif num_str_len % 2 == 0:
        left_half = int(num_str[:int(num_str_len/2)])
        right_half = int(num_str[int(num_str_len/2):])
        return [left_half, right_half, ]
    else:
        return num * 2024

for i in range(blink_count):
    counter = 0
    new_stones_dict = {}

    for stone in stones_dict.keys():
        ret_val = implement_rules(stone)
        if type(ret_val) is int:
            if ret_val not in new_stones_dict:
                new_stones_dict[ret_val] = stones_dict[stone]
            else:
                new_stones_dict[ret_val] += stones_dict[stone]
        else:
            stone_1, stone_2 = ret_val
            if stone_1 not in new_stones_dict:
                new_stones_dict[stone_1] = stones_dict[stone]
            else:
                new_stones_dict[stone_1] += stones_dict[stone]
            if stone_2 not in new_stones_dict:
                new_stones_dict[stone_2] = stones_dict[stone]
            else:
                new_stones_dict[stone_2] += stones_dict[stone]
    
    stones_dict = new_stones_dict

print(sum(stones_dict.values()))
