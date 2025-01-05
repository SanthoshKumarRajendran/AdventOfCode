LOCKS = []
KEYS = []
CYLINDER_HEIGHT = 7
CYLINDER_LENGTH = 5

def process_input_batch(input_batch):
    lock_or_key_schema = [0] * CYLINDER_LENGTH
    if input_batch[0][0] == '#':
        for row in input_batch[1:]:
            for i in range(CYLINDER_LENGTH):
                lock_or_key_schema[i] += 1 if row[i] == '#' else 0
        LOCKS.append(lock_or_key_schema)
    else:
        for row in input_batch[:-1]:
            for i in range(CYLINDER_LENGTH):
                lock_or_key_schema[i] += 1 if row[i] == '#' else 0
        KEYS.append(lock_or_key_schema)

with open('input.txt', 'r') as f:
    batch=[]
    for line in f:
        if not line.strip():
            continue
        batch.append(line.strip())
        if len(batch) == CYLINDER_HEIGHT:
            process_input_batch(batch)
            batch=[]

print(LOCKS)
print(KEYS)

#################################################################

MATHCES_FOUND = 0

for lock in LOCKS:
    for key in KEYS:
        match = True
        for i in range(CYLINDER_LENGTH):
            if (key[i] + lock[i]) > (CYLINDER_HEIGHT - 2):
                match = False
                break
        MATHCES_FOUND += 1 if match else 0

print(MATHCES_FOUND)
