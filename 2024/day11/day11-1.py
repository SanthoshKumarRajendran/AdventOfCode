stones_list = []
with open('input.txt', 'r') as f:
    stones_list = [int(x) for x in f.read().strip().split()]

############################################

blink_count = 25

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
    while(counter < len(stones_list)):
        num = stones_list[counter]
        ret_val = implement_rules(num)
        if type(ret_val) is int:
            stones_list[counter] = ret_val
        else:
            stones_list = stones_list[:counter] + ret_val + stones_list[counter+1:]
            counter += 1
        counter += 1

print(len(stones_list))
