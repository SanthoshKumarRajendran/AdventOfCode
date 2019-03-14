from sets import Set

FILE_PATH = 'input.txt'

f = open(FILE_PATH, 'r')
ids = [list(id.strip()) for id in f]
f.close()

def find_one_off(list_1, list_2):
    diff = 0
    result = ''

    for l1, l2 in zip(list_1, list_2):
        if l1 != l2:
            diff += 1
            if diff > 1:
                return None
        else:
            result += l1

    return result

iteration = 0
for outer_id_list in ids:
    for inner_id_list in ids[iteration+1:]:
        correct_id = find_one_off(outer_id_list, inner_id_list)
        if correct_id:
            print correct_id
    iteration += 1
