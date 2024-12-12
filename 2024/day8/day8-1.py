from itertools import combinations

f = open('input.txt', 'r')

city_map, antenna_positions_dict, antenna_positions_set, x = [], {}, set([]), 0
for line in f:
    char_list = list(line.strip())
    city_map.append(char_list)
    for y in range(len(char_list)):
        if char_list[y] != '.':
            antenna_positions_set.add((x,y))
            if char_list[y] not in antenna_positions_dict.keys():
                antenna_positions_dict[char_list[y]] = [(x,y)]
            else:
                antenna_positions_dict[char_list[y]].append((x,y))
    x += 1

##################################################################

valid_x_coordinate = range(len(city_map))
valid_y_coordinate = range(len(city_map[0]))
anti_node_positions = set([])

for antenna in antenna_positions_dict.keys():
    if len(antenna_positions_dict[antenna]) > 1:
        combos = combinations(antenna_positions_dict[antenna], 2)
        for combo in combos:
            first, second = combo
            x_diff, y_diff = (first[0] - second[0]), (first[1] - second[1])

            mult = 1
            while((first[0] + mult * x_diff) in valid_x_coordinate) and ((first[1] + mult * y_diff) in valid_y_coordinate):
                anti_node_positions.add((first[0] + mult * x_diff, first[1] + mult * y_diff))
                mult += 1

            mult = 1
            while ((second[0] - mult * x_diff) in valid_x_coordinate) and ((second[1] - mult * y_diff) in valid_y_coordinate):
                anti_node_positions.add((second[0] - mult * x_diff, second[1] - mult * y_diff))
                mult += 1

print(len(anti_node_positions.union(antenna_positions_set)))
