from sets import Set

with open('input.txt') as f:
    num_list = [int(n) for n in f]

sum = 0
sum_set = Set([])

while True:
    for n in num_list:
        sum += int(n)

        pre_length = len(sum_set)
        sum_set.add(sum)

        if len(sum_set) == pre_length:
            print sum
            exit()
