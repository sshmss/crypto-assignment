import time

input_hash = input('type password which includes abcdefhijkl only and length 7 or lower: ')
with open('rainbow_table.txt', 'r') as file:
    start = time.time()
    for line in file:
        pair = line.strip().split(',')
        password = pair[0]
        hash = pair[1]
        if input_hash == hash:
            print(f'{input_hash} cracked in {time.time() - start}s')
            print(f'The password is {password}')
            break
