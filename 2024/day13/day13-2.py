import re

claw_machines = []

def populate_claw_machine(input):
    button_a_pattern = r"Button A: X\+(\d+), Y\+(\d+)"
    button_b_pattern = r"Button B: X\+(\d+), Y\+(\d+)"
    prize_pattern = r"Prize: X=(\d+), Y=(\d+)"

    m = re.search(button_a_pattern, input[0].strip())
    a_x_coeff, a_y_coeff = int(m.group(1)), int(m.group(2))

    m = re.search(button_b_pattern, input[1].strip())
    b_x_coeff, b_y_coeff = int(m.group(1)), int(m.group(2))

    m = re.search(prize_pattern, input[2].strip())
    prize_x, prize_y = 10000000000000 + int(m.group(1)), 10000000000000 + int(m.group(2))

    claw_machines.append({
        'a': { 'x': a_x_coeff, 'y': a_y_coeff},
        'b': { 'x': b_x_coeff, 'y': b_y_coeff},
        'p': { 'x': prize_x, 'y': prize_y}
    })

with open('input.txt', 'r') as f:
    lines = f.readlines()

line_count = len(lines)
for chunk in [lines[i*4 : i*4 + 3] for i in range(int(line_count/4)+1)]:
    populate_claw_machine(chunk)

#####################################################

token_cost = 0
for claw_machine in claw_machines:
    but_a_x, but_a_y = claw_machine['a']['x'], claw_machine['a']['y']
    but_b_x, but_b_y = claw_machine['b']['x'], claw_machine['b']['y']
    prize_x, prize_y = claw_machine['p']['x'], claw_machine['p']['y']

    but_b_count = (prize_x * but_a_y - prize_y * but_a_x)/(but_b_x * but_a_y - but_b_y * but_a_x)
    but_a_count = (prize_x - but_b_x * but_b_count)/but_a_x

    if (but_a_count.is_integer()) and (but_b_count.is_integer()):
        token_cost += but_a_count * 3 + but_b_count

print(token_cost)
