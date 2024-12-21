from copy import deepcopy
from enum import Enum

class THING(Enum):
    WALL = '#'
    NOTHING = '.'
    DEER = 'S'
    END_TILE = 'E'

class MOVE(Enum):
    M_UP = 1 # Move Forward
    R_CL_M_UP = 2 # Rotate Clockwise and Move Forward
    R_CNTR_CL_M_UP = 3 # Rotate Counter Clockwise and Move Forward

class DIRECTION(Enum):
    NORTH = 'North'
    EAST = 'East'
    SOUTH = 'South'
    WEST = 'West'

class Deer:
    def __init__(self, x, y, direction=DIRECTION.EAST, score=0, locations_visited={}):
        self.x_pos = x
        self.y_pos = y
        self.direction = direction
        self.score = score
        self.locations_visited = { str((x,y)): True } if not locations_visited else locations_visited

    def __str__(self):
        return f"Position: ({self.x_pos},{self.y_pos}), Direction: {self.direction.value}"
    
    def is_valid_pos(self, x, y):
        maze_dimension = len(maze_map)
        return (0 <= x < maze_dimension) and (0 <= y < maze_dimension)
    
    def get_pos_after_move(self, move):
        direction_map = {
            'North': 0, 0: 'North',
            'East': 1, 1: 'East',
            'South': 2, 2: 'South',
            'West': 3, 3: 'West',
        }
        pos_diff_map = {
            0: (-1,0), # Go North
            1: (0,1),  # Go East
            2: (1,0),  # Go South
            3: (0,-1)  # Go West
        }

        dir_num = direction_map[self.direction.value]
        if move == MOVE.M_UP:
            x_diff, y_diff = pos_diff_map[dir_num]
            new_dir = self.direction
        elif move == MOVE.R_CL_M_UP:
            turn_dir_num = dir_num + 1 if dir_num < 3 else 0
            x_diff, y_diff = pos_diff_map[turn_dir_num]
            new_dir = DIRECTION(direction_map[turn_dir_num])
        else:
            turn_dir_num = dir_num - 1 if dir_num > 0 else 3
            x_diff, y_diff = pos_diff_map[turn_dir_num]
            new_dir = DIRECTION(direction_map[turn_dir_num])

        return (self.x_pos + x_diff, self.y_pos + y_diff, new_dir)

    def get_next_valid_moves(self):
        all_moves = [MOVE.M_UP, MOVE.R_CL_M_UP, MOVE.R_CNTR_CL_M_UP]
        valid_moves = []
        for move in all_moves:
            new_pos_x, new_pos_y, _ = self.get_pos_after_move(move)
            if self.is_valid_pos(new_pos_x, new_pos_y) and maze_map[new_pos_x][new_pos_y] != THING.WALL and not self.locations_visited.get(str((new_pos_x,new_pos_y)), False):
                valid_moves.append(move)
        return valid_moves

    def make_move(self, move):
        new_pos_x, new_pos_y, new_dir = self.get_pos_after_move(move)

        # plot path on map
        # maze_map[new_pos_x][new_pos_y] = THING.DEER
        # maze_map[self.x_pos][self.y_pos] = THING.NOTHING
        # output_maze_map(maze_map)

        self.x_pos, self.y_pos = new_pos_x, new_pos_y
        self.direction = new_dir
        self.locations_visited[str((self.x_pos, self.y_pos))] = True
        self.score += 1 if move == MOVE.M_UP else 1001

        return (self.x_pos, self.y_pos)

    def copy(self):
        return Deer(self.x_pos, self.y_pos, self.direction, self.score, deepcopy(self.locations_visited))

##################################################

def output_maze_map(map):
    for x in map:
        print([i.value for i in x])

maze_map = []
deer, end_tile_pos = None, None
with open('input.txt', 'r') as f:
    x = 0
    for line in f:
        maze_map.append([ THING(x) for x in line.strip()])
        if not deer and 'S' in line:
            deer = Deer(x, line.index('S'))
        elif not end_tile_pos and 'E' in line:
            end_tile_pos = (x, line.index('E'))
        x += 1

# output_maze_map(maze_map)
# print(deer)

##################################################

import sys
min_score = sys.maxsize

def move_deer(deer_obj):
    global min_score

    for next_move in deer_obj.get_next_valid_moves():
        # import pdb;pdb.set_trace()
        deer_alt = deer_obj.copy()
        pos_x, pos_y = deer_alt.make_move(next_move)
        if maze_map[pos_x][pos_y] == THING.END_TILE:
            min_score = deer_alt.score if deer_alt.score < min_score else min_score
            print(min_score)
            # print("REACHED")
        else:
            move_deer(deer_alt)

move_deer(deer)
print(min_score)

# deer.make_move(MOVE.M_UP)
# import pdb; pdb.set_trace()
