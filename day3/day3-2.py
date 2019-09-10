from sets import Set
import re

INPUT_FILE_PATH = 'input.txt'
atleast_on_one_claim = Set([])
atleast_on_two_claims = Set([])

def update_tracker_dict(xpos, ypos, length, width):
    for x in xrange(int(xpos), int(xpos) + int(length)):
        for y in xrange(int(ypos), int(ypos) + int(width)):
            if (1000*x + y) in atleast_on_one_claim:
                atleast_on_two_claims.add(1000*x + y)
            else:
                atleast_on_one_claim.add(1000*x + y)

def parse_claim_and_update_tracker_dict(claim):
    m = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim)
    update_tracker_dict(m.group(2), m.group(3), m.group(4), m.group(5))

def check_if_intact(xpos, ypos, length, width):
    for x in xrange(int(xpos), int(xpos) + int(length)):
        for y in xrange(int(ypos), int(ypos) + int(width)):
            if (1000*x + y) in atleast_on_two_claims:
                return False
    return True

def parse_claim_and_print_intact_claim(claim):
    m = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim)
    if check_if_intact(m.group(2), m.group(3), m.group(4), m.group(5)):
        print m.group(1)
        exit

with open(INPUT_FILE_PATH, 'r') as f:
    for claim in f:
        parse_claim_and_update_tracker_dict(claim)
    f.seek(0)
    for claim in f:
        parse_claim_and_print_intact_claim(claim)
