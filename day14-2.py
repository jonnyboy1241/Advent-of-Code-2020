'''
--- Part Two ---
For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.

A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1

When this program goes to write to memory address 42, it first applies the bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X

After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)

Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX

This results in an address with three floating bits, causing writes to eight memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)

The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?
'''

def get_binary_value(decimal_value):
    return format(decimal_value, '036b')


def mask_value(mask, binary_value):
    masked_binary_value = ''

    for i in range(len(mask)):
        if mask[i] == '1':
            masked_binary_value += '1'
        elif mask[i] == '0':
            masked_binary_value += binary_value[i]
        elif mask[i] == 'X':
            masked_binary_value += 'X'
    
    return masked_binary_value


def all_values(value):
    ret_val = []

    num_X = value.count('X')
    loc_X = []

    for i in range(len(value)):
        if value[i] == 'X':
            loc_X.append(i)

    for i in range(2 ** num_X):
        current_value = value
        replacement_value = format(i, '0' + str(num_X) + 'b')

        for i in range(len(loc_X)):
            replacement_index = loc_X[i]
            current_value = current_value[:replacement_index] + replacement_value[i]  + current_value[replacement_index + 1:]

        ret_val.append(int(current_value, 2))

    return ret_val


def apply_mask(mask, value):
    binary_value = get_binary_value(value)
    mask_val = mask_value(mask, binary_value)
    return all_values(mask_val)

raw_data = []

with open('data/day14.txt', 'r') as file:
    while True:
        line = file.readline().strip('\n')
        if not line:
            break
        raw_data.append(line)


values_in_memory = {}
current_mask = ''

for line in raw_data:
    if line[0:4] == 'mask':
        current_mask = line.split(' ')[-1]
    else:
        split_line = line.split(' ')
        # This value is not masked in v2. This is the value to write to the masked memory value
        value_in_memory = int(split_line[-1])

        # We're now masking this value
        mem_loc = int(split_line[0][4:-1])

        memory_locations_to_write_to = apply_mask(current_mask, mem_loc)

        for loc in memory_locations_to_write_to:
            values_in_memory[loc] = value_in_memory

val = 0

for key in values_in_memory:
    val += values_in_memory[key]

print(val)