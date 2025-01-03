TOWEL_OPTIONS = []
TOWEL_DESIGNS = []

with open("input.txt", 'r') as f:
    TOWEL_OPTIONS += f.readline().strip().split(', ')
    f.readline()

    for line in f:
        TOWEL_DESIGNS.append(line.strip())

# print(TOWEL_OPTIONS)
# print(TOWEL_DESIGNS)

####################################################################

def is_design_possible(towel_so_far, requested_design):
    if towel_so_far not in designs_checked_already:
        designs_checked_already.add(towel_so_far)
    else:
        return False

    if towel_so_far == requested_design:
        return True

    for option in TOWEL_OPTIONS:
        new_towel = towel_so_far + option
        if requested_design.startswith(new_towel) and is_design_possible(new_towel, requested_design):
            return True

    return False

designs_possible = 0
for design in TOWEL_DESIGNS:
    designs_checked_already = set([])
    if is_design_possible('', design):
        designs_possible += 1

print(designs_possible)
