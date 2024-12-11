input_str = ''
with open('input.txt', 'r') as f:
    input_str = f.read().strip()

id_num = 0
disk_map = []
files_or_free_space = True # True => file, False => free space
for x in list(input_str):
    if files_or_free_space:
        char_list = [id_num] * int(x)
        id_num += 1
    else:
        char_list = [f".{x}"] * int(x)
    disk_map += char_list
    files_or_free_space = not files_or_free_space

##################################################################

right_index = len(disk_map)

def find_next_valid_right_index(x):
    x -= 1
    while(isinstance(disk_map[x], str)):
        x -= 1
    return x

for x in range(len(disk_map)):
    if isinstance(disk_map[x], str):
        right_index = find_next_valid_right_index(right_index)
        if x < right_index: # swap number and .x
            val = disk_map[right_index]
            disk_map[right_index] = disk_map[x]
            disk_map[x] = val
        else:
            break

# for sanity's sake, pulling the checksum calculation out
checksum = 0
for index, value in zip(range(len(disk_map)), disk_map):
    if isinstance(value, str):
        break
    checksum += index * value

print(checksum)
