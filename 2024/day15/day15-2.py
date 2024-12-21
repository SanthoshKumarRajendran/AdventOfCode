from copy import deepcopy
from enum import Enum
import pdb

class THING(Enum):
    BOX_L = '['
    BOX_R = ']'
    WALL = '#'
    NOTHING = '.'
    ROBOT = '@'

class MOVE(Enum):
    UP = '^'
    RIGHT = '>'
    DOWN = 'v'
    LEFT = '<'

def output_warehouse(map):
    for x in map:
        print([i.value for i in x])

warehouse_map = []
with open('input_map.txt', 'r') as f:
    for line in f:
        warehouse_row = []
        for x in line.strip():
            if x == 'O':
                warehouse_row.append(THING.BOX_L)
                warehouse_row.append(THING.BOX_R)    
            elif x == '@':
                warehouse_row.append(THING.ROBOT)
                warehouse_row.append(THING.NOTHING)
            else:
                warehouse_row.append(THING(x))
                warehouse_row.append(THING(x))
        warehouse_map.append(warehouse_row)

robot_pos = None
for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map)):
        if warehouse_map[i][j] == THING.ROBOT:
            robot_pos = (i, j)
            break

output_warehouse(warehouse_map)
# print(robot_pos)

robot_moves = []
with open('input_moves.txt', 'r') as f:
    for line in f:
        for move in line.strip():
            robot_moves.append(MOVE(move))

# print(robot_moves)

##################################################

pos_diff = {
    MOVE.UP: (-1,0),
    MOVE.RIGHT: (0,1),
    MOVE.DOWN: (1,0),
    MOVE.LEFT: (0,-1)
}

def is_valid_pos(x_pos, y_pos):
    warehouse_dimension_x = len(warehouse_map)
    warehouse_dimension_y = len(warehouse_map[0])
    return (0 <= x_pos < warehouse_dimension_x) and (0 <= y_pos < warehouse_dimension_y)

def move_boxes_left_or_right(to_pos_x, to_pos_y, direction):
    global robot_pos

    robot_pos_x, robot_pos_y = robot_pos
    x_diff, y_diff = pos_diff[direction]

    new_pos_x, new_pos_y = to_pos_x, to_pos_y
    while not ((new_pos_x == robot_pos_x) and (new_pos_y == robot_pos_y)):
        warehouse_map[new_pos_x][new_pos_y] = warehouse_map[new_pos_x - x_diff][new_pos_y - y_diff]
        new_pos_x, new_pos_y = new_pos_x - x_diff, new_pos_y - y_diff
    warehouse_map[robot_pos_x][robot_pos_y] = THING.NOTHING

def find_all_box_pos_to_be_move_up_or_down(current_pos_x, current_pos_y, direction, box_pos_to_be_moved):
    x_diff, y_diff = pos_diff[direction]
    new_pos_x, new_pos_y = current_pos_x + x_diff, current_pos_y + y_diff

    if warehouse_map[new_pos_x][new_pos_y] == THING.WALL or warehouse_map[new_pos_x][new_pos_y] == THING.NOTHING:
        return
    elif warehouse_map[new_pos_x][new_pos_y] == THING.BOX_L:
        box_pos_to_be_moved.add((new_pos_x, new_pos_y))
        box_pos_to_be_moved.add((new_pos_x, new_pos_y + 1))
        find_all_box_pos_to_be_move_up_or_down(new_pos_x, new_pos_y, direction, box_pos_to_be_moved)
        find_all_box_pos_to_be_move_up_or_down(new_pos_x, new_pos_y + 1, direction, box_pos_to_be_moved)
    elif warehouse_map[new_pos_x][new_pos_y] == THING.BOX_R:
        box_pos_to_be_moved.add((new_pos_x, new_pos_y))
        box_pos_to_be_moved.add((new_pos_x, new_pos_y - 1))
        find_all_box_pos_to_be_move_up_or_down(new_pos_x, new_pos_y, direction, box_pos_to_be_moved)
        find_all_box_pos_to_be_move_up_or_down(new_pos_x, new_pos_y - 1, direction, box_pos_to_be_moved)
    else:
        print("SOMETHING IS WRONG")

