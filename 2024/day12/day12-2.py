from enum import Enum
from pprint import pprint
import pdb

f = open('/Users/srajendran/Documents/santhosh_personal_git_repos/AdventOfCode/2024/day12/input.txt', 'r')
garden_grid = []
for line in f:
    char_list = list(line.strip())
    garden_grid.append(char_list)

grid_dimension = len(garden_grid) - 1

# pprint(garden_grid)

###############################################################

plant_locations = {}
# { 
#   'A' : [ region-1, region-2 ],
#   'B' : [ region-1, region-2 ]
# }

def is_valid_location(x, y):
    return (0 <= x <= grid_dimension) and (0 <= y <= grid_dimension)

def get_neighbors(x, y, only_valid_neighbors=False):
    neighbors = set([(x-1, y), (x, y+1), (x+1, y), (x, y-1)])
    if not only_valid_neighbors:
        return neighbors

    valid_neighbors = set([])
    for x, y in neighbors:
        if is_valid_location(x, y):
            valid_neighbors.add((x,y))
    return valid_neighbors

checked_locations = set([])
def is_location_in_region(x, y, region, plant):
    checked_locations.add((x,y)) # don't check again

    neighbors = get_neighbors(x, y, True)
    if region.intersection(neighbors):
        return True
    else:
        neighbors_that_are_the_same_plant = []
        for i, j in neighbors:
            if (garden_grid[i][j] == plant) and ((i,j) not in checked_locations):
                neighbors_that_are_the_same_plant += [(i, j)]
        # import pdb; pdb.set_trace()
        for i, j in neighbors_that_are_the_same_plant:
            if is_location_in_region(i, j, region, plant):
                return True
    return False

def find_and_add_plant_to_region(plant, x, y):
    if plant not in plant_locations:
        plant_locations[plant] = [ set([(x,y)]) ]
    else:
        region_found = False
        for i in range(len(plant_locations[plant])):
            region = plant_locations[plant][i]

            # reset checked locations
            global checked_locations
            checked_locations = set([])

            if is_location_in_region(x, y, region, plant):
                plant_locations[plant][i].add((x, y))
                region_found = True
                break
        if not region_found:
            plant_locations[plant].append(set([(x,y)]))

x_pos = 0
for line in garden_grid:
    for y_pos in range(len(line)):
        plant = line[y_pos]
        # print(f"adding plant: {plant} from ({x_pos},{y_pos})")
        find_and_add_plant_to_region(plant, x_pos, y_pos)
    x_pos += 1

# pprint(plant_locations)

###############################################################

class SideType(Enum):
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4

def check_out_of_bounds(x, y):
    return (x < 0) or (x > grid_dimension) or (y < 0) or (y > grid_dimension)

def is_in_group(x_1, y_1, x_2, y_2, side_padding):
    # pdb.set_trace()
    pad_x, pad_y = side_padding
    plant = garden_grid[x_1][y_1]
    if x_1 == x_2:
        # horizontal
        if y_1 < y_2:
            for i in range(y_1, y_2):
                pad_check = False if check_out_of_bounds(x_1 + pad_x, i + pad_y) else (garden_grid[x_1 + pad_x][i + pad_y] == plant)
                if (garden_grid[x_1][i] != plant) or pad_check:
                    return False
        else:
            for i in range(y_2, y_1):
                pad_check = False if check_out_of_bounds(x_1 + pad_x, i + pad_y) else (garden_grid[x_1 + pad_x][i + pad_y] == plant)
                if (garden_grid[x_1][i] != plant) or pad_check:
                    return False
    else:
        if x_1 < x_2:
            for i in range(x_1, x_2):
                pad_check = False if check_out_of_bounds(i + pad_x, y_1 + pad_y) else (garden_grid[i + pad_x][y_1 + pad_y] == plant)
                if (garden_grid[i][y_1] != plant) or pad_check:
                    return False
        else:
            for i in range(x_2, x_1):
                pad_check = False if check_out_of_bounds(i + pad_x, y_1 + pad_y) else (garden_grid[i + pad_x][y_1 + pad_y] == plant)
                if (garden_grid[i][y_1] != plant) or pad_check:
                    return False
    return True

def calculate_sides(region):
    sides_list_horizontal = []
    sides_list_vertical = []
    side_to_calculate = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 0->top, 1->botton, 2->left, 3->right

    # TOP
    sides = {}
    for location in region:
        print(location)
        if tuple(sum(coords) for coords in zip(location, side_to_calculate[0])) in region:
            # neighbor is the same plant, so don't count as side to fence
            continue
        x, y = location
        if x not in sides:
            sides[x] = [ [y] ]
        else:
            found_group = False
            for group in sides[x]:
                if found_group:
                    break
                for coordinate in group:
                    if is_in_group(x, coordinate, x, y, side_to_calculate[0]):
                        group.append(y)
                        found_group = True
                        break
            if not found_group:
                sides[x].append([y])
    sides_list_horizontal.append(sides)

    # BOTTOM
    sides = {}
    for location in region:
        print(location)
        if tuple(sum(coords) for coords in zip(location, side_to_calculate[1])) in region:
            # neighbor is the same plant, so don't count as side to fence
            continue
        x, y = location
        if x not in sides:
            sides[x] = [ [y] ]
        else:
            found_group = False
            for group in sides[x]:
                if found_group:
                    break
                for coordinate in group:
                    if is_in_group(x, coordinate, x, y, side_to_calculate[1]):
                        group.append(y)
                        found_group = True
                        break
            if not found_group:
                sides[x].append([y])
    sides_list_horizontal.append(sides)

    # LEFT
    sides = {}
    for location in region:
        print(location)
        if tuple(sum(coords) for coords in zip(location, side_to_calculate[2])) in region:
            # neighbor is the same plant, so don't count as side to fence
            continue
        x, y = location
        if y not in sides:
            sides[y] = [ [x] ]
        else:
            found_group = False
            for group in sides[y]:
                if found_group:
                    break
                for coordinate in group:
                    if is_in_group(coordinate, y, x, y, side_to_calculate[2]):
                        group.append(x)
                        found_group = True
                        break
            if not found_group:
                sides[y].append([x])
    sides_list_vertical.append(sides)

    # RIGHT
    sides = {}
    for location in region:
        print(location)
        if tuple(sum(coords) for coords in zip(location, side_to_calculate[3])) in region:
            # neighbor is the same plant, so don't count as side to fence
            continue
        x, y = location
        if y not in sides:
            sides[y] = [ [x] ]
        else:
            found_group = False
            for group in sides[y]:
                if found_group:
                    break
                for coordinate in group:
                    if is_in_group(coordinate, y, x, y, side_to_calculate[3]):
                        group.append(x)
                        found_group = True
                        break
            if not found_group:
                sides[y].append([x])
    sides_list_vertical.append(sides)

    sides_count = 0
    for sides_list in sides_list_horizontal + sides_list_vertical:
        for values in sides_list.values():
            sides_count += len(values)

    return sides_count

def calculate_total_price():
    total_price = 0

    for plant in plant_locations:
        for region in plant_locations[plant]:
            region_area = len(region)
            region_perimeter = calculate_sides(region)
            total_price += region_area * region_perimeter

    return total_price

print(calculate_total_price())
