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

with open(INPUT_FILE_PATH, 'r') as f:
    for claim in f:
        parse_claim_and_update_tracker_dict(claim)

print len(atleast_on_two_claims)
