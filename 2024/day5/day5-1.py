from pprint import pprint

f = open('input.txt', 'r')

ordering_rules_asc = {} # { 'no': set('no.s that should come after')}

def update_ordering_rules_dict(first, second):
    if first not in ordering_rules_asc.keys():
        ordering_rules_asc[first] = set([second])
    else:
        ordering_rules_asc[first].add(second)

ordered_pages_middle_sum = 0
for line in f:
    if '|' in line:
        first, second = line.strip().split('|')
        update_ordering_rules_dict(first, second)
    elif ',' in line:
        page_list = line.strip().split(',')
        ordered = True
        for i in range(len(page_list)-1):
            coming_up = set(page_list[i+1:])
            allowed_list = set(ordering_rules_asc.get(page_list[i], []))
            if not coming_up.issubset(allowed_list):
                ordered = False
                break
        if ordered:
            ordered_pages_middle_sum += int(page_list[int(len(page_list)/2)])

print(ordered_pages_middle_sum)
