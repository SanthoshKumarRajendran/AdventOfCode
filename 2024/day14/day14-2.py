from copy import deepcopy
import re
import time

bathroom_dimension_x = 101
bathroom_dimension_y = 103
seconds = 100

bathroom_map_robot_count = [ [ 0 ] * bathroom_dimension_x for _ in range(bathroom_dimension_y) ]
bathroom_map_robot_info = [ [ [] for _ in range(bathroom_dimension_x) ] for _ in range(bathroom_dimension_y) ]
robot_positions = set([])

# pprint(bathroom_map_robot_count)
# pprint(bathroom_map_robot_info)
# pprint(robot_positions)

with open('input.txt', 'r') as f:
    for line in f:
        search_string = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
        m = re.search(search_string, line.strip())
        pos_x = int(m.group(1))
        pos_y = int(m.group(2))
        vel_x = int(m.group(3))
        vel_y = int(m.group(4))
        robot_positions.add((pos_x, pos_y))
        bathroom_map_robot_count[pos_y][pos_x] += 1
        bathroom_map_robot_info[pos_y][pos_x].append((vel_x, vel_y))
        # import pdb; pdb.set_trace()

# pprint(bathroom_map_robot_count)
# pprint(bathroom_map_robot_info)
# pprint(robot_positions)

###############################################

# Actual problem goes here
def compute_next_position(pos_x, pos_y, vel_x, vel_y):
    next_x = pos_x + vel_x
    next_y = pos_y + vel_y

    if next_x >= bathroom_dimension_x:
        next_x = next_x - bathroom_dimension_x
    elif next_x < 0:
        next_x = next_x + bathroom_dimension_x
    
    if next_y >= bathroom_dimension_y:
        next_y = next_y - bathroom_dimension_y
    elif next_y < 0:
        next_y = next_y + bathroom_dimension_y

    return (next_x, next_y)


def update_bathroom(pos_x, pos_y, vel_x, vel_y, count_map, info_map):
    count_map[pos_y][pos_x] += 1
    info_map[pos_y][pos_x].append((vel_x, vel_y))


def print_to_file(robot_count_map):
    with open('output.txt', 'w') as f:
        for line in robot_count_map:
            line = [' ' if not x else '*' for x in line]
            f.write(''.join(line))
            f.write('\n')


def detect_tree_and_print(second, robot_count_map):
    for j in range(2, len(robot_count_map)-2):
        if sum(robot_count_map[j]) > 20:
            if sum(robot_count_map[j-1]) < sum(robot_count_map[j]) < sum(robot_count_map[j+1]):
                print(second + 1)
                print_to_file(robot_count_map)
                return


for i in range(10000000):
    bathroom_map_robot_count_new = [ [ 0 ] * bathroom_dimension_x for _ in range(bathroom_dimension_y) ]
    bathroom_map_robot_info_new = [ [ [] for _ in range(bathroom_dimension_x) ] for _ in range(bathroom_dimension_y) ]
    robot_positions_new = set([])

    for robot_pos_x, robot_pos_y in robot_positions:
        for robot_vel_x, robot_vel_y in bathroom_map_robot_info[robot_pos_y][robot_pos_x]:
            next_x, next_y = compute_next_position(robot_pos_x, robot_pos_y, robot_vel_x, robot_vel_y)
            update_bathroom(next_x, next_y, robot_vel_x, robot_vel_y, bathroom_map_robot_count_new, bathroom_map_robot_info_new)
            robot_positions_new.add((next_x, next_y))
        
        bathroom_map_robot_info[robot_pos_y][robot_pos_x] = []
        bathroom_map_robot_count[robot_pos_y][robot_pos_x] = 0

    detect_tree_and_print(i, bathroom_map_robot_count_new)

    bathroom_map_robot_count = deepcopy(bathroom_map_robot_count_new)
    bathroom_map_robot_info = deepcopy(bathroom_map_robot_info_new)
    robot_positions = robot_positions_new
