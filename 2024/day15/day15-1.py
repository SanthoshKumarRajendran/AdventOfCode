# from pprint import pprint
from enum import Enum

class THING(Enum):
    BOX = 'O'
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
robot_pos = None
with open('input_map.txt', 'r') as f:
    x = 0
    for line in f:
        warehouse_map.append([ THING(x) for x in line.strip()])
        if '@' in line:
            robot_pos = (x, line.index('@'))
        x += 1

# output_warehouse(warehouse_map)
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
    warehouse_dimension = len(warehouse_map)
    return (0 <= x_pos < warehouse_dimension) and (0 <= y_pos < warehouse_dimension)

def move_boxes_and_occupy(robot_pos_x, robot_pos_y, x_diff, y_diff):
    global robot_pos

    new_pos_x, new_pos_y = robot_pos_x + x_diff, robot_pos_y + y_diff
    while(is_valid_pos(new_pos_x, new_pos_y)):
        # if we encounter a wall before we find an empty space, then quit trying to move
        if warehouse_map[new_pos_x][new_pos_y] == THING.WALL:
            return
        # find if there's an empty space for the boxes to move if pushed
        if warehouse_map[new_pos_x][new_pos_y] == THING.NOTHING:
            warehouse_map[robot_pos_x][robot_pos_y] = THING.NOTHING
            warehouse_map[new_pos_x][new_pos_y] = THING.BOX
            warehouse_map[robot_pos_x + x_diff][robot_pos_y + y_diff] = THING.ROBOT
            robot_pos = (robot_pos_x + x_diff, robot_pos_y + y_diff)
            return
        new_pos_x, new_pos_y = new_pos_x + x_diff, new_pos_y + y_diff

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
    elif obstacle_at_new_pos == THING.BOX:
        move_boxes_and_occupy(robot_pos_x, robot_pos_y, x_diff, y_diff)
    else:
        print("SOMETHING IS WRONG")

for move in robot_moves:
    # print(move)
    move_robot(move)
    # output_warehouse(warehouse_map)
    # import pdb; pdb.set_trace()

# output_warehouse(warehouse_map)

gps_sum = 0
for i in range(len(warehouse_map)):
    for j in range(len(warehouse_map)):
        if warehouse_map[i][j] == THING.BOX:
            gps_sum += 100 * i + j

print(gps_sum)
