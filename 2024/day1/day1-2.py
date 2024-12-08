f = open('input.txt', 'r')

location_list_1 = []
location_list_2 = []
location_list_2_count = {}

for line in f:
    first, second = line.split()
    location_list_1.append(first)
    location_list_2.append(second)
    if second in location_list_2_count.keys():
        location_list_2_count[second] += 1
    else:
        location_list_2_count[second] = 1

similarity_score = 0
for location_id in location_list_1:
    similarity_score += int(location_id) * int(location_list_2_count.get(location_id, 0))

print(similarity_score)
