FILE_PATH = 'input.txt'

def check_for_double_and_triple(id):
    letter_count_dict = {}
    double_present = False
    triple_present = False

    for letter in id:
        if letter in letter_count_dict.keys():
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1

    if 2 in letter_count_dict.values():
        double_present = True

    if 3 in letter_count_dict.values():
        triple_present = True

    return double_present, triple_present

f = open(FILE_PATH, 'r')
ids = [id.strip() for id in f]
f.close()

double_count = 0
triple_count = 0

for id in ids:
    double_present, triple_present = check_for_double_and_triple(id)
    if double_present:
        double_count += 1
    if triple_present:
        triple_count += 1

print double_count * triple_count
