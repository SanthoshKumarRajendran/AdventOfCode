f = open('input.txt')

sum = 0

for n in f:
    sum += int(n)

f.close()
print sum
