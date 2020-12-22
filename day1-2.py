'''
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
'''

import sys

nums = []

# Read the input file
with open('data/day1.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break

        nums.append(int(line))

# Dynamic programming is probably more efficient for the subset sum problem, but, this works quickly enough
for num1 in nums:
    for num2 in nums:
        for num3 in nums:
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
                sys.exit(0)

print('DONE!')