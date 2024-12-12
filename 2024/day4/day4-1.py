SEARCH_TEXT = "XMAS"
f = open('input.txt', 'r')

char_grid = []
for line in f:
    char_list = list(line.strip())
    char_grid.append(char_list)

##################################################

SEARCH_TEXT_COUNT = 0

def valid_neighbors(x_pos, y_pos, path):
    valid_x_coordinate = range(len(char_grid))
    valid_y_coordinate = range(len(char_grid[0]))

    if len(path) > 1:
        #there's only one valid next option if a direction is already decided
        possible_neighbors = [(x_pos + (path[-1][0] - path[-2][0]),
                               y_pos + (path[-1][1] - path[-2][1]))]
    else:
        possible_neighbors = [(x_pos-1, y_pos-1), (x_pos-1, y_pos), (x_pos-1, y_pos+1),
                              (x_pos, y_pos-1), (x_pos, y_pos+1),
                              (x_pos+1, y_pos-1), (x_pos+1, y_pos), (x_pos+1, y_pos+1)]

    valid_neighbors = []
    for x, y in possible_neighbors:
        if x in valid_x_coordinate and y in valid_y_coordinate:
            valid_neighbors.append((x,y))
    
    return valid_neighbors

def find_text(found_count, x_pos, y_pos, path):
    global SEARCH_TEXT_COUNT

    next_char_to_find = SEARCH_TEXT[found_count]
    for x,y in valid_neighbors(x_pos, y_pos, path):
        if char_grid[x][y] == next_char_to_find:
            if found_count == 3:
                SEARCH_TEXT_COUNT += 1
                return
            else:
                find_text(found_count+1, x, y, path + [(x,y)])
    return

for x in range(len(char_grid)):
    for y in range(len(char_grid[x])):
        if char_grid[x][y] == SEARCH_TEXT[0]:
            find_text(1, x, y, [(x,y)])

print(SEARCH_TEXT_COUNT)
