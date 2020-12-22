'''
--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''

passes = []

with open('data/day5.txt', 'r') as file:
    while True:
        line = file.readline().strip('\n')
        if not line:
            break
        passes.append(line)

def calc_id(boarding_pass):
    rows = boarding_pass[:-3]
    cols = boarding_pass[-3:]

    rows = rows.replace('F', '0').replace('B', '1')
    cols = cols.replace('L', '0').replace('R', '1')

    return 8 * int(rows, 2) + int(cols, 2)

seat_ids = list(range(0, 833))

for b_pass in passes:
    val = calc_id(b_pass)

    seat_ids.remove(val)

print(seat_ids[-1])