'''
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
'''

XMAS_DATA_STREAM = []

with open('data/day9.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        XMAS_DATA_STREAM.append(int(line.strip('\n')))

target_sum = 104054607


def list_sum(cum_list):
    val = 0
    for value in cum_list:
        val += value
    return val


def calc_weakness():
    list_size = 3
    while True:
        offset = 0
        while True:
            first_val = 0 + offset
            last_val = 0 + offset + list_size

            if last_val > len(XMAS_DATA_STREAM):
                list_size += 1
                break

            subset = XMAS_DATA_STREAM[first_val : last_val]

            if list_sum(subset) == target_sum:
                return (min(subset) + max(subset))

            offset += 1

print(calc_weakness())