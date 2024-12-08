import re

def compute_result(section):
    pattern = r"\d+"
    a, b = re.findall(pattern, section)
    return int(a)*int(b)

f = open('input.txt', 'r')

result_sum = 0
for line in f:
    pattern = r"mul\(\d+,\d+\)"
    sections = re.findall(pattern, line)
    for section in sections:
        result_sum += compute_result(section)

print(result_sum)
