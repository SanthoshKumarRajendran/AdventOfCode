CONNECTIONS = set([])
COMPUTERS = set([])

with open('input.txt', 'r') as f:
    for line in f:
        comp_1, comp_2 = line.strip().split('-')
        CONNECTIONS.add((comp_1, comp_2))
        CONNECTIONS.add((comp_2, comp_1))
        COMPUTERS.add(comp_1)

#################################################################

ALL_NETWORKS = [set([comp]) for comp in COMPUTERS]

for network in ALL_NETWORKS:
    for comp in COMPUTERS:
        if all([(comp, n) in CONNECTIONS for n in network]):
            network.add(comp)

print(','.join(sorted(max(ALL_NETWORKS, key=len))))
