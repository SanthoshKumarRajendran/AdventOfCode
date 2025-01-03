from copy import deepcopy
from pprint import pprint
from sys import maxsize

BIG_NUM = maxsize
MEMORY_MAP_DIMENSION = 71

MEMORY_MAP = [ [ '.' ] * MEMORY_MAP_DIMENSION for _ in range(MEMORY_MAP_DIMENSION) ]
CORRUPTED_MEMORY_LOCATIONS = []

with open("input.txt", 'r') as f:
    for line in f:
        x, y = line.strip().split(',')
        x, y = int(x), int(y)
        CORRUPTED_MEMORY_LOCATIONS.append((x, y))

# pprint(MEMORY_MAP)

####################################################################

def check_out_of_bounds(x, y):
    return (x < 0) or (x > MEMORY_MAP_DIMENSION-1) or (y < 0) or (y > MEMORY_MAP_DIMENSION-1)

def get_neighbors(x, y):
    possible_neighbors = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
    valid_neighbors = []

    for pos_x, pos_y in possible_neighbors:
        if check_out_of_bounds(pos_x, pos_y) or MEMORY_MAP[pos_y][pos_x] == '#':
            continue
        valid_neighbors.append((pos_x, pos_y))

    return valid_neighbors

def path_exists():
    START_POS = (0,0)
    END_POS = (70,70)
    PROCESS_QUEUE = []
    PROCESS_QUEUE.append((START_POS, set([START_POS])))
    SHORTEST_PATH_AT_POS = {
        START_POS: 1
    }

    while(PROCESS_QUEUE):
        position, path = PROCESS_QUEUE.pop(0)
        if position == END_POS:
            return True

        neighbors = get_neighbors(*position)
        for neighbor in neighbors:
            if neighbor not in path:
                path_copy = deepcopy(path)
                path_copy.add(neighbor)
                if SHORTEST_PATH_AT_POS.get(neighbor, BIG_NUM) <= len(path_copy):
                    continue
                PROCESS_QUEUE.append((neighbor, path_copy))
                SHORTEST_PATH_AT_POS[neighbor] = len(path_copy)

for loc_x, loc_y in CORRUPTED_MEMORY_LOCATIONS:
    MEMORY_MAP[loc_y][loc_x] = '#'
    if path_exists():
        continue
    print(loc_x,loc_y)
    exit(0)
