from copy import deepcopy

LAN_DATA = {}
with open('input.txt', 'r') as f:
    for line in f:
        comp_1, comp_2 = line.strip().split('-')
        if comp_1 not in LAN_DATA.keys():
            LAN_DATA[comp_1] = set([])
        if comp_2 not in LAN_DATA.keys():
            LAN_DATA[comp_2] = set([])
        LAN_DATA[comp_1].add(comp_2)
        LAN_DATA[comp_2].add(comp_1)

# print(LAN_DATA)

#################################################################

GROUPS_OF_THREE = set([])

for comp_1 in LAN_DATA.keys():
    three_set = set([comp_1])

    for comp_2 in LAN_DATA[comp_1]:
        three_set_ext = deepcopy(three_set)
        three_set_ext.add(comp_2)

        for comp_3 in LAN_DATA[comp_2]:
            if comp_1 in LAN_DATA[comp_3]:
                if comp_1.startswith('t') or comp_2.startswith('t') or comp_3.startswith('t'):
                    GROUPS_OF_THREE.add(frozenset([comp_1, comp_2, comp_3]))

print(len(GROUPS_OF_THREE))
