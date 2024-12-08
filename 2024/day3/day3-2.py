import re

def compute_result(section):
    pattern = r"\d+"
    a, b = re.findall(pattern, section)
    return int(a)*int(b)

f = open('input.txt', 'r')

result_sum = 0
do_true = True

for line in f:
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    sections = re.findall(pattern, line)
    for section in sections:
        if section == "don't()":
            do_true = False
            continue
        if section == "do()":
            do_true = True
            continue
        if do_true:
            result_sum += compute_result(section)

print(result_sum)
