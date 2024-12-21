from pprint import pprint
import sys

def output_maze_map(map):
    for x in map:
        print(x)

maze_map = []
start_pos, end_pos = (), ()

with open('input.txt', 'r') as f:
    x = 0
    for line in f:
        char_list = list(line.strip())
        maze_map.append(char_list)
        if 'S' in line:
            start_pos = (x, line.index('S'))
        elif 'E' in line:
            end_pos = (x, line.index('E'))
            char_list[end_pos[1]] = '.'
        x += 1

# output_maze_map(maze_map)
# print(start_pos)
# print(end_pos)

##########################################################

# direction
# 0 -> East
# 1 -> South
# 2 -> West
# 3 -> North

pos_diff_map = {
    0: (0, 1),  # -> East
    1: (1, 0),  # 1 -> South
    2: (0, -1), # 2 -> West
    3: (-1, 0)  # 3 -> North
}

min_score = sys.maxsize
visited = set([])
visited_by_score = {}
process_queue = []
visited_locations_min_score = {}

process_queue.append((*start_pos, 0, 0, ''))
process_queue.append((*start_pos, 3, 1000, ''))
while(process_queue):
    x, y, dir, score, visited_by_me = process_queue.pop(0)

    if (x, y, dir) in visited and score > visited_locations_min_score[(x, y, dir)]:
        continue

    # Debug
    # print(f"(Processing pos: {x},{y}, dir:{dir})")
    # import pdb; pdb.set_trace()

    if (x,y) == end_pos:
        # print(f"Reached End Tile with score {score}")
        if score in visited_by_score:
            visited_by_score[score] += visited_by_me
        else:
            visited_by_score[score] = visited_by_me
        min_score = score if score < min_score else min_score
        continue

    visited.add((x, y, dir))
    visited_by_me += f" {x},{y}"
    visited_locations_min_score[(x, y, dir)] = score

    x_diff, y_diff = pos_diff_map[dir]
    next_x, next_y = x + x_diff, y + y_diff

    if maze_map[next_x][next_y] == '.' and ((next_x, next_y, dir) not in visited or score+1 < visited_locations_min_score[(next_x, next_y, dir)]):
        process_queue.append((next_x, next_y, dir, score+1, visited_by_me))

    left_turn_dir = dir + 1 if dir < 3 else 0
    if maze_map[next_x][next_y] == '.' and ((next_x, next_y, left_turn_dir) not in visited or score+1001 < visited_locations_min_score[(next_x, next_y, left_turn_dir)]):
        process_queue.append((next_x, next_y, left_turn_dir, score+1001, visited_by_me))

    right_turn_dir = dir - 1 if dir > 0 else 3
    if maze_map[next_x][next_y] == '.' and ((next_x, next_y, right_turn_dir) not in visited or score+1001 < visited_locations_min_score[(next_x, next_y, right_turn_dir)]):
        process_queue.append((next_x, next_y, right_turn_dir, score+1001, visited_by_me))

print(min_score)
# pprint(visited_by_score)
print(len(set(visited_by_score[min_score].split())) + 1)
