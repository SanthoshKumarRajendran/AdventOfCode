f = open('input.txt', 'r')

char_grid = []
for line in f:
    char_list = list(line.strip())
    char_grid.append(char_list)

##################################################

SEARCH_PATTERN_COUNT = 0
exception_count = 0

def found_pattern(x, y):
    # (x-1,y-1) . (x-1,y+1)
    #     .   (x,y)   .
    # (x+1,y-1) . (x+1,y+1)
    try:
        if (char_grid[x-1][y-1] == 'M' and char_grid[x+1][y+1] == 'S') or (char_grid[x-1][y-1] == 'S' and char_grid[x+1][y+1] == 'M'):
            if (char_grid[x+1][y-1] == 'M' and char_grid[x-1][y+1] == 'S') or (char_grid[x+1][y-1] == 'S' and char_grid[x-1][y+1] == 'M'):
                return True
        return False
    except:
        return False

for x in range(1,len(char_grid)-1):
    for y in range(1,len(char_grid[x])-1):
        if char_grid[x][y] == 'A':
            SEARCH_PATTERN_COUNT += 1 if found_pattern(x,y) else 0

print(SEARCH_PATTERN_COUNT)
