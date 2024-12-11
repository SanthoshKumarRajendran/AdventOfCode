f = open('input.txt', 'r')

hiking_map, trail_head_positions, x_pos = [], [], 0
for line in f:
    char_list = list(line.strip())
    hiking_map.append([int(x) for x in char_list])
    for i in range(len(char_list)):
        if char_list[i] == '0':
            trail_head_positions.append((x_pos, i))
    x_pos += 1

##################################################

TRAILS_PATHS_FOUND = 0

def valid_neighbors(x_pos, y_pos):
    valid_x_coordinate = range(len(hiking_map))
    valid_y_coordinate = range(len(hiking_map[0]))

    possible_neighbors = [(x_pos-1, y_pos), # UP
                          (x_pos, y_pos-1), # LEFT
                          (x_pos, y_pos+1), # RIGHT
                          (x_pos+1, y_pos)] # DOWN

    valid_neighbors = []
    for x, y in possible_neighbors:
        if x in valid_x_coordinate and y in valid_y_coordinate:
            valid_neighbors.append((x,y))
    
    return valid_neighbors

def find_path(x_pos, y_pos, next_height, trail_head_location):
    global TRAILS_PATHS_FOUND
    for x,y in valid_neighbors(x_pos, y_pos):
        if hiking_map[x][y] == next_height:
            if next_height == 9:
                TRAILS_PATHS_FOUND += 1
            else:
                find_path(x, y, next_height + 1, trail_head_location)

for x, y in trail_head_positions:
    find_path(x, y, 1, (x,y))

print(TRAILS_PATHS_FOUND)
