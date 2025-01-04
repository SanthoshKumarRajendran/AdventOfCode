from pprint import pprint

RACE_TRACK, START_POS, END_POS = [], None, None

with open("input.txt", 'r') as f:
    y = 0
    for line in f:
        track_line = list(line.strip())
        RACE_TRACK.append(track_line)
        if 'S' in track_line:
            START_POS = (track_line.index('S'), y)
        if 'E' in track_line:
            END_POS = (track_line.index('E'), y)
        y += 1

# pprint(RACE_TRACK)
# print(START_POS)
# print(END_POS)

#################################################################

def check_out_of_bounds(x, y):
    return (x < 0) or (x >= len(RACE_TRACK)) or (y < 0) or (y >= len(RACE_TRACK))

def get_next_location(x, y):
    possible_neighbors = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
    next_location = []

    for pos_x, pos_y in possible_neighbors:
        if check_out_of_bounds(pos_x, pos_y) or RACE_TRACK[pos_y][pos_x] == '#' or (pos_x, pos_y) in RACE_PATH:
            continue
        next_location.append((pos_x, pos_y))

    if len(next_location) > 1:
        raise Exception(f"More than one option found for {x},{y}")

    return next_location[0]

RACE_PATH = [START_POS]
curr_loc = START_POS
while(curr_loc != END_POS):
    next_pos = get_next_location(*curr_loc)
    RACE_PATH.append(next_pos)
    curr_loc = next_pos
RACE_PATH.append(END_POS)

# print(RACE_PATH)
# print(len(RACE_PATH) - 1) # time without cheating

#################################################################

def find_cheat_options(x, y, visited_locations):
    possible_locations_after_cheating = [(x-2, y), (x, y+2), (x+2, y), (x, y-2)]
    locations_for_walls_if_cheating = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]

    valid_locations_after_cheating = []
    for loc, wall in zip(possible_locations_after_cheating, locations_for_walls_if_cheating):
        x_loc, y_loc = loc
        x_wall, y_wall = wall
        if not check_out_of_bounds(x_loc, y_loc) and not check_out_of_bounds(x_wall, y_wall):
            if (RACE_TRACK[y_loc][x_loc] == '.' or RACE_TRACK[y_loc][x_loc] == 'E') and RACE_TRACK[y_wall][x_wall] == '#':
                if loc not in visited_locations:
                    valid_locations_after_cheating.append((x_loc, y_loc))

    return valid_locations_after_cheating

def calculate_time(location_1, location_2):
    # START_POS -> location_1 + 2 + location_2 -> END_POS
    location_1_index = RACE_PATH.index(location_1)
    location_2_index = RACE_PATH.index(location_2)
    return location_1_index + 2 + (len(RACE_PATH) - location_2_index)

CHEATS_THAT_SAVE_ATLEAST_HUNDRED = 0
VISITED_LOCATIONS = set([])

for race_path_location in RACE_PATH:
    for cheat_option in find_cheat_options(*race_path_location, VISITED_LOCATIONS):
        cheat_savings = len(RACE_PATH) - calculate_time(race_path_location, cheat_option)
        if cheat_savings > 99:
            CHEATS_THAT_SAVE_ATLEAST_HUNDRED += 1
    VISITED_LOCATIONS.add(race_path_location)

print(CHEATS_THAT_SAVE_ATLEAST_HUNDRED)
