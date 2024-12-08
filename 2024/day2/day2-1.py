def check_if_safe(levels):
    levels_diff_set_inc = set([1,2,3])
    levels_diff_set_dec = set([-1,-2,-3])
    for i in range(len(levels)-1):
        levels_diff = levels[i+1] - levels[i]
        levels_diff_set_inc.add(levels_diff)
        levels_diff_set_dec.add(levels_diff)
    if len(levels_diff_set_inc) == 3 or len(levels_diff_set_dec) == 3:
        return True
    return False

f = open('input.txt', 'r')

safe_reports = 0
for report in f:
    levels = [int(x) for x in report.split()]
    safe_reports += 1 if check_if_safe(levels) else 0

print(safe_reports)
