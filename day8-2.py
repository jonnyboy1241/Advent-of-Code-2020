'''
--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
'''

import copy

orig_commands = []
new_commands = []

with open('data/day8.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break

        line = line.strip('\n')

        orig_commands.append([line.split()[0], int(line.split()[1])])


def change_jmp_nop(jmp_nop_to_change):
    global new_commands

    jmp_nop_counter = 0
    new_commands = copy.deepcopy(orig_commands)

    for i in range(len(orig_commands)):
        curr_instruction = orig_commands[i][0]

        if curr_instruction == 'jmp' or curr_instruction == 'nop':
            if jmp_nop_to_change == jmp_nop_counter:
                if curr_instruction == 'jmp':
                    new_commands[i][0] = 'nop'
                else:
                    new_commands[i][0] = 'jmp'
                return
            jmp_nop_counter += 1
        


def attempt_run(jmp_nop_to_change):
    change_jmp_nop(jmp_nop_to_change)

    location = 0
    accumulator = 0
    previously_visited = []

    while True:
        if location in previously_visited:
            return attempt_run(jmp_nop_to_change + 1)

        if location == len(orig_commands):
            return accumulator

        current_command = new_commands[location]
        previously_visited.append(location)

        if current_command[0] == 'nop':
            location += 1
        
        elif current_command[0] == 'acc':
            accumulator += current_command[1]
            location += 1

        elif current_command[0] == 'jmp':
            location += current_command[1]

        else:
            print('SOMETHING WENT HORRIBLY WRONG')

accumulator = attempt_run(0)
print(accumulator)