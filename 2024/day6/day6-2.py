from copy import deepcopy
from enum import Enum
from pprint import pprint

f = open('input.txt', 'r')

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class OutOfBoundsException(Exception):
    pass

class LoopDetectedException(Exception):
    pass

class Guard():
    def __init__(self, start_position, map):
        self.map = map
        self.guard_pos = start_position
        self.guard_direction = Direction.NORTH
        self.path = { (start_position, self.guard_direction): True }
        self.valid_x_coordinate = range(len(map))
        self.valid_y_coordinate = range(len(map[0]))

    def update_status(self, pos, direction):
        self.guard_pos = pos
        self.guard_direction = direction
        self.path[(pos,direction)] = True
    
    def compute_next_step(self, x, y, direction):
        next_step_map = {
            Direction.NORTH: (x-1, y),
            Direction.EAST: (x, y+1),
            Direction.SOUTH: (x+1, y),
            Direction.WEST: (x, y-1)
        }
        return next_step_map[direction]

    def rotate_clockwise(self, direction):
        rotate_map = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }
        return rotate_map[direction]

    def take_next_step(self):
        x, y = self.guard_pos
        next_x, next_y = self.compute_next_step(x, y, self.guard_direction)

        if (next_x not in self.valid_x_coordinate) or (next_y not in self.valid_x_coordinate):
            raise OutOfBoundsException()

        if self.path.get(((next_x, next_y), self.guard_direction), False):
            raise LoopDetectedException("")

        if self.map[next_x][next_y] == '#':
            next_x, next_y = self.guard_pos # be in the same location, but turn clockwise
            self.guard_direction = self.rotate_clockwise(self.guard_direction)

        self.update_status((next_x, next_y), self.guard_direction)

    def __str__(self):
        return_string = ""
        return_string += f"Position: {self.guard_pos}\n"
        return_string += f"Direction: {self.guard_direction}\n"
        return_string += f"Path followed: {self.path}\n"
        return return_string

##################################################    

grid_map = []
guard_x_pos, guard_y_pos, x_pos = 0, 0, 0
for line in f:
    char_list = list(line.strip())
    grid_map.append(char_list)
    if '^' in char_list:
        guard_x_pos, guard_y_pos = x_pos, char_list.index('^')
    x_pos += 1

##################################################

obstacle_positions_candidates = set([])
obstacle_positions_that_cause_loop = 0

guard = Guard((guard_x_pos, guard_y_pos), grid_map)
while(True):
    try:
        guard.take_next_step()
        if guard.guard_pos != (guard_x_pos, guard_y_pos):
            obstacle_positions_candidates.add(guard.guard_pos)
    except:
        break

for i, j in obstacle_positions_candidates:
    alternate_grid_map = deepcopy(grid_map)
    alternate_grid_map[i][j] = '#'
    guard = Guard((guard_x_pos, guard_y_pos), alternate_grid_map)
    while(True):
        try:
            guard.take_next_step()
        except OutOfBoundsException:
            break
        except LoopDetectedException:
            obstacle_positions_that_cause_loop += 1
            print(f"({i},{j}) will trigger loop. position_count: {obstacle_positions_that_cause_loop}")
            break            

print(obstacle_positions_that_cause_loop)