def are_boxes_movable(boxes, direction):
    x_diff, y_diff = pos_diff[direction]
    for box_x, box_y in boxes:
        if warehouse_map[box_x + x_diff][box_y + y_diff] == THING.WALL:
            return False
    return True

def move_boxes_alt(boxes, direction):
    global warehouse_map
    x_diff, y_diff = pos_diff[direction]
    warehouse_map_new = deepcopy(warehouse_map)
    for box_x, box_y in boxes:
        warehouse_map_new[box_x + x_diff][box_y + y_diff] = warehouse_map[box_x][box_y]
    warehouse_map = warehouse_map_new

def move_boxes(boxes, direction):
    x_diff, y_diff = pos_diff[direction]
    direction_switch = 1 if direction == MOVE.UP else -1

    for x in range(len(warehouse_map))[::direction_switch]:
        for y in range(len(warehouse_map[0])):
            if (x,y) in boxes:
                warehouse_map[x + x_diff][y + y_diff] = warehouse_map[x][y]
                warehouse_map[x][y] = THING.NOTHING

def move_boxes_and_occupy(robot_pos_x, robot_pos_y, move):
    global robot_pos
    x_diff, y_diff = pos_diff[move]

    if move == MOVE.LEFT or move == MOVE.RIGHT:
        new_pos_x, new_pos_y = robot_pos_x + x_diff, robot_pos_y + y_diff
        while(is_valid_pos(new_pos_x, new_pos_y)):
            # if we encounter a wall before we find an empty space, then quit trying to move
            if warehouse_map[new_pos_x][new_pos_y] == THING.WALL:
                return
            # find if there's an empty space for the boxes to move if pushed
            if warehouse_map[new_pos_x][new_pos_y] == THING.NOTHING:
                move_boxes_left_or_right(new_pos_x, new_pos_y, move)
                robot_pos = (robot_pos_x + x_diff, robot_pos_y + y_diff)
                return
            new_pos_x, new_pos_y = new_pos_x + x_diff, new_pos_y + y_diff
    else:
        # here goes the complicated logic
        box_pos_to_be_moved = set([])
        find_all_box_pos_to_be_move_up_or_down(robot_pos_x, robot_pos_y, move, box_pos_to_be_moved)
        if are_boxes_movable(box_pos_to_be_moved, move):
            move_boxes(box_pos_to_be_moved, move)
            warehouse_map[robot_pos_x + x_diff][robot_pos_y + y_diff] = THING.ROBOT
            robot_pos = (robot_pos_x + x_diff, robot_pos_y + y_diff)
            warehouse_map[robot_pos_x][robot_pos_y] = THING.NOTHING

def move_robot(move):
    global robot_pos

    robot_pos_x, robot_pos_y = robot_pos
    x_diff, y_diff = pos_diff[move]
    new_pos_x, new_pos_y = robot_pos_x + x_diff, robot_pos_y + y_diff
    obstacle_at_new_pos = warehouse_map[new_pos_x][new_pos_y]

    if obstacle_at_new_pos == THING.WALL:
        return
    elif obstacle_at_new_pos == THING.NOTHING:
        warehouse_map[robot_pos_x][robot_pos_y] = THING.NOTHING
        warehouse_map[new_pos_x][new_pos_y] = THING.ROBOT
        robot_pos = (new_pos_x, new_pos_y)
    elif obstacle_at_new_pos == THING.BOX_L or obstacle_at_new_pos == THING.BOX_R:
        move_boxes_and_occupy(robot_pos_x, robot_pos_y, move)
    else:
        print("SOMETHING IS WRONG")

for move in robot_moves:
    # print(move)
    move_robot(move)
    # output_warehouse(warehouse_map)
    # pdb.set_trace()

# print("\n\n")
# output_warehouse(warehouse_map)

gps_sum = 0
for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map[0])):
        if warehouse_map[i][j] == THING.BOX_L:
            gps_sum += 100 * i + j

print(gps_sum)
