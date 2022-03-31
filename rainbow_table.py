from itertools import permutations

possible_inputs = 'abcdefgh'
perms = []

def hasher(perm):
    hashed = perm[-1] * 2
    hashed += perm
    hashed = hashed[::-1]
    if len(hashed) > len(possible_inputs):
        hashed = hashed[: len(possible_inputs)]
    while True:
        if len(hashed) < len(possible_inputs):
            hashed += possible_inputs[-len(hashed)]
        else:
            break
    return hashed

for i in range(1, len(possible_inputs)+1):
    perms += [''.join(p) for p in permutations(possible_inputs, i)]
print(len(perms))

with open('rainbow_table.txt', 'w') as file:
    for p in perms:
        file.writelines(f'{p},{hasher(p)}\n')

