f = open('input.txt', 'r')

location_list_1 = []
location_list_2 = []

for line in f:
    first, second = line.split()
    location_list_1.append(int(first))
    location_list_2.append(int(second))

sum_distance = 0
for left, right in zip(sorted(location_list_1), sorted(location_list_2)):
    sum_distance += abs(left - right)

print(sum_distance)
