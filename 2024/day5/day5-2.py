f = open('input.txt', 'r')

ordering_rules_asc = {} # { 'no': set('no.s that should come after')}

pages_list = []

def update_ordering_rules_dict(first, second):
    if first not in ordering_rules_asc.keys():
        ordering_rules_asc[first] = set([second])
    else:
        ordering_rules_asc[first].add(second)

def sorted_page_number_order(page_no_list):
    sorted_page_number_list = []
    for p_no in page_no_list:
        if (len(sorted_page_number_list) == 0) or (p_no not in ordering_rules_asc):
            sorted_page_number_list.append(p_no)
        else:
            added = False
            for i in range(len(sorted_page_number_list)):
                if sorted_page_number_list[i] in ordering_rules_asc[p_no]:
                    sorted_page_number_list = sorted_page_number_list[:i] + [p_no] + sorted_page_number_list[i:]
                    added = True
                    break
            if not added:
                sorted_page_number_list.append(p_no)
    return sorted_page_number_list

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
        if not ordered:
            sorted_page_order = sorted_page_number_order(page_list)
            ordered_pages_middle_sum += int(sorted_page_order[int(len(sorted_page_order)/2)])

print(ordered_pages_middle_sum)
