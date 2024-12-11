input_str = ''
with open('input.txt', 'r') as f:
    input_str = f.read().strip()

id_num = 0
disk_map = []
files_or_free_space = True # True => file, False => free space
for left_index in list(input_str):
    if files_or_free_space:
        char_list = [id_num] * int(left_index)
        id_num += 1
    else:
        char_list = ["."] * int(left_index)
    disk_map += char_list
    files_or_free_space = not files_or_free_space

##################################################################

file_sizes = []
free_disk_sizes = []

for i in range(len(input_str)):
    if (i % 2):
        free_disk_sizes.append(int(input_str[i]))
    else:
        file_sizes.append(int(input_str[i]))

def move_file_to_free_space(file_index_from_right, free_space_index, file_size):
    # recompute reversed lists
    free_disk_sizes_reversed = free_disk_sizes[::-1]
    file_sizes_reversed = file_sizes[::-1]

    # update disk_map
    free_space_start_index = sum(file_sizes[:free_space_index+1]) + sum(free_disk_sizes[:free_space_index])
    file_start_index_from_right = sum(file_sizes_reversed[:file_index_from_right+1]) + sum(free_disk_sizes_reversed[:file_index_from_right])
    file_start_index_from_left = len(disk_map) - file_start_index_from_right
    
    for i in range(file_size):
        temp = disk_map[file_start_index_from_left + i]
        disk_map[file_start_index_from_left + i] = disk_map[free_space_start_index + i]
        disk_map[free_space_start_index + i] = temp

    free_disk_sizes[free_space_index] -= file_size
    file_sizes[free_space_index] += file_size

def find_free_space(requested_size, file_index):
    for index in range(len(free_disk_sizes) - file_index):
        if free_disk_sizes[index] >= requested_size:
            return index

file_sizes_reversed = file_sizes[::-1]
for index in range(len(file_sizes_reversed)):
    file_size = file_sizes_reversed[index]
    free_space_index = find_free_space(file_size, index)

    if free_space_index is not None:
        move_file_to_free_space(index, free_space_index, file_size)

# for sanity's sake, pulling the checksum calculation out
checksum = 0
for index, value in zip(range(len(disk_map)), disk_map):
    if isinstance(value, str):
        continue
    checksum += index * value

print(checksum)
