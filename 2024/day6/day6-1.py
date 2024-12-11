from enum import Enum

f = open('input.txt', 'r')

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Guard():
    def __init__(self, start_position, map):
        self.map = map
        self.guard_pos = start_position
        self.guard_direction = Direction.NORTH
        # self.path = [start_position]
        self.locations_visited = set([start_position])
        self.valid_x_coordinate = range(len(map))
        self.valid_y_coordinate = range(len(map[0]))

    def update_status(self, pos, direction):
        self.guard_pos = pos
        self.guard_direction = direction
        # self.path.append(pos)
        if pos not in self.locations_visited:
            self.locations_visited.add(pos)

    def take_next_step(self):
        x, y = self.guard_pos
        if self.guard_direction == Direction.NORTH:
            next_x, next_y = x-1, y
        elif self.guard_direction == Direction.EAST:
            next_x, next_y = x, y+1
        elif self.guard_direction == Direction.SOUTH:
            next_x, next_y = x+1, y
        else: # WEST
            next_x, next_y = x, y-1

        if (next_x not in self.valid_x_coordinate) or (next_y not in self.valid_x_coordinate):
            raise Exception("Out of Bounds")
        
        if self.map[next_x][next_y] == '#':
            next_x, next_y = self.guard_pos # be in the same location, but turn clockwise
            if self.guard_direction == Direction.NORTH:
                self.guard_direction = Direction.EAST
            elif self.guard_direction == Direction.EAST:
                self.guard_direction = Direction.SOUTH
            elif self.guard_direction == Direction.SOUTH:
                self.guard_direction = Direction.WEST
            else: # WEST
                self.guard_direction = Direction.NORTH

        self.update_status((next_x, next_y), self.guard_direction)

    def __str__(self):
        return_string = ""
        return_string += f"Position: {self.guard_pos}\n"
        return_string += f"Direction: {self.guard_direction}\n"
        # return_string += f"Path followed: {self.path}\n"
        return_string += f"Locations visited: {self.locations_visited}"
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

guard = Guard((guard_x_pos, guard_y_pos), grid_map)

##################################################

while(True):
    try:
        guard.take_next_step()
    except:
        break

print(len(guard.locations_visited))
