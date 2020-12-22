'''
--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
'''

groups = []

with open('data/day6.txt', 'r') as file:
    group = []
    while True:
        line = file.readline()
        if not line:
            groups.append(group)
            break

        line = line.strip('\n')

        if line == '':
            groups.append(group)
            group = []
            continue

        group.append(line)

number_yesses = 0

for group in groups:
    num_people = len(group)
    
    answers = ''
    
    for response in group:
        answers += response

    char_freq = {}

    for i in answers:
        if i in char_freq:
            char_freq[i] += 1
        else:
            char_freq[i] = 1

    for key, value in char_freq.items():
        if value == num_people:
            number_yesses += 1

print(number_yesses)