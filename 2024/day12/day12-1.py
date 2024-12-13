from pprint import pprint

f = open('input.txt', 'r')
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

def calculate_perimeter(region):
    perimeter = 0
    for location in region:
        x, y = location
        neighbors = get_neighbors(x, y)
        perimeter += len(neighbors - region)
    return perimeter

def calculate_total_price():
    total_price = 0

    for plant in plant_locations:
        for region in plant_locations[plant]:
            region_area = len(region)
            region_perimeter = calculate_perimeter(region)
            # import pdb; pdb.set_trace()
            total_price += region_area * region_perimeter

    return total_price

print(calculate_total_price())
